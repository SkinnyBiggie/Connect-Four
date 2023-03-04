import unittest
from termcolor import colored

from src.domain.board import Board
from src.domain.computer import Computer
from src.domain.player import Player
from src.domain.disc import Disc

from src.service.serv_board import ServiceBoard
from src.service.serv_computer import ServiceComputer

class TestDisc(unittest.TestCase):
    """
    Disc domain test class
    """
    def test_disc(self):
        disc1 = Disc("yellow")
        disc2 = Disc("red")
        self.assertEqual(disc1.color, "yellow")
        self.assertEqual(disc2.color, "red")
        self.assertEqual(str(disc1), colored('#', "yellow"))
        self.assertEqual(str(disc2), colored('#', "red"))

class TestBoard(unittest.TestCase):
    def test_board(self):
        """
        Board domain and service test class
        """
        disc1 = Disc("yellow")
        disc2 = Disc("red")
        board = Board()
        board_service = ServiceBoard()
        self.assertEqual(board.matrix[0][1], '#')
        self.assertEqual(str(board), ' | 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n'
                                     ' - - - - - - - - - - - - - - -\n'
                                     ' | # | # | # | # | # | # | # | \n'
                                     ' - - - - - - - - - - - - - - -\n'
                                     ' | # | # | # | # | # | # | # | \n'
                                     ' - - - - - - - - - - - - - - -\n'
                                     ' | # | # | # | # | # | # | # | \n'
                                     ' - - - - - - - - - - - - - - -\n'
                                     ' | # | # | # | # | # | # | # | \n'
                                     ' - - - - - - - - - - - - - - -\n'
                                     ' | # | # | # | # | # | # | # | \n'
                                     ' - - - - - - - - - - - - - - -\n'
                                     ' | # | # | # | # | # | # | # | \n'
                                     ' - - - - - - - - - - - - - - -\n')
        board_service.place_disc(board, disc1, 1)
        board_service.place_disc(board, disc2, 2)
        self.assertEqual(board_service.did_someone_win(board), False)
        board_service.place_disc(board, disc1, 1)
        board_service.place_disc(board, disc2, 3)
        self.assertEqual(board_service.did_someone_win(board), False)
        board_service.place_disc(board, disc1, 1)
        board_service.place_disc(board, disc2, 4)
        self.assertEqual(board_service.did_someone_win(board), False)
        board_service.place_disc(board, disc1, 1)
        self.assertEqual(board_service.did_someone_win(board), True)

        board2 = Board()
        board_service.place_disc(board2, disc1, 1)
        board_service.place_disc(board2, disc2, 1)
        board_service.place_disc(board2, disc1, 2)
        board_service.place_disc(board2, disc2, 2)
        board_service.place_disc(board2, disc1, 3)
        board_service.place_disc(board2, disc2, 1)
        board_service.place_disc(board2, disc1, 4)
        self.assertEqual(board_service.did_someone_win(board2), True)

        board3 = Board()
        board_service.place_disc(board3, disc1, 1)
        board_service.place_disc(board3, disc2, 2)
        board_service.place_disc(board3, disc1, 2)
        board_service.place_disc(board3, disc2, 3)
        board_service.place_disc(board3, disc2, 3)
        board_service.place_disc(board3, disc1, 3)
        board_service.place_disc(board3, disc2, 4)
        board_service.place_disc(board3, disc2, 4)
        board_service.place_disc(board3, disc2, 4)
        board_service.place_disc(board3, disc1, 4)
        self.assertEqual(board_service.did_someone_win(board3), True)

        board4 = Board()
        board_service.place_disc(board4, disc2, 1)
        board_service.place_disc(board4, disc2, 1)
        board_service.place_disc(board4, disc2, 1)
        board_service.place_disc(board4, disc1, 1)
        board_service.place_disc(board4, disc2, 2)
        board_service.place_disc(board4, disc2, 2)
        board_service.place_disc(board4, disc1, 2)
        board_service.place_disc(board4, disc2, 3)
        board_service.place_disc(board4, disc1, 3)
        board_service.place_disc(board4, disc1, 4)
        self.assertEqual(board_service.did_someone_win(board4), True)


        board5 = Board()
        board_service.place_disc(board5, disc1, 0)
        self.assertEqual(board_service.draw(board5), False)
        board_service.place_disc(board5, disc2, 0)
        board_service.place_disc(board5, disc1, 0)
        board_service.place_disc(board5, disc1, 0)
        board_service.place_disc(board5, disc2, 0)
        board_service.place_disc(board5, disc1, 0)

        board_service.place_disc(board5, disc2, 1)
        board_service.place_disc(board5, disc1, 1)
        board_service.place_disc(board5, disc2, 1)
        board_service.place_disc(board5, disc2, 1)
        board_service.place_disc(board5, disc1, 1)
        board_service.place_disc(board5, disc1, 1)

        board_service.place_disc(board5, disc1, 2)
        board_service.place_disc(board5, disc2, 2)
        board_service.place_disc(board5, disc1, 2)
        board_service.place_disc(board5, disc1, 2)
        board_service.place_disc(board5, disc2, 2)
        board_service.place_disc(board5, disc2, 2)

        board_service.place_disc(board5, disc2, 3)
        board_service.place_disc(board5, disc1, 3)
        board_service.place_disc(board5, disc2, 3)
        board_service.place_disc(board5, disc2, 3)
        board_service.place_disc(board5, disc1, 3)
        board_service.place_disc(board5, disc2, 3)

        board_service.place_disc(board5, disc1, 4)
        board_service.place_disc(board5, disc2, 4)
        board_service.place_disc(board5, disc1, 4)
        board_service.place_disc(board5, disc1, 4)
        board_service.place_disc(board5, disc2, 4)
        board_service.place_disc(board5, disc1, 4)

        board_service.place_disc(board5, disc2, 5)
        board_service.place_disc(board5, disc1, 5)
        board_service.place_disc(board5, disc2, 5)
        board_service.place_disc(board5, disc2, 5)
        board_service.place_disc(board5, disc1, 5)
        board_service.place_disc(board5, disc1, 5)

        board_service.place_disc(board5, disc1, 6)
        board_service.place_disc(board5, disc2, 6)
        board_service.place_disc(board5, disc1, 6)
        board_service.place_disc(board5, disc1, 6)
        board_service.place_disc(board5, disc2, 6)
        board_service.place_disc(board5, disc2, 6)

        self.assertEqual(board_service.draw(board5), True)

        self.assertEqual(board_service.place_disc(board5, disc1, 6), False)

