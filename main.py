from src.domain.board import Board
from src.domain.player import Player
from src.domain.disc import Disc
from src.domain.computer import Computer

from src.service.serv_board import ServiceBoard
from src.service.serv_computer import ServiceComputer

from src.ui.user_interface import UI

if __name__ == "__main__":
    service_board = ServiceBoard()
    service_comp = ServiceComputer()
    user_interface = UI(service_board, service_comp)
    user_interface.game_menu()