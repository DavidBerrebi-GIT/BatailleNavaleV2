from board import Board
from boat import Boat

def test_init():
    board = Board()
    assert board != None

def test_put_boat():
    board = Board()
    boat = Boat(5,(3,3))
    board.put_boat(boat)
    assert board.boats == [boat]
    
    for i in range(5):
        assert board.cells[3][3+i] == 0
    