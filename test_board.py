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
def test_valid_cell():
    board = Board()
    
    for i in range(10):
        for j in range(10):
            assert board._valid_cell((i,j))
    
    
    assert board._valid_cell((-1,5)) == False
    assert board._valid_cell((10,5)) == False
    assert board._valid_cell((5,-1)) == False
    assert board._valid_cell((5,11)) == False
    

def test_hit():
    board = Board()
    boat = Boat(5,(3,3))
    board.put_boat(boat)

    for i in range(1,6):
        board.hit(0)
        assert boat.hp == 5 - i
        assert board.boats[0].hp == 5-i
    assert board.sinked[0] 
