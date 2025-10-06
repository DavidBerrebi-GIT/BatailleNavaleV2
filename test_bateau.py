from boat import Boat

def test_init():
    boat = Boat(2,(5,5),True)
    assert boat != None
    assert boat.cells == [(5,5),(6,5)]