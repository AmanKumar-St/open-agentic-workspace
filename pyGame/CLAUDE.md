# pyGame Snake — Project Context

## Stack
- **Language:** Python 3.x
- **Framework:** pygame
- **Package structure:** `snake_game/` is a proper package — always run as `python -m snake_game` from `./pyGame`
- **Python path:** `python`

## Run Commands
```bash
# Correct way to run (from ./pyGame)
python -m snake_game

# Demo / headless test
python run_demo.py

# Tests
python -m pytest tests/
```

## Project Structure
```
pyGame/
├── snake_game/        # Main package (use relative imports inside)
│   ├── __init__.py
│   ├── game.py
│   └── constants.py
├── tests/             # Test suite
├── run_demo.py        # Headless demo runner
├── high_score.txt     # Persisted high score
└── CLAUDE.md          # This file
```

## Known Issues / Rules
- **Never run `game.py` directly** — it uses relative imports. Always use `python -m snake_game`
- `high_score.txt` is created in the CWD — must run from `pyGame/` root
- pygame display requires a display server; headless testing uses `run_demo.py`

## Skills to Use
- `python-patterns` — Python idioms, type hints, dataclasses
- `python-testing` — pytest patterns, fixtures
- `tdd-workflow` — write failing test first, then implement
- `coding-standards` — clean code, no magic numbers (use constants.py)

## Code Standards
- All constants go in `constants.py` — never hardcode values in game logic
- Type hints on all public functions
- 80%+ test coverage requirement
- PEP 8 style enforced

## Agent Delegation
- Use `python-reviewer` for code review
- Use `build-error-resolver` for import errors
- Use `tdd-guide` for new feature development
