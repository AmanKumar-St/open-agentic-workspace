"""Core game logic for the Snake game.

The :class:`Game` class is deliberately UI‑agnostic – it only knows about the grid,
positions, direction, score and speed. The Tkinter UI (in ``__main__.py``) pulls
state from this class and renders it.

All public methods are designed to be easy to unit‑test without a graphical
environment.
"""

import os
import random
from typing import List, Tuple

from . import constants

# Type alias for a grid coordinate (column, row)
Coord = Tuple[int, int]


class Game:
    """Represent the state and rules of a Snake game.

    Parameters
    ----------
    width : int, optional
        Width of the window in pixels. Defaults to ``constants.WINDOW_SIZE``.
    height : int, optional
        Height of the window in pixels. Defaults to ``constants.WINDOW_SIZE``.
    cell_size : int, optional
        Size of a single grid cell in pixels. Defaults to ``constants.CELL_SIZE``.
    high_score_path : str, optional
        Path to the file used for persisting the high score. If omitted the
        default ``constants.HIGH_SCORE_FILE`` in the current working directory
        is used.
    """

    def __init__(
        self,
        width: int = constants.WINDOW_SIZE,
        height: int = constants.WINDOW_SIZE,
        cell_size: int = constants.CELL_SIZE,
        high_score_path: str | None = None,
    ) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cols = self.width // self.cell_size
        self.rows = self.height // self.cell_size

        # Game state
        self.snake: List[Coord] = []
        self.direction: str = "Right"  # one of "Up", "Down", "Left", "Right"
        self.food: Coord | None = None
        self.score: int = 0
        self.high_score: int = 0
        self.delay: int = constants.INITIAL_DELAY
        self._high_score_path = (
            high_score_path or os.path.join(os.getcwd(), constants.HIGH_SCORE_FILE)
        )

        self._init_game()

    # ---------------------------------------------------------------------
    # Public API used by the UI and tests
    # ---------------------------------------------------------------------
    def change_direction(self, new_dir: str) -> None:
        """Change snake direction unless it is directly opposite.

        ``new_dir`` must be one of ``"Up"``, ``"Down"``, ``"Left"`` or ``"Right"``.
        The snake cannot reverse onto itself, so a request that would cause an
        immediate 180° turn is ignored.
        """

        opposite = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left",
        }
        if new_dir not in opposite:
            return  # ignore invalid input silently
        if opposite[new_dir] != self.direction:
            self.direction = new_dir

    def step(self) -> bool:
        """Advance the game one tick.

        Returns
        -------
        bool
            ``True`` if the snake is still alive after the move, ``False`` if a
            collision occurred (wall or self). The UI should stop the loop when
            ``False`` is returned.
        """

        head_x, head_y = self.snake[0]
        dx, dy = 0, 0
        if self.direction == "Up":
            dy = -1
        elif self.direction == "Down":
            dy = 1
        elif self.direction == "Left":
            dx = -1
        elif self.direction == "Right":
            dx = 1
        new_head = (head_x + dx, head_y + dy)

        # Wall collision
        if (
            new_head[0] < 0
            or new_head[0] >= self.cols
            or new_head[1] < 0
            or new_head[1] >= self.rows
        ):
            return False

        # Self collision (ignore tail because it moves forward unless we eat)
        if new_head in self.snake:
            return False

        # Insert new head
        self.snake.insert(0, new_head)

        # Food handling
        if self.food and new_head == self.food:
            self.score += 1
            self._maybe_speed_up()
            self._place_food()
            # Do *not* pop tail – snake grows
        else:
            # Normal move – remove tail
            self.snake.pop()

        return True

    def get_delay(self) -> int:
        """Current delay (ms) between moves – useful for UI scheduling."""

        return self.delay

    def get_snake_coords(self) -> List[Coord]:
        """Return a copy of the snake coordinate list."""

        return list(self.snake)

    def get_food_coord(self) -> Coord | None:
        """Return the current food coordinate, or ``None`` if not placed yet."""

        return self.food

    def save_high_score(self) -> None:
        """Write the high score to the persistence file if it exceeds the stored one."""

        if self.score > self.high_score:
            self.high_score = self.score
            try:
                with open(self._high_score_path, "w", encoding="utf-8") as f:
                    f.write(str(self.high_score))
            except OSError:
                # Failure to write should not crash the game – we simply ignore.
                pass

    # ---------------------------------------------------------------------
    # Internal helpers
    # ---------------------------------------------------------------------
    def _init_game(self) -> None:
        """Set up initial snake position, load high score and place first food."""

        # Start near the centre of the grid
        start_x = self.cols // 2
        start_y = self.rows // 2
        self.snake = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
        self.direction = "Right"
        self.score = 0
        self.delay = constants.INITIAL_DELAY
        self._load_high_score()
        self._place_food()

    def _load_high_score(self) -> None:
        try:
            with open(self._high_score_path, "r", encoding="utf-8") as f:
                self.high_score = int(f.read().strip())
        except (OSError, ValueError):
            # File missing or malformed – treat as zero.
            self.high_score = 0

    def _place_food(self) -> None:
        """Randomly locate food on an empty cell."""

        empty_cells = [
            (c, r)
            for c in range(self.cols)
            for r in range(self.rows)
            if (c, r) not in self.snake
        ]
        self.food = random.choice(empty_cells) if empty_cells else None

    def _maybe_speed_up(self) -> None:
        """Decrease the delay after eating food, respecting ``MIN_DELAY``."""

        new_delay = max(self.delay - constants.DELAY_DECREMENT, constants.MIN_DELAY)
        self.delay = new_delay
