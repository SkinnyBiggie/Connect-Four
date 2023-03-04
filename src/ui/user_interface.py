from src.domain.board import Board
from src.domain.player import Player
from src.domain.computer import Computer
from src.domain.disc import Disc

from src.service.serv_board import ServiceBoard
from src.service.serv_computer import ServiceComputer
from src.validator.validation import Validation

class UI:
    def __init__(self, service_board, service_computer):
        self.__service_board = service_board
        self.__service_computer = service_computer

    def human_vs_computer(self):
        disc1 = Disc('yellow')
        disc2 = Disc('red')

        while True:
            try:
                name = input("Enter your name:")
                Validation.is_name_correct(name)
                break
            except Exception as ex:
                print(ex)

        player1 = Player(name, disc1)
        comp = Computer(disc2, disc1, 4)

        board = Board()

        print(player1)
        print(comp)
        print(board)

        while self.__service_board.draw(board) is False:
            column1 = input(player1.get_name + " choose the column to place your disc")

            while Validation.is_column_valid(column1) is False:
                column1 = input("Invalid column, please choose one between 1 and 7:")

            column1 = int(column1)
            column1 -= 1

            while self.__service_board.place_disc(board, player1.get_disc, column1) is False:
                column1 = input("That column is full, please choose another one:")

                while Validation.is_column_valid(column1) is False:
                    column1 = input("Invalid column, please choose one between 1 and 7:")

                column1 = int(column1)
                column1 -= 1
            print(board)


            if self.__service_board.did_someone_win(board) is False:
                print("Please wait for the computer to place a disc.")
                column2 = int(self.__service_computer.best_placement(comp, board))

                print("The computer chose column number {}".format(str(column2 + 1)))
                self.__service_board.place_disc(board, comp.get_disc, column2)

                print(board)

                if self.__service_board.did_someone_win(board) is True:
                    print("The computer is the winner!")
                    break
                continue

            print("{} is the winner!".format(player1.get_name))
            break

        if self.__service_board.draw(board) is True:
            print("It's a draw!")

    def human_vs_human(self):
        disc1 = Disc("yellow")
        disc2 = Disc("red")

        while True:
            try:
                name1 = input("First player's name:")
                Validation.is_name_correct(name1)
                break
            except Exception as ex:
                print(ex)

        while True:
            try:
                name2 = input("First player's name:")
                Validation.is_name_correct(name2)
                break
            except Exception as ex:
                print(ex)

        player1 = Player(name1, disc1)
        player2 = Player(name2, disc2)

        board = Board()

        print(player1)
        print(player2)
        print(board)

        while self.__service_board.draw(board) is False:
            column1 = input("{}, choose the column:".format(player1.get_name))

            while Validation.is_column_valid(column1) is False:
                column1 = input("Invalid column, please choose one between 1 and 7:")

            column1 = int(column1)
            column1 -= 1

            while self.__service_board.place_disc(board, player1.get_disc, column1) is False:
                column1 = input("That column is full, please choose another one:")

                while Validation.is_column_valid(column1) is False:
                    column1 = input("Invalid column, please choose one between 1 and 7:")

                column1 = int(column1)
                column1 -= 1

            print(board)

            if self.__service_board.did_someone_win(board) is False:
                column2 = input("{}, choose the column:".format(player2.get_name))

                while Validation.is_column_valid(column2) is False:
                    column2 = input("Invalid column, please choose one between 1 and 7:")

                column2 = int(column2)
                column2 -= 1

                while self.__service_board.place_disc(board, player2.get_disc, column2) is False:
                    column2 = input("That column is full, please choose another one:")

                    while Validation.is_column_valid(column2) is False:
                        column2 = input("Invalid column, please choose one between 1 and 7:")

                    column2 = int(column2)
                    column2 -= 1


                print(board)

                if self.__service_board.did_someone_win(board) is True:
                    print("{} is the winner!".format(player2.get_name))
                    break
                continue

            print("{} is the winner!".format(player1.get_name))
            break

        if self.__service_board.draw(board) is True:
            print("It's a draw!")

    @staticmethod
    def gamemode():
        print("\nGamemodes:")
        print("1. 1P vs COM")
        print("2. 1P vs 2P")
        print("3. Quit")

    def game_menu(self):
        while True:
            self.gamemode()
            choice = input("Choose a gamemode:")
            if choice == "1":
                self.human_vs_computer()
            elif choice == "2":
                self.human_vs_human()
            elif choice == "3":
                print("Quitting the game...")
                return
            else:
                print("Invalid choice. Please choose one of the available options")

