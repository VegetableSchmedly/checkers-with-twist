# Author: Eric Daly
# GitHub username: VegetableSchmedly
# Date:2/24/2023
# Description:

import CheckersGame as check
import unittest

class TestGamePiece(unittest.TestCase):
    """Contains tests for the GamePiece class."""

    def test_1_GamePiece(self):
        """Test promote_piece"""
        piece_1 = check.GamePiece(1, 1, 'Black')
        self.assertEqual(piece_1.get_type(), 'normal')
        piece_1.promote_piece()
        self.assertEqual(piece_1.get_type(), 'king')
        piece_1.promote_piece()
        self.assertEqual(piece_1.get_type(), 'triple_king')






class TestPlayer(unittest.TestCase):
    """Contains tests for the Player class."""

    def test_1_Player(self):
        """Tests get methods for king, triple_king, and captured pieces counts."""


class TestCheckers(unittest.TestCase):
    """Contains tests for the Checkers class."""

    def test_0_Checkers(self):
        """Tests all mandatory Exceptions"""

    def test_1_Checkers(self):
        """Test fill board and get checker details at creation of game."""

    def test_2_Checkers(self):
        """Tests create player"""

    def test_3_Checkers(self):
        """Tests play game and normal moves, including a single, double, and triple jump for each color"""

    def test_4_Checkers(self):
        """Tests promotion check for the ending of a jump, and a regular move. For each color. Checks for captured pieces."""

    def test_5_Checkers(self):
        """Tests moves and single and double jumps for a king, as well as the promotion to a triple_king"""

    def test_6_Checkers(self):
        """Tests moves and single and double jumps for a triple_king.
        Includes jumping over own piece and jumping 2 pieces at once."""

    def test_7_Checkers(self):
        """Tests winning a game by eliminating all opponent's pieces."""

    def test_8_Checkers(self):
        """Tests winning by blocking in all of opponent's pieces."""












if __name__ == '__main__':
    unittest.main()