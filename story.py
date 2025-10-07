from board import Board
from boat import Boat


board = Board()
board.show()

boat1 = Boat(3, (4,4))
boat2 = Boat(3, (6,3))
board.put_boat(boat1)
board.put_boat(boat2)



board.shoot((4,4))
board.show()

board.shoot((4,5))
board.shoot((4,6))
board.show()

board.shoot((0,0))
board.show()


