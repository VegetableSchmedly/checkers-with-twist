# Author: Eric Daly
# GitHub username: VegetableSchmedly
# Date:2/24/2023
# Description:
import CheckersGame
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

    def setUp(self):
        """Sets up the board for all of the tests."""
        self.game = check.Checkers()
        self.game.create_player('Eric', 'Black')
        self.game.create_player('Maggie', 'White')
        self.game.play_game('Eric', (5, 0), (4, 1))
        self.game.play_game('Maggie', (2, 1), (3, 2))
        self.game.play_game('Eric', (5, 2), (4, 3))
        self.game.play_game('Maggie', (2, 3), (3, 4))
        self.game.play_game('Eric', (4, 1), (2, 3))
        self.game.play_game('Maggie', (3, 4), (4, 5))
        self.game.play_game('Eric', (5, 6), (4, 7))
        self.game.play_game('Maggie', (1, 2), (3, 4))
        self.game.play_game('Maggie', (3, 4), (5, 2))
        self.game.play_game('Eric', (6, 1), (5, 0))
        self.game.play_game('Maggie', (1, 0), (2, 1))
        self.game.play_game('Eric', (7, 0), (6, 1))
        self.game.play_game('Maggie', (5, 2), (7, 0))
        self.game.play_game('Eric', (6, 3), (5, 2))
        self.game.play_game('Maggie', (7, 0), (3, 4))

    def test_1_Player(self):
        """Tests get methods for king, triple_king, and captured pieces counts."""
        player_1 = self.game._players[0]
        player_2 = self.game._players[1]
        self.assertEqual(1, player_2.get_king_count())
        self.assertEqual(0, player_1.get_king_count())
        self.game.play_game('Eric', (4, 7), (3, 6))
        self.game.play_game('Maggie', (3, 4), (4, 3))
        self.game.play_game('Eric', (7, 2), (6, 1))
        self.assertEqual(4, player_2.get_captured_pieces_count())
        self.game.play_game('Maggie', (4, 3), (7, 0))
        self.assertEqual(5, player_2.get_captured_pieces_count())
        self.game.play_game('Eric', (5,0), (4,1))
        self.game.play_game('Maggie', (1, 4), (2, 3))
        self.assertEqual(1, player_1.get_captured_pieces_count())
        self.game.play_game('Eric', (3,6), (1,4))
        self.assertEqual(2, player_1.get_captured_pieces_count())
        self.game.play_game('Maggie', (0, 3), (1, 2))
        self.game.play_game('Eric', (1,4), (0,3))
        self.assertEqual(1, player_1.get_king_count())
        self.game.play_game('Maggie', (1, 6), (2, 5))
        self.game.play_game('Eric', (4,1), (3,2))
        self.game.play_game('Maggie', (0, 7), (1, 6))
        self.game.play_game('Eric', (3,2), (1,0))
        self.game.play_game('Maggie', (7, 0), (6, 1))
        self.game.play_game('Eric', (5,4), (4,3))
        self.assertEqual(0, player_2.get_triple_king_count())
        self.game.play_game('Maggie', (6, 1), (0, 7))
        self.assertEqual(1, player_2.get_triple_king_count())


