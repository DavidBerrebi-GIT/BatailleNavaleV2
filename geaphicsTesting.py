from board import Board
from graphics import Graphics



board = Board()
board.put_random_all_boats()
window= Graphics()
window.draw_board_player(board)