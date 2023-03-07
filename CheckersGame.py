# Author: Eric Daly
# GitHub username: VegetableSchmedly
# Date: 3/1/2023
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
        """Initalizies the GamePiece data members."""
        self._row = row
        self._column = column
        self._color = color
        self._piece_type = piece_type  # Can be 'normal', 'king', or 'triple_king'

    def promote_piece(self):
        """Promotes a piece from normal to king to triple_king."""
        if self._piece_type == 'normal':
            self._piece_type = 'king'
        elif self._piece_type == 'king':
            self._piece_type = 'triple_king'

    def set_row(self, row):
        """Set method for row."""
        self._row = row

    def set_column(self, column):
        """Set method for column"""
        self._column = column

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
        self._pieces = []
        self._color = color  # "Black" or "White"
        self._captured_pieces = []

    def get_king_count(self):
        """returns the number of king pieces the player has."""
        king_count = 0
        for piece in self._pieces:
            if piece.get_type() == 'king':
                king_count += 1
        return king_count

    def get_triple_king_count(self):
        """Returns the number of triple king pieces the player has."""
        triple_king_count = 0
        for piece in self._pieces:
            if piece.get_type() == 'triple_king':
                triple_king_count += 1
        return triple_king_count

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

    def add_piece(self, piece):
        """Adds a piece to the player's collection"""
        self._pieces.append(piece)

    def add_captured_piece(self, piece):
        """Adds a captured piece to the list."""
        self._captured_pieces.append(piece)

    def get_total_pieces(self):
        """Returns a list of all GamePiece objects associated with player."""
        return self._pieces


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
        for piece in self._pieces:
            if piece.get_color() == piece_color:
                player.add_piece(piece)
        return player

    def play_game(self, player_name, starting_square_location, destination_square_location):
        """Represents a move in a game of checkers."""
        move_info = self.valid_move_check(player_name, starting_square_location, destination_square_location)
        current_player = move_info[1]
        current_piece = move_info[0]

        if current_piece.get_type() == 'normal':
            return self.make_normal_move(current_player, current_piece, starting_square_location,
                                         destination_square_location)
        elif current_piece.get_type() == 'king':
            return self.make_king_move(current_player, current_piece, starting_square_location,
                                       destination_square_location)
        elif current_piece.get_type() == 'triple_king':
            return self.make_triple_king_move(current_player, current_piece, starting_square_location,
                                              destination_square_location)

    def make_normal_move(self, player, moving_piece, start, destination):
        """Makes the directed move"""
        capture_count = 0
        current_row = start[0]
        current_column = start[1]
        move_row = destination[0]
        move_column = destination[1]
        moving_piece.set_row(move_row)
        moving_piece.set_column(move_column)
        if abs(move_row - current_row) > 1:  # If 2 row move, a jump was executed.
            if move_column > current_column:
                jump_column = current_column + 1
            else:
                jump_column = current_column - 1
            if move_row > current_row:
                jump_row = current_row + 1
            else:
                jump_row = current_row - 1
            for piece in self._pieces:
                if piece.get_location() == (jump_row, jump_column):
                    self.capture_piece(player, piece)
                    capture_count += 1
                    if self.check_if_end_of_turn(moving_piece, start,
                                                 destination) is True:  # Called since we made a jump.
                        self.promotion_check(moving_piece)
                        self._turn += 1
        else:
            self.promotion_check(moving_piece)
            self._turn += 1
        return capture_count

    def make_king_move(self, player, moving_piece, start, destination):     # TODO: Add king constraints
        """Makes a directed move with the rules of a king."""
        capture_count = 0
        current_row = start[0]
        current_column = start[1]
        move_row = destination[0]
        move_column = destination[1]
        rows_moved = abs(current_row - move_row)
        squares_crossed = []
        moving_piece.set_row(move_row)
        moving_piece.set_column(move_column)
        if move_row - current_row > 1:  # If a 2 row move, a jump was executed DOWN the board
            if move_column - current_column > 1:  # Moving DOWN to RIGHT
                crossed_row = current_row + 1
                crossed_column = current_column + 1
                for square in range(current_row + 1, move_row):
                    squares_crossed.append((crossed_row, crossed_column))
                    crossed_row += 1
                    crossed_column += 1
            else:  # Moving DOWN to LEFT
                crossed_row = current_row + 1
                crossed_column = current_column - 1
                for square in range(current_row + 1, move_row):
                    squares_crossed.append((crossed_row, crossed_column))
                    crossed_row += 1
                    crossed_column -= 1
        elif current_row - move_row > 1:  # If a 2 row move, a jump was executed UP the board
            if move_column - current_column > 1:  # Moving UP to RIGHT
                crossed_row = current_row - 1
                crossed_column = current_column + 1
                for square in range(current_row - 1, move_row, -1):
                    squares_crossed.append((crossed_row, crossed_column))
                    crossed_row -= 1
                    crossed_column += 1
            else:  # Moving UP to LEFT
                crossed_row = current_row - 1
                crossed_column = current_column - 1
                for square in range(current_row - 1, move_row, -1):
                    squares_crossed.append((crossed_row, crossed_column))
                    crossed_row -= 1
                    crossed_column -= 1
        for square in squares_crossed:
            for piece in self._pieces:
                if piece.get_location() == square and piece.get_color() != moving_piece.get_color():
                    self.capture_piece(player, piece)
                    capture_count += 1
                    if rows_moved == 2:  # Check to see if it was a normal jump, therefore able to be a multi-jump
                        if self.check_if_end_of_turn(moving_piece, start,
                                                     destination) is True:  # Called since we made a jump.
                            self.promotion_check(moving_piece)
                            self._turn += 1
        else:
            self.promotion_check(moving_piece)
            self._turn += 1
        return capture_count

    def make_triple_king_move(self, player, moving_piece, start, destination):  # TODO: Add TK constraints
        """Makes a directed move with the rules of a triple king."""
        capture_count = 0
        current_row = start[0]
        current_column = start[1]
        move_row = destination[0]
        move_column = destination[1]
        rows_moved = abs(current_row - move_row)
        squares_crossed = []
        moving_piece.set_row(move_row)
        moving_piece.set_column(move_column)
        if move_row - current_row > 1:  # If a 2 row move, a jump was executed DOWN the board
            if move_column - current_column > 1:  # Moving DOWN to RIGHT
                crossed_row = current_row + 1
                crossed_column = current_column + 1
                for square in range(current_row + 1, move_row):
                    squares_crossed.append((crossed_row, crossed_column))
                    crossed_row += 1
                    crossed_column += 1
            else:  # Moving DOWN to LEFT
                crossed_row = current_row + 1
                crossed_column = current_column - 1
                for square in range(current_row + 1, move_row):
                    squares_crossed.append((crossed_row, crossed_column))
                    crossed_row += 1
                    crossed_column -= 1
        elif current_row - move_row > 1:  # If a 2 row move, a jump was executed UP the board
            if move_column - current_column > 1:  # Moving UP to RIGHT
                crossed_row = current_row - 1
                crossed_column = current_column + 1
                for square in range(current_row - 1, move_row, -1):
                    squares_crossed.append((crossed_row, crossed_column))
                    crossed_row -= 1
                    crossed_column += 1
            else:  # Moving UP to LEFT
                crossed_row = current_row - 1
                crossed_column = current_column - 1
                for square in range(current_row - 1, move_row, -1):
                    squares_crossed.append((crossed_row, crossed_column))
                    crossed_row -= 1
                    crossed_column -= 1
        for square in squares_crossed:
            for piece in self._pieces:
                if piece.get_location() == square and piece.get_color() != moving_piece.get_color():
                    self.capture_piece(player, piece)
                    capture_count += 1
                    if rows_moved == 2:  # Check to see if it was a normal jump, therefore able to be a multi-jump
                        if self.check_if_end_of_turn(moving_piece, start,
                                                     destination) is True:  # Called since we made a jump.
                            self.promotion_check(moving_piece)
                            self._turn += 1
        else:
            self.promotion_check(moving_piece)
            self._turn += 1
        return capture_count

    def promotion_check(self, piece):
        """Check if piece is to be promoted, and promote if applicable."""
        if piece.get_color() == 'Black':
            if piece.get_type() == 'normal' and piece.get_row() == 0:
                piece.promote_piece()
            elif piece.get_type() == 'king' and piece.get_row() == 7:
                piece.promote_piece()

        if piece.get_color() == 'White':
            if piece.get_type() == 'normal' and piece.get_row() == 7:
                piece.promote_piece()
            elif piece.get_type() == 'king' and piece.get_row() == 0:
                piece.promote_piece()

    def capture_piece(self, player, piece):
        """Removes the piece from the board and adds it to the player's captured list."""
        self._pieces.remove(piece)
        player.add_captured_piece(piece)

    def check_if_end_of_turn(self, moving_piece, starting_square, landing_square):
        """Checks if this is the mid-point in a multi-jump move. If it is a mid-point, return False."""
        if moving_piece.get_color() == 'Black':
            if landing_square[0] - starting_square[0] > 0 or moving_piece.get_type() != 'normal':  # Moving down
                potential_right_move = (landing_square[0] + 1, landing_square[1] + 1)
                potential_left_move = (landing_square[0] + 1, landing_square[1] - 1)
                for piece in self._pieces:
                    if piece.get_location() == potential_left_move and piece.get_color() == 'White':
                        if potential_left_move[0] < 7 and potential_left_move[1] > 0:
                            if self.get_checker_details(
                                    (potential_left_move[0] + 1, potential_left_move[1] - 1)) is None:
                                return False
                    if piece.get_location() == potential_right_move and piece.get_color() == 'White':
                        if potential_right_move[0] < 7 and potential_right_move[1] < 7:
                            if self.get_checker_details(
                                    (potential_right_move[0] + 1, potential_right_move[1] + 1)) is None:
                                return False

            if landing_square[0] - starting_square[0] < 0 or moving_piece.get_type() != 'normal':  # Moving up
                potential_right_move = (landing_square[0] - 1, landing_square[1] + 1)
                potential_left_move = (landing_square[0] - 1, landing_square[1] - 1)
                for piece in self._pieces:
                    if piece.get_location() == potential_left_move and piece.get_color() == 'White':
                        if potential_left_move[0] > 0 and potential_left_move[1] > 0:
                            if self.get_checker_details(
                                    (potential_left_move[0] - 1, potential_left_move[1] - 1)) is None:
                                return False
                    if piece.get_location() == potential_right_move and piece.get_color() == 'White':
                        if potential_right_move[0] > 0 and potential_right_move[1] < 7:
                            if self.get_checker_details(
                                    (potential_right_move[0] - 1, potential_right_move[1] + 1)) is None:
                                return False

        elif moving_piece.get_color() == 'White':
            if landing_square[0] - starting_square[0] > 0 or moving_piece.get_type() != 'normal':  # Moving down
                potential_right_move = (landing_square[0] + 1, landing_square[1] + 1)
                potential_left_move = (landing_square[0] + 1, landing_square[1] - 1)
                for piece in self._pieces:
                    if piece.get_location() == potential_left_move and piece.get_color() == 'Black':
                        if potential_left_move[0] < 7 and potential_left_move[1] > 0:
                            if self.get_checker_details(
                                    (potential_left_move[0] + 1, potential_left_move[1] - 1)) is None:
                                return False
                    if piece.get_location() == potential_right_move and piece.get_color() == 'Black':
                        if potential_right_move[0] < 7 and potential_right_move[1] < 7:
                            if self.get_checker_details(
                                    (potential_right_move[0] + 1, potential_right_move[1] + 1)) is None:
                                return False

            if landing_square[0] - starting_square[0] < 0 or moving_piece.get_type() != 'normal':  # Moving up
                potential_right_move = (landing_square[0] - 1, landing_square[1] + 1)
                potential_left_move = (landing_square[0] - 1, landing_square[1] - 1)
                for piece in self._pieces:
                    if piece.get_location() == potential_left_move and piece.get_color() == 'Black':
                        if potential_left_move[0] > 0 and potential_left_move[1] > 0:
                            if self.get_checker_details(
                                    (potential_left_move[0] + 1, potential_left_move[1] - 1)) is None:
                                return False
                    if piece.get_location() == potential_right_move and piece.get_color() == 'Black':
                        if potential_right_move[0] > 0 and potential_right_move[1] < 7:
                            if self.get_checker_details(
                                    (potential_right_move[0] + 1, potential_right_move[1] + 1)) is None:
                                return False
        return True

    def valid_move_check(self, player_name, starting_square_location, destination_square_location):
        """Raises appropriate exception, if there is one. Otherwise returns [piece, player]"""
        current_player = None
        for player in self._players:
            if player.get_name() == player_name:
                current_player = player
        if current_player is None:
            raise InvalidPlayer
        if current_player.get_color() == 'Black' and self._turn % 2 == 1:
            raise OutofTurn
        if current_player.get_color() == 'White' and self._turn % 2 == 0:
            raise OutofTurn

        if starting_square_location[0] > 7 or starting_square_location[0] < 0:
            raise InvalidSquare
        if starting_square_location[1] > 7 or starting_square_location[1] < 0:
            raise InvalidSquare
        if destination_square_location[0] > 7 or destination_square_location[0] < 0:
            raise InvalidSquare
        if destination_square_location[1] > 7 or destination_square_location[1] < 0:
            raise InvalidSquare

        current_piece = None
        for piece in self._pieces:
            if piece.get_location() == starting_square_location:
                current_piece = piece
        if current_piece is None:
            raise InvalidSquare
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
                    if piece.get_type() == 'normal':  # Can be 'normal', 'king', or 'triple_king'
                        return 'Black'
                    elif piece.get_type() == 'king':
                        return 'Black_king'
                    elif piece.get_type() == 'triple_king':
                        return 'Black_Triple_King'
                if piece.get_color() == 'White':
                    if piece.get_type() == 'normal':  # Can be 'normal', 'king', or 'triple_king'
                        return 'White'
                    elif piece.get_type() == 'king':
                        return 'White_king'
                    elif piece.get_type() == 'triple_king':
                        return 'White_Triple_King'
        else:
            return None

    def print_board(self):
        """Prints the gameboard in an array, row by row."""
        game_list = []
        for row in range(0, 8):
            row_list = []
            for column in range(0, 8):
                row_list.append(self.get_checker_details((row, column)))
            game_list.append(row_list)
        print(game_list)

    def print_square_board(self):
        """Prints the gameboard in a readable format."""
        for row in range(0, 8):
            row_list = []
            for column in range(0, 8):
                row_list.append(self.get_checker_details((row, column)))
            print(row_list)
        print('\n')

    def game_winner(self):
        """Returns the name of the player who won the game. Or "Game has not ended." if applicable."""
        player_1 = self._players[0]
        player_2 = self._players[1]
        if len(player_1.get_total_pieces()) == 0:
            return player_2.get_name()
        elif len(player_2.get_total_pieces()) == 0:
            return player_1.get_name()
        return 'Game has not ended'