class TestCheckers(unittest.TestCase):
    """Contains tests for the Checkers class."""

    def setUp(self):
        """Sets up the board for all of the tests."""
        self.game = check.Checkers()
        self.game.create_player('Eric', 'Black')
        self.game.create_player('Maggie', 'White')
        self.game.play_game('Eric', (5, 0), (4, 1))
        self.game.play_game('Maggie', (2, 1), (3, 2))
        self.game.play_game('Eric', (5, 2), (4, 3))
        self.game.play_game('Maggie', (2, 3), (3, 4))
        self.game.play_game('Eric', (4, 1), (2, 3))
        self.game.play_game('Maggie', (3, 4), (4, 5))
        self.game.play_game('Eric', (5, 6), (4, 7))
        self.game.play_game('Maggie', (1, 2), (3, 4))
        self.game.play_game('Maggie', (3, 4), (5, 2))
        self.game.play_game('Eric', (6, 1), (5, 0))
        self.game.play_game('Maggie', (1, 0), (2, 1))
        self.game.play_game('Eric', (7, 0), (6, 1))
        self.game.play_game('Maggie', (5, 2), (7, 0))
        self.game.play_game('Eric', (6, 3), (5, 2))
        self.game.play_game('Maggie', (7, 0), (3, 4))

    def test_1_Checkers(self):
        """Tests all mandatory Exceptions"""
        with self.assertRaises(CheckersGame.InvalidPlayer):
             self.game.play_game('Schmed', (4,7), (3,6))

        with self.assertRaises(CheckersGame.InvalidSquare):     # Test using wrong color piece
            self.game.play_game('Eric', (3,4), (2,3))

        with self.assertRaises(CheckersGame.InvalidSquare):     # Tests moving off board into negative
            self.game.play_game('Eric', (5,0), (4,-1))

        with self.assertRaises(CheckersGame.InvalidSquare):     # Tests moving off board to 8
            self.game.play_game('Eric', (6,7), (7,8))

        with self.assertRaises(CheckersGame.OutofTurn):
            self.game.play_game('Maggie', (3,4), (4,3))

    def test_2_Checkers(self):
        """Tests create player"""
        player_1 = self.game.create_player('Schmed', 'White')
        self.assertIn(player_1, self.game._players)

    def test_3_Checkers(self):
        """Tests play game and normal moves, including a single and double jump"""
        player_1 = self.game._players[0]
        player_2 = self.game._players[1]
        self.assertEqual(1, player_2.get_king_count())
        self.assertEqual(0, player_1.get_king_count())
        self.game.play_game('Eric', (4, 7), (3, 6))
        self.game.play_game('Maggie', (3, 4), (4, 3))
        self.game.play_game('Eric', (7, 2), (6, 1))
        self.assertEqual(4, player_2.get_captured_pieces_count())
        self.game.play_game('Maggie', (4, 3), (7, 0))
        self.assertEqual(5, player_2.get_captured_pieces_count())
        self.game.play_game('Eric', (5,0), (4,1))
        self.game.play_game('Maggie', (1, 4), (2, 3))
        self.game.play_game('Eric', (4,1), (3,2))
        self.game.play_game('Maggie', (7, 0), (6, 1))
        self.game.play_game('Eric', (6,5), (5,6))
        self.game.play_game('Maggie', (2, 1), (4, 3))
        self.game.play_game('Maggie', (4, 3), (6, 5))
        self.assertEqual(7, player_2.get_captured_pieces_count())


    def test_4_Checkers(self):
        """Tests promotion check for the ending of a jump, and a regular move. For each color.
        Checks for captured pieces."""
        player_1 = self.game._players[0]
        player_2 = self.game._players[1]
        self.assertEqual(1, player_2.get_king_count())
        self.assertEqual(0, player_1.get_king_count())
        self.game.play_game('Eric', (5, 0), (4, 1))
        self.game.play_game('Maggie', (2, 1), (3, 2))
        self.game.play_game('Eric', (7, 4), (6, 3))
        self.game.play_game('Maggie', (2, 7), (3, 6))
        self.game.play_game('Eric', (7, 2), (6, 1))
        self.game.play_game('Maggie', (1, 6), (2, 7))
        self.game.play_game('Eric', (5,4), (4, 3))
        self.game.play_game('Maggie', (0, 5), (1, 6))
        self.game.play_game('Eric', (4,1), (2, 3))
        self.game.play_game('Eric', (2,3), (0, 5))
        self.assertEqual(1, player_1.get_king_count())
        self.game.play_game('Maggie', (4, 5), (5, 4))
        self.game.play_game('Eric', (6,1), (5, 0))
        self.game.play_game('Maggie', (5, 4), (7, 2))
        self.assertEqual(2, player_2.get_king_count())


    def test_5_Checkers(self):
        """Tests moves and single and multi jumps for a king, a triple jump that goes both directions"""
        player_1 = self.game._players[0]
        player_2 = self.game._players[1]
        self.assertEqual(1, player_2.get_king_count())
        self.assertEqual(0, player_1.get_king_count())
        self.game.play_game('Eric', (4, 7), (3, 6))
        self.game.play_game('Maggie', (3, 4), (4, 3))
        self.game.play_game('Eric', (7, 2), (6, 1))
        self.game.play_game('Maggie', (4, 3), (7, 0))
        self.game.play_game('Eric', (5,0), (4,1))
        self.game.play_game('Maggie', (1, 4), (2, 3))
        self.game.play_game('Eric', (3,6), (1,4))
        self.game.play_game('Maggie', (0, 3), (1, 2))
        self.game.play_game('Eric', (1,4), (0,3))
        self.game.play_game('Maggie', (1, 6), (2, 5))
        self.game.play_game('Eric', (4,1), (3,2))
        self.game.play_game('Maggie', (0, 7), (1, 6))
        self.game.play_game('Eric', (3,2), (1,0))
        self.game.play_game('Maggie', (7, 0), (6, 1))
        self.game.play_game('Eric', (5,4), (4,3))
        self.game.play_game('Maggie', (6, 1), (0, 7))
        self.game.play_game('Eric', (6,5), (5,4))
        self.assertEqual(6, player_2.get_captured_pieces_count())
        self.game.play_game('Maggie', (0, 7), (3, 4))               # Moving over friendly pieces.
        self.assertEqual(6, player_2.get_captured_pieces_count())
        self.game.play_game('Eric', (7,4), (6,3))
        self.game.play_game('Maggie', (2, 3), (3, 2))
        self.game.play_game('Eric', (6,3), (5,4))
        self.game.play_game('Maggie', (2, 5), (3, 4))
        self.assertEqual(3, player_1.get_captured_pieces_count())
        self.game.play_game('Eric', (0,3), (2,1))
        self.game.play_game('Eric', (2,1), (4,3))
        self.game.play_game('Eric', (4,3), (2,5))
        self.game.play_game('Eric', (2,5), (0,7))
        self.assertEqual(7, player_1.get_captured_pieces_count())       # Quad Jump in both directions with KING



    def test_6_Checkers(self):
        """Tests moves a triple_king. Includes jumping over own piece and jumping 2 pieces at once."""
        player_1 = self.game._players[0]
        player_2 = self.game._players[1]
        self.assertEqual(1, player_2.get_king_count())
        self.assertEqual(0, player_1.get_king_count())
        self.game.play_game('Eric', (4, 7), (3, 6))
        self.game.play_game('Maggie', (3, 4), (4, 3))
        self.game.play_game('Eric', (7, 2), (6, 1))
        self.game.play_game('Maggie', (4, 3), (7, 0))
        self.game.play_game('Eric', (5,0), (4,1))
        self.game.play_game('Maggie', (1, 4), (2, 3))
        self.game.play_game('Eric', (3,6), (1,4))
        self.game.play_game('Maggie', (0, 3), (1, 2))
        self.game.play_game('Eric', (1,4), (0,3))
        self.game.play_game('Maggie', (1, 6), (2, 5))
        self.game.play_game('Eric', (4,1), (3,2))
        self.game.play_game('Maggie', (0, 7), (1, 6))
        self.game.play_game('Eric', (3,2), (1,0))
        self.game.play_game('Maggie', (7, 0), (6, 1))
        self.game.play_game('Eric', (5,4), (4,3))
        self.game.play_game('Maggie', (6, 1), (0, 7))
        self.game.play_game('Eric', (6,5), (5,4))
        self.assertEqual(6, player_2.get_captured_pieces_count())
        self.game.play_game('Maggie', (0, 7), (3, 4))               # Moving over friendly pieces.
        self.assertEqual(6, player_2.get_captured_pieces_count())
        self.game.play_game('Eric', (5,4), (4,3))
        self.game.play_game('Maggie', (3, 4), (0, 7))               # Moving over friendly pieces.
        self.game.play_game('Eric', (7,4), (6,3))
        self.game.play_game('Maggie', (0, 7), (3, 4))               # Moving over friendly pieces.
        self.game.play_game('Eric', (6,3), (5,2))
        self.game.play_game('Maggie', (3, 4), (7, 0))               # Capturing 2 pieces.
        self.assertEqual(8, player_2.get_captured_pieces_count())

    def test_7_Checkers(self):
        """Tests winning a game by eliminating all opponent's pieces."""
        player_1 = self.game._players[0]
        player_2 = self.game._players[1]
        self.assertEqual(1, player_2.get_king_count())
        self.assertEqual(0, player_1.get_king_count())
        self.game.play_game('Eric', (4, 7), (3, 6))
        self.game.play_game('Maggie', (3, 4), (4, 3))
        self.game.play_game('Eric', (7, 2), (6, 1))
        self.game.play_game('Maggie', (4, 3), (7, 0))
        self.game.play_game('Eric', (5,0), (4,1))
        self.game.play_game('Maggie', (1, 4), (2, 3))
        self.game.play_game('Eric', (3,6), (1,4))
        self.game.play_game('Maggie', (0, 3), (1, 2))
        self.game.play_game('Eric', (1,4), (0,3))
        self.game.play_game('Maggie', (1, 6), (2, 5))
        self.game.play_game('Eric', (4,1), (3,2))
        self.game.play_game('Maggie', (0, 7), (1, 6))
        self.game.play_game('Eric', (3,2), (1,0))
        self.game.play_game('Maggie', (7, 0), (6, 1))
        self.game.play_game('Eric', (5,4), (4,3))
        self.game.play_game('Maggie', (6, 1), (0, 7))
        self.game.play_game('Eric', (6,5), (5,4))
        self.game.play_game('Maggie', (0, 7), (3, 4))               # Moving over friendly pieces.
        self.game.play_game('Eric', (5,4), (4,3))
        self.game.play_game('Maggie', (3, 4), (0, 7))               # Moving over friendly pieces.
        self.game.play_game('Eric', (7,4), (6,3))
        self.game.play_game('Maggie', (0, 7), (3, 4))               # Moving over friendly pieces.
        self.game.play_game('Eric', (6,3), (5,2))
        self.game.play_game('Maggie', (3, 4), (7, 0))               # Capturing 2 pieces.
        self.game.play_game('Eric', (1,0), (2,1))
        self.game.play_game('Maggie', (1, 2), (3, 0))
        self.game.play_game('Eric', (6,7), (5,6))
        self.game.play_game('Maggie', (4, 5), (6, 7))
        self.game.play_game('Eric', (7,6), (6,5))
        self.game.play_game('Maggie', (7, 0), (4, 3))
        self.game.play_game('Eric', (6,5), (5,4))
        self.game.play_game('Maggie', (4, 3), (6, 5))
        self.game.play_game('Eric', (0,3), (1,2))
        self.game.play_game('Maggie', (2, 3), (3, 4))
        self.game.play_game('Eric', (1,2), (2,3))
        self.game.play_game('Maggie', (6, 5), (4, 3))
        self.game.play_game('Eric', (2,3), (3,2))
        self.assertEqual('Game has not ended', self.game.game_winner())
        self.game.play_game('Maggie', (4, 3), (2, 1))
        self.assertEqual('Maggie', self.game.game_winner())             #TODO FIX













if __name__ == '__main__':
    unittest.main()