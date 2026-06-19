"""Unit tests for the Snake game core logic.

These tests exercise the :class:`Game` class without launching a GUI.
"""

import os
import unittest
from pathlib import Path

# Ensure the package is importable
import sys
sys.path.append(str(Path(__file__).parents[1]))  # add project root to sys.path

from snake_game.game import Game
from snake_game import constants


class TestGame(unittest.TestCase):
    def setUp(self):
        # Use a temporary high‑score file to avoid polluting the repo
        self.tmp_file = Path("high_score_test.txt")
        # Ensure it's removed before each test
        if self.tmp_file.exists():
            self.tmp_file.unlink()
        self.game = Game(high_score_path=str(self.tmp_file))

    def tearDown(self):
        if self.tmp_file.exists():
            self.tmp_file.unlink()

    def test_initial_state(self):
        # Verify initial snake length and position
        self.assertEqual(len(self.game.snake), 3)
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.delay, constants.INITIAL_DELAY)
        self.assertIsNotNone(self.game.food)

    def test_change_direction(self):
        # Changing to opposite direction should be ignored
        orig = self.game.direction
        self.game.change_direction("Left")  # opposite of initial Right
        self.assertEqual(self.game.direction, orig)
        # Valid change
        self.game.change_direction("Down")
        self.assertEqual(self.game.direction, "Down")

    def test_eat_food_and_speed_up(self):
        # Place food directly in front of the snake head
        head_x, head_y = self.game.snake[0]
        if self.game.direction == "Right":
            food = (head_x + 1, head_y)
        elif self.game.direction == "Left":
            food = (head_x - 1, head_y)
        elif self.game.direction == "Up":
            food = (head_x, head_y - 1)
        else:
            food = (head_x, head_y + 1)
        self.game.food = food
        # Step – should eat food, grow, increase score and speed up
        alive = self.game.step()
        self.assertTrue(alive)
        self.assertEqual(self.game.score, 1)
        self.assertEqual(len(self.game.snake), 4)  # grew by one
        self.assertLess(self.game.delay, constants.INITIAL_DELAY)

    def test_collision_wall(self):
        # Direct snake towards wall to trigger collision
        self.game.direction = "Up"
        # Move head to top row
        self.game.snake[0] = (self.game.snake[0][0], 0)
        alive = self.game.step()
        self.assertFalse(alive)

    def test_high_score_persistence(self):
        # Simulate a game ending with a score
        self.game.score = 5
        self.game.save_high_score()
        # Reload a new game instance and verify high score loaded
        new_game = Game(high_score_path=str(self.tmp_file))
        self.assertEqual(new_game.high_score, 5)

if __name__ == "__main__":
    unittest.main()
