# Author: Eric Daly
# GitHub username: VegetableSchmedly
# Date: 2/24/2023
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


class GamePiece:
    """Represents a game piece"""

    def __init__(self, row, column, color, piece_type='normal'):
        self._row = row
        self._column = column
        self._color = color
        self._piece_type = piece_type                   # Can be 'normal', 'king', or 'triple_king'

    def promote_piece(self):
        if self._piece_type == 'normal':
            self._piece_type = 'king'
        elif self._piece_type == 'king':
            self._piece_type = 'triple_king'

    def get_location(self):
        """Returns the tuple for row,column of current square."""
        return (self._row, self._column)

    def get_color(self):
        """Get method for color."""
        return self._color


class Player:
    """Represents a player in a checkers game."""

    def __init__(self, name, color):
        """Initializes data members"""
        self._name = name
        self._color = color                              # "Black" or "White"
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
        self._players = []
        self._rows = 8
        self._columns = 8
        self._squares = []
        self._pieces = []
        self.fill_board()


    def fill_board(self):
        """fills the list of squares with the appropriate tuples, then the appropriate pieces."""
        for row in range(0, 8):
            for column in range(0, 8):
                self._squares.append((row, column))

        for square in self._squares:
            if square[0] == 0 or square[0] == 2:
                if square[1] % 2 != 0:
                    self._pieces.append(GamePiece(square[0], square[1], 'White'))
            if square[0] == 1:
                if square[1] % 2 == 0:
                    self._pieces.append(GamePiece(square[0], square[1], 'White'))
            if square[0] == 5 or square[0] == 7:
                if square[1] % 2 == 0:
                    self._pieces.append(GamePiece(square[0], square[1], 'Black'))
            if square[0] == 6:
                if square[1] % 2 != 0:
                    self._pieces.append(GamePiece(square[0], square[1], 'Black'))

    def create_player(self, player_name, piece_color):
        """Create a player for the game of checkers"""
        self._players.append(Player(player_name, piece_color))

    def play_game(self, player_name, starting_square_location, destination_square_location):
        """Represents a move in a game of checkers."""

    def get_checker_details(self, square_location):
        """Returns the checker details at the location specified."""

    def print_board(self):
        """Prints the gameboard in a readable array, row by row."""
        for row in range(0,8):
            row_status = []
            for square in self._squares:
                color = None
                if square[0] == row:
                    for piece in self._pieces:
                        if piece.get_location() == square:
                            color = piece.get_color()
                    if color:
                        row_status.append(color)
                    else:
                        row_status.append(None)
            print(row_status)






    def game_winner(self):
        """Returns the name of the player who won the game. Or "Game has not ended." if applicable."""


game = Checkers()
game.print_board()
