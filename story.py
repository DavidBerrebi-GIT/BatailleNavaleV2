from board import Board
from boat import Boat


board = Board()
board.show()

boat1 = Boat(3, (4,4))
boat2 = Boat(3, (6,3))
board.put_boat(boat1)
board.put_boat(boat2)
board.show()