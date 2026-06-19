"""Entry point for the Snake game.

Running ``python -m snake_game`` will launch a Tkinter window that displays the
game and handles user input.
"""

import sys
import tkinter as tk
from tkinter import messagebox

from .game import Game
from . import constants


def _draw_snake(canvas: tk.Canvas, snake_coords):
    """Draw each segment of the snake as a green rectangle."""
    for x, y in snake_coords:
        canvas.create_rectangle(
            x * constants.CELL_SIZE,
            y * constants.CELL_SIZE,
            (x + 1) * constants.CELL_SIZE,
            (y + 1) * constants.CELL_SIZE,
            fill="green",
            tag="snake",
        )


def _draw_food(canvas: tk.Canvas, food_coord):
    """Draw the food as a red oval."""
    if food_coord:
        x, y = food_coord
        canvas.create_oval(
            x * constants.CELL_SIZE,
            y * constants.CELL_SIZE,
            (x + 1) * constants.CELL_SIZE,
            (y + 1) * constants.CELL_SIZE,
            fill="red",
            tag="food",
        )


def _update_score(canvas: tk.Canvas, score: int, high_score: int):
    canvas.delete("score")
    canvas.create_text(
        10,
        10,
        anchor="nw",
        text=f"Score: {score}  High: {high_score}",
        font=("Arial", 12),
        fill="white",
        tag="score",
    )


def _game_loop(root: tk.Tk, canvas: tk.Canvas, game: Game):
    alive = game.step()
    canvas.delete("snake", "food")
    _draw_snake(canvas, game.get_snake_coords())
    _draw_food(canvas, game.get_food_coord())
    _update_score(canvas, game.score, game.high_score)

    if not alive:
        game.save_high_score()
        messagebox.showinfo("Game Over", f"Your score: {game.score}\nHigh score: {game.high_score}")
        root.destroy()
        return

    # schedule next tick using the current delay
    root.after(game.get_delay(), lambda: _game_loop(root, canvas, game))


def _on_key(event, game: Game):
    key_map = {
        "Up": "Up",
        "Down": "Down",
        "Left": "Left",
        "Right": "Right",
    }
    direction = key_map.get(event.keysym)
    if direction:
        game.change_direction(direction)


def main():
    root = tk.Tk()
    root.title("Snake Game")
    root.resizable(False, False)
    canvas = tk.Canvas(root, width=constants.WINDOW_SIZE, height=constants.WINDOW_SIZE, bg="black")
    canvas.pack()

    game = Game()

    # bind arrow keys
    root.bind("<Up>", lambda e: _on_key(e, game))
    root.bind("<Down>", lambda e: _on_key(e, game))
    root.bind("<Left>", lambda e: _on_key(e, game))
    root.bind("<Right>", lambda e: _on_key(e, game))

    # start loop
    root.after(game.get_delay(), lambda: _game_loop(root, canvas, game))
    root.mainloop()


if __name__ == "__main__":
    # allow running as a script directly
    sys.exit(main())
