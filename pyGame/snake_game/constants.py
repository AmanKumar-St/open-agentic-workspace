"""Configuration constants for the Snake game.

All values are chosen to match the specifications:
- 800 × 800 px window
- 20 px grid cells → 40 × 40 logical cells
- Initial speed 150 ms per move, decreasing by 5 ms each food (min 50 ms)
- High‑score persisted to a simple text file in the package directory.
"""

# Window & grid
WINDOW_SIZE = 800  # pixels (square window)
CELL_SIZE = 20     # size of one grid cell in pixels
GRID_CELLS = WINDOW_SIZE // CELL_SIZE  # 40 cells per side

# Timing (ms between moves)
INITIAL_DELAY = 150
DELAY_DECREMENT = 5
MIN_DELAY = 50

# Persistence
HIGH_SCORE_FILE = "high_score.txt"
