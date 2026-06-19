# Snake Game

A minimal, dependency‑free desktop Snake game written in Python using the standard library **Tkinter**.

## Requirements
- Python 3.8+ (Tkinter is bundled with the standard Windows Python distribution)
- No additional packages are needed.

## Installation
1. Clone or copy the repository contents to a folder.
2. Ensure `python` is on your `PATH` and points to a version that includes Tkinter.
   ```
   python --version
   ```
   You should see a version like `Python 3.14.0`.

## Running the Game
There are two ways to run the game:

### 1. Launch the GUI (recommended)
```bash
python -m snake_game
```
This opens an 800 × 800 window with the snake, food, and a score display. Use the arrow keys to move the snake. The game ends on a wall or self‑collision and shows a dialog with your final score and the high score.

### 2. Run a simple console demo (logic only)
```bash
python run_demo.py
```
The script creates a `Game` instance, performs a few steps, and prints the snake coordinates, food location, current score, and delay. It also attempts to read the high‑score file if one exists.

## Game Features
- **Score display** – the current score and the saved high score are shown in the window.
- **Speed increase** – the snake starts with a 150 ms move delay and speeds up by 5 ms each time it eats food (minimum 50 ms).
- **High‑score persistence** – the best score is saved to `high_score.txt` in the game package directory and loaded on subsequent runs.

## Project Structure
```
snake_game/
├─ __init__.py        # package marker
├─ constants.py       # configuration values (window size, cell size, timing, etc.)
├─ game.py            # core game logic (state, movement, collision, persistence)
├─ __main__.py        # Tkinter UI entry point
└─ high_score.txt     # created at runtime when a new high score is achieved

tests/
└─ test_game.py       # unit tests for the core logic (run with `python -m unittest discover`)

run_demo.py            # simple script that runs the core logic without the GUI
```

## Testing
To run the unit tests (requires no GUI), execute:
```bash
python -m unittest discover
```
All tests should pass, confirming that the core `Game` class behaves as expected.

## License
This project is released into the public domain. Feel free to copy, modify, or redistribute.