class TestPlayer(unittest.TestCase):
    """
    Player domain test class
    """
    def test_player(self):
        player1 = Player("Dorian", colored('#', 'yellow'))
        player2 = Player("Alex", colored('#', 'red'))
        self.assertEqual(player1.get_name, 'Dorian')
        self.assertEqual(player2.get_disc, colored('#', 'red'))
        self.assertEqual(str(player1), "Player Dorian is using {} discs.".format(colored('#', 'yellow')))


class TestComputer(unittest.TestCase):
    """
    Computer domain and service test class
    """
    def test_computer(self):
        disc1 = Disc('yellow')
        disc2 = Disc('red')
        player1 = Player("Dorian", disc1)
        player2 = Computer(disc2, player1.get_disc, 2)
        self.assertEqual(str(player2), "The computer is using {} discs".format(disc2))
        board = Board()
        board_service = ServiceBoard()
        computer_service = ServiceComputer()
        board_service.place_disc(board, disc1, 0)
        board_service.place_disc(board, disc2, 1)
        board_service.place_disc(board, disc1, 1)
        board_service.place_disc(board, disc2, 2)
        board_service.place_disc(board, disc2, 2)
        board_service.place_disc(board, disc1, 2)
        board_service.place_disc(board, disc2, 2)
        board_service.place_disc(board, disc1, 2)
        board_service.place_disc(board, disc2, 2)
        self.assertEqual(player2.get_disc, disc2)
        self.assertEqual(computer_service.is_move_allowed(board, 3), True)
        self.assertEqual(computer_service.is_move_allowed(board, 2), False)

        board2 = computer_service.simulate_placement(board, 1, player2.get_disc)
        self.assertEqual(board2.matrix[0][2], disc2)
        self.assertEqual(computer_service.find_vertical_connection(4, 2, board, 2, disc2), 1)
        self.assertEqual(computer_service.find_vertical_connection(4, 2, board, 3, disc2), 0)
        self.assertEqual(computer_service.find_vertical_connection(5, 2, board, 2, disc2), 0)
        self.assertEqual(computer_service.find_horizontal_connection(5, 1, board, 2, disc2), 1)
        self.assertEqual(computer_service.find_horizontal_connection(5, 2, board, 2, disc2), 0)
        self.assertEqual(computer_service.find_horizontal_connection(5, 1, board, 4, disc2), 0)
        self.assertEqual(computer_service.find_diagonal_connection(5, 0, board, 3, disc1), 1)
        self.assertEqual(computer_service.find_diagonal_connection(5, 0, board, 4, disc1), 0)
        self.assertEqual(computer_service.find_diagonal_connection(4, 1, board, 3, disc1), 0)
        self.assertEqual(computer_service.find_diagonal_connection(5, 0, board, 2, disc1), 1)

        board_service.place_disc(board, disc2, 3)
        self.assertEqual(computer_service.find_diagonal_connection(4, 2, board, 2, disc2), 1)
        self.assertEqual(computer_service.find_diagonal_connection(5, 3, board, 2, disc2), 0)
        self.assertEqual(computer_service.find_diagonal_connection(4, 2, board, 3, disc2), 0)
        self.assertEqual(computer_service.check_for_connect(board, disc1, 2), 2)
        self.assertEqual(computer_service.check_for_connect(board, disc2, 3), 1)
        self.assertEqual(computer_service.check_for_connect(board, disc1, 4), 0)
        self.assertEqual(computer_service.check_for_connect(board, disc1, 3), 1)
        self.assertEqual(computer_service.check_for_connect(board, disc2, 2), 5)
        self.assertEqual(computer_service.check_for_connect(board, disc2, 4), 0)
        self.assertEqual(computer_service.value(player2, board, disc2), 3)
        self.assertEqual(computer_service.value(player2, board, disc1), -3)
        self.assertEqual(computer_service.find_score(player2, 2, board, disc1), -3)
        self.assertEqual(computer_service.find_score(player2, 2, board, disc2), 3)
        self.assertEqual(computer_service.best_placement(player2, board), 0)

if __name__ == "__main__":
    unittest.main()