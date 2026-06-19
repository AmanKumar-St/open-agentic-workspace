"""Simple demo to exercise the Snake game logic without GUI.
It creates a Game instance, prints initial state, performs a few steps,
and prints the resulting state. This is used for verification that the
core logic runs without errors.
"""

from snake_game.game import Game

if __name__ == "__main__":
    game = Game()
    print("Initial snake:", game.get_snake_coords())
    print("Food:", game.get_food_coord())
    # perform 5 steps (may eat food depending on random placement)
    for i in range(5):
        alive = game.step()
        print(f"Step {i+1} alive={alive}, snake={game.get_snake_coords()}, score={game.score}, delay={game.get_delay()}")
        if not alive:
            break
    # Save high score (should be 0 if never ate food)
    game.save_high_score()
    print("High score file content (if created):")
    try:
        with open('high_score.txt', 'r') as f:
            print(f.read().strip())
    except Exception as e:
        print("No high_score.txt", e)
