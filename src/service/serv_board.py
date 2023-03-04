from src.domain.board import Board

class ServiceBoard:
    """
    Class for the board service
    """

    def did_someone_win(self, board):
        """
        Function to check if the player or the computer won the game
        :param board:
        :return: True if one of them won, otherwise False
        """

        "Vertically"
        for column in range(7):
            for row in range(3):
                if board.matrix[row][column] != '#':
                    if board.matrix[row][column] == board.matrix[row + 1][column]:
                        if board.matrix[row][column] == board.matrix[row + 2][column]:
                            if board.matrix[row][column] == board.matrix[row + 3][column]:
                                return True

        "Horizontally"
        for row in range(6):
            for column in range(4):
                if board.matrix[row][column] != '#':
                    if board.matrix[row][column] == board.matrix[row][column + 1]:
                        if board.matrix[row][column] == board.matrix[row][column + 2]:
                            if board.matrix[row][column] == board.matrix[row][column + 3]:
                                return True


        "Positive slope (upwards)"
        for row in range(3):
            column = 6
            while column >= 3:
                if board.matrix[row][column] != "#":
                    if board.matrix[row][column] == board.matrix[row + 1][column - 1]:
                        if board.matrix[row][column] == board.matrix[row + 2][column - 2]:
                            if board.matrix[row][column] == board.matrix[row + 3][column - 3]:
                                return True
                column -= 1

        "Negative slope (downwards)"
        for row in range(3):
            for column in range(4):
                if board.matrix[row][column] != '#':
                    if board.matrix[row][column] == board.matrix[row + 1][column + 1]:
                        if board.matrix[row][column] == board.matrix[row + 2][column + 2]:
                            if board.matrix[row][column] == board.matrix[row + 3][column + 3]:
                                return True

        return False

    def draw(self, board):
        """
        Check if the game ended in a draw
        :return: True if it ended in a draw, false otherwise
        """
        for row in range(6):
            for column in range(7):
                if board.matrix[row][column] == "#":
                    return False
        return True


    def place_disc(self, board, disc, column):
        """
        Function to place discs on the board
        :param board: Current state of the board
        :param disc: Color of the disc
        :param column: Column where the disc will be placed
        :return: True if we can place a disc on that column, false otherwise
        """
        row = 5
        while row > -1:
            if board.matrix[row][column] == '#':
                board.matrix[row][column] = disc
                return True
            row -= 1
        return False