if __name__ == '__main__':
    game = Checkers()
    game.create_player('Eric', 'Black')
    game.create_player('Maggie', 'White')
    game.play_game('Eric', (5, 0), (4, 1))
    game.play_game('Maggie', (2, 1), (3, 2))
    game.play_game('Eric', (5, 2), (4, 3))
    game.play_game('Maggie', (2, 3), (3, 4))
    game.play_game('Eric', (4, 1), (2, 3))
    game.play_game('Maggie', (3, 4), (4, 5))
    game.play_game('Eric', (5, 6), (4, 7))
    game.play_game('Maggie', (1, 2), (3, 4))
    game.play_game('Maggie', (3, 4), (5, 2))
    game.play_game('Eric', (6, 1), (5, 0))
    game.play_game('Maggie', (1, 0), (2, 1))
    game.play_game('Eric', (7, 0), (6, 1))
    game.play_game('Maggie', (5, 2), (7, 0))
    game.play_game('Eric', (6, 3), (5, 2))
    game.play_game('Maggie', (7, 0), (3, 4))
    game.play_game('Eric', (5, 0), (4, 1))
    game.play_game('Maggie', (0, 1), (1, 0))
    game.play_game('Eric', (4, 1), (3, 2))
    game.play_game('Maggie', (3, 4), (2, 3))
    game.play_game('Eric', (7, 2), (6, 1))
    game.play_game('Maggie', (2, 3), (5, 0))
    game.play_game('Eric', (7, 4), (6, 3))
    game.play_game('Maggie', (5, 0), (7, 2))
    game.play_game('Eric', (6, 7), (5, 6))
    game.play_game('Maggie', (7, 2), (3, 6))
    game.play_game('Eric', (7, 6), (6, 7))
    game.play_game('Maggie', (3, 6), (5, 4))
    game.play_game('Eric', (4,7), (3, 6))
    game.print_square_board()
