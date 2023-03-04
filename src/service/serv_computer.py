from src.domain.computer import Computer
from src.service.serv_board import ServiceBoard
from src.domain.board import Board

class ServiceComputer:
    """
    Class for the computer service
    """
    def is_move_allowed(self, board, column):
        """
        Function to check whether the move that the computer wants to make is allowed
        :param board: The board
        :param column: the column where it wants to place the disc
        :return: True if the move is allowed, false otherwise
        """
        row = 5
        while row > -1:
            if board.matrix[row][column] == '#':
                return True
            row -= 1

        return False

    def simulate_placement(self, board, column, disc):
        """
        Function that simulates disc placements for the miniMax algorithm
        :param board: The board before the simulated placement
        :param column: the column where the computer wants to place the disc
        :param disc: the disc the computer will place on the board
        :return: a new virtual board where the placement was made
        """
        fake_board = Board()
        for row in range(6):
            for column in range(7):
                fake_board.matrix[row][column] = board.matrix[row][column]
        ServiceBoard().place_disc(fake_board, disc, column)
        return fake_board


    def value(self, computer, board, disc):
        """
        Function to find the value for a configuration of the board using a heuristic
        :param computer: the computer
        :param board: the board
        :param disc: the disc of the player
        :return: the score of a configuration of the board
        """
        if disc == computer.disc:
            opponent_disc = computer.human_disc
        else:
            opponent_disc = computer.disc

        c_fours = self.check_for_connect(board, disc, 4)
        c_threes = self.check_for_connect(board, disc, 3)
        c_twos = self.check_for_connect(board, disc, 2)
        h_fours = self.check_for_connect(board, opponent_disc, 4)
        h_threes = self.check_for_connect(board, opponent_disc, 3)
        h_twos = self.check_for_connect(board, opponent_disc, 2)

        if h_fours > 0:
            return -100000
        else:
            return c_fours*100000 + c_threes*100 + c_twos - h_threes*100 - h_twos


    def find_score(self, computer, depth, board, disc):
        """
        Function to find the score of a move by recursively playing a "fake" board until the computer reaches depth level 0
        :param computer: The computer
        :param depth: The depth of the "game tree" at which the computer simulates moves
        :param board: The board used to find the score of a move
        :param disc: The disc used at a move
        :return: the score of the move calculated using an heuristic

        A heuristic, or heuristic technique, is any approach to problem-solving that uses a practical method or various
        shortcuts in order to produce solutions that may not be optimal but are sufficient given a limited timeframe or deadline.
        """
        allowed_moves = []
        for column in range(7):
            if self.is_move_allowed(board, column):
                fake_board = self.simulate_placement(board, column, disc)
                allowed_moves.append(fake_board)

        if depth == 0 or len(allowed_moves) == 0 or ServiceBoard().did_someone_win(board):
            return self.value(computer, board, disc)

        if disc == computer.disc:
            opponent_disc = computer.human_disc
        else:
            opponent_disc = computer.disc

        score = -99999999

        for move in allowed_moves:
            score = max(score, -self.find_score(computer, depth - 1, move, opponent_disc))

        return score

    def best_placement(self, computer, board):
        """
        Function to check for the best possible placement
        :param computer: The computer
        :param board: The board
        :return: The column number for the best placement
        """
        allowed_moves = {}
        for column in range(7):
            if self.is_move_allowed(board, column) is True:
                fake_board = self.simulate_placement(board, column, computer.disc)
                allowed_moves[column] = -self.find_score(computer, computer.depth - 1, fake_board, computer.human_disc)

        best_score = -99999999
        best_placement = None
        placements = allowed_moves.items()

        for placement, score in placements:
            if score > best_score:
                best_score = score
                best_placement = placement
        return best_placement

    def check_for_connect(self, board, disc, size):
        """
        Function to find out the number of connections of <length> for a certain <board> and player
        :param board: the table
        :param disc: the disc of the player
        :param size: the size of the connection we want to find
        :return: number of possible connections
        """
        counter = 0
        for row in range(6):
            for column in range(7):
                if board.matrix[row][column] == disc:
                    counter += self.find_vertical_connection(row, column, board, size, board.matrix[row][column])
                    counter += self.find_horizontal_connection(row, column, board, size, board.matrix[row][column])
                    counter += self.find_diagonal_connection(row, column, board, size, board.matrix[row][column])

        return counter

    def find_vertical_connection(self, row, column, board, size, disc):
        """
        Function that finds the number of possible vertical connections
        :param row: the row
        :param column: the column
        :param board: the state of the board
        :param size: the size of the connection we want to find
        :param disc: The type of disc we need to find the connections for
        :return: the number of vertical connections found
        """
        counter = 0
        if row + size - 1 < 6:
            for x in range(size):
                if board.matrix[row + x][column] == disc:
                    counter += 1
                else:
                    break

        if counter == size:
            return 1
        else:
            return 0

    def find_horizontal_connection(self, row, column, board, size, disc):
        """
        Function that finds the number of possible horizontal connections
        :param row: the row
        :param column: the column
        :param board: the state of the board
        :param size: the size of the connection we want to find
        :param disc: The type of disc we need to find the connections for
        :return: the number of horizontal connections found
        """
        counter = 0
        if column + size - 1 < 7:
            for x in range(size):
                if disc == board.matrix[row][column + x]:
                    counter += 1
                else:
                    break
        if counter == size:
            return 1
        else:
            return 0

    def find_diagonal_connection(self, row, column, board, size, disc):
        """
        Function that finds the number of possible diagonal connections
        :param row: the row
        :param column: the column
        :param board: the state of the board
        :param size: the size of the connection we want to find
        :param disc: The type of disc we need to find the connections for
        :return: the number of diagonal connections found
        """
        total = 0
        counter = 0
        if column + size - 1 < 7 and row + size - 1 < 6:
            for x in range(size):
                if disc == board.matrix[row + x][column + x]:
                    counter += 1
                else:
                    break

        if counter == size:
            total += 1

        counter = 0
        if column + size - 1 < 7 and row - size + 1 > - 1:
            for x in range(size):
                if disc == board.matrix[row - x][column + x]:
                    counter += 1
                else:
                    break

        if counter == size:
            total += 1
        return total
