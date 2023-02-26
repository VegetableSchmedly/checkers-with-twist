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

    def get_row(self):
        """Returns the number row it the piece is in"""
        return self._row

    def get_column(self):
        """Get method for the column the piece is in"""
        return self._column

    def get_color(self):
        """Get method for color."""
        return self._color

    def get_type(self):
        """Gets piece type"""
        return self._piece_type

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

    def get_name(self):
        """Get method for name."""
        return self._name

    def get_color(self):
        """Get method for color"""
        return self._color


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
        self._turn = 0


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
        player = Player(player_name, piece_color)
        self._players.append(player)
        # for piece in self._pieces:
        #     if piece_color == piece.get_color():
        #         piece.set_player(player)
        return player

    def play_game(self, player_name, starting_square_location, destination_square_location):
        """Represents a move in a game of checkers."""
        move_info = self.valid_move_check(player_name, starting_square_location, destination_square_location)
        self._turn += 1
        current_row = starting_square_location[0]
        current_column = starting_square_location[1]
        move_row = destination_square_location[0]
        move_column = destination_square_location[1]
        current_player = move_info[1]
        current_piece = move_info[0]
        destination_status = None
        for piece in self._pieces:
            if piece.get_location == destination_square_location:
                destination_status = piece.get_color()

        # if current_piece.get_type() == 'normal':
        #     if current_piece.get_color() == 'Black':
        #
        #     elif current_piece.get_color() == 'White':

    def check_potential_jumps(self, color):
        """Checks to see if there are jumps that need to be made prior to any regular moves. Returns True if there is."""
        player_pieces = []
        opponent_pieces = []
        potential_jumps = []
        available_jumps = []
        for piece in self._pieces:
            if piece.get_color == color:
                player_pieces.append(piece)
            else:
                opponent_pieces.append(piece)

        if color == 'Black':            # Working up the board for normal pieces.
            for player_piece in player_pieces:
                for opponent_piece in opponent_pieces:
                    if opponent_piece.get_location() == (player_piece.get_row()+1, player_piece.get_column+1):
                        potential_jumps.append((player_piece.get_row()+2, player_piece.get_row()+2))
                    elif opponent_piece.get_location() == (player_piece.get_row()+1, player_piece.get_column-1):
                        potential_jumps.append((player_piece.get_row()+2, player_piece.get_row()-2))
        if color == 'White':            # Working down the board for normal pieces.
            for player_piece in player_pieces:
                for opponent_piece in opponent_pieces:
                    if opponent_piece.get_location() == (player_piece.get_row()-1, player_piece.get_column+1):
                        potential_jumps.append((player_piece.get_row()-2, player_piece.get_row()+2))
                    elif opponent_piece.get_location() == (player_piece.get_row()-1, player_piece.get_column-1):
                        potential_jumps.append((player_piece.get_row()-2, player_piece.get_row()-2))

        for jump in potential_jumps:
            if jump[0] > 7 or jump[0] < 0:
                continue
            if jump[1] > 7 or jump[1] <0:
                continue
            else:
                for piece in self._pieces:
                    if piece.get_location() == jump:
                        continue
                    else:
                        available_jumps.append(jump)

        if len(available_jumps) > 0:
            return True
        else:
            return False




    def valid_move_check(self, player_name, starting_square_location, destination_square_location):
        """Raises appropriate exception, if there is one."""
        if player_name.color == 'Black' and self._turn % 2 == 1:
            raise OutofTurn
        if player_name.color == 'White' and self._turn % 2 == 0:
            raise OutofTurn

        if starting_square_location[0] > 7 or starting_square_location[0] < 0:
            raise InvalidSquare
        if starting_square_location[1] > 7 or starting_square_location[1] < 0:
            raise InvalidSquare
        if destination_square_location[0] > 7 or destination_square_location[0] < 0:
            raise InvalidSquare
        if destination_square_location[1] > 7 or destination_square_location[1] < 0:
            raise InvalidSquare

        current_player = None
        for player in self._players:
            if player.get_name() == player_name:
                current_player = player
        if current_player is None:
            raise InvalidPlayer

        current_piece = None
        for piece in self._pieces:
            if piece.get_location() == starting_square_location:
                current_piece = piece
        if current_piece.get_color() != current_player.get_color():
            raise InvalidSquare

        else:
            return [current_piece, current_player]


    def get_checker_details(self, square_location):
        """Returns the checker details at the location specified."""
        if square_location[0] > 7 or square_location[0] < 0:
            raise InvalidSquare
        if square_location[1] > 7 or square_location[1] < 0:
            raise InvalidSquare

        for piece in self._pieces:
            if piece.get_location() == square_location:
                if piece.get_color() == 'Black':
                    if piece.get_type() == 'normal':                 # Can be 'normal', 'king', or 'triple_king'
                        return 'Black'
                    elif piece.get_type() == 'king':
                        return 'Black_king'
                    elif piece.get_type() == 'triple_king':
                        return 'Black_Triple_King'
                if piece.get_color() == 'White':
                    if piece.get_type() == 'normal':                 # Can be 'normal', 'king', or 'triple_king'
                        return 'White'
                    elif piece.get_type() == 'king':
                        return 'White_king'
                    elif piece.get_type() == 'triple_king':
                        return 'White_Triple_King'
        else:
            return None

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
game.create_player('Eric', 'Black')
game.create_player('Maggie', 'White')

