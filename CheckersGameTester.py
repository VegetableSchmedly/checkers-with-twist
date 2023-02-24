# Author: Eric Daly
# GitHub username: VegetableSchmedly
# Date:2/24/2023
# Description:


class OutofTurn(Exception):
    """Raised if a player tries to move when its not their turn."""
    pass

class InvalidSquare(Exception):
    """Raised if the player does not own the checker present in the square, or if the square doesnt exist."""
    pass

class InvalidPlayer(Exception):
    """Raised if the player name is invalid"""
    pass


class Board:
    """Represents a game board for checkers"""

    def __init__(self):
        """Initializes data members"""


class Player:
    """Represents a player in a checkers game."""

    def __init__(self, name, color):
        """Initializes data members"""
        self._name = name
        self._color = color         # "Black" or "White"
        self._kings = []
        self._triple_kings = []
        self._captured_pieces = []

    def get_king_count(self):
        """returns the number of king pieces the player has."""
        count = 0
        for king in self._kings:
            count += 1
        return count

    def get_triple_king_count(self):
        """Returns the number of triple king pieces the player has."""
        count = 0
        for king in self._triple_kings:
            count += 1
        return count

    def get_captured_pieces_count(self):
        """Returns the number of triple king pieces the player has."""
        count = 0
        for piece in self._captured_pieces:
            count += 1
        return count


class Checkers:
    """Represents a game of checkers."""

    def __init__(self):
        """Initializes data members"""
        self._rows = 10
        self._columns = 10
        self._players = []



    def create_player(self, player_name, piece_color):
        """Create a player for the game of checkers"""
        return Player(player_name, piece_color)


    def play_game(self, player_name, starting_square_location, destination_square_location):
        """Represents a move in a game of checkers."""


    def game_winner(self):
        """Returns the name of the player who won the game. Or "Game has not ended." if applicable."""


