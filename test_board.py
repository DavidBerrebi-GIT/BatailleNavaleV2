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
    board.hit(0)
    assert boat.hp == 0
    assert board.boats[0].hp == 0
    assert board.sinked[0]

    assert board.cells[3][2] == -2
    assert board.cells[3][8] == -2

    for i in range(2,9):
        assert board.cells[2][i] == -2
        assert board.cells[4][i] == -2


def test_shoot():
    board = Board()
    boat = Boat(2,(0,0))
    board.put_boat(boat)

    board.shoot((0,0))
    assert board.cells[0][0] == -4
    assert boat.hp == 1

    board.shoot((0,1))
    assert board.cells[0][1] == -4
    assert boat.hp == 0
    assert board.sinked[0]

def test_lost():
    board = Board()
    boat1 = Boat(2,(0,0))
    boat2 = Boat(2, (2,0))
    board.put_boat(boat1)
    board.put_boat(boat2)

    board.shoot((0,0))
    board.shoot((0,1))
    assert board.lost() == False

    board.shoot((2,0))
    board.shoot((2,1))
    assert board.lost()



