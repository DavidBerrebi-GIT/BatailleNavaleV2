from board import Board
from graphics import Graphics



board_player = Board()
board_player.put_random_all_boats()
board_opponent = Board()
board_opponent.put_random_all_boats()

board_player.shoot((0,4))


window= Graphics()
window.draw_board_player(board_player)
window.draw_board_opponnent(board_opponent)
window.root.mainloop()