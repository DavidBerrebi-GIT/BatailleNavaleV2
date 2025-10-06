from boat import Boat

def test_init():
    boat = Boat(2,(5,5),True)
    assert boat != None
    assert boat.cells == [(5,5),(6,5)]

def test_hit():
    boat = Boat(2,(0,0))
    assert boat.hit() == False
    assert boat.hp == 1
    assert boat.hit() == True