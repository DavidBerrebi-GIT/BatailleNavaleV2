from bateau import Bateau

def test_init():
    bateau = Bateau(2,(5,5),True)
    assert bateau != None
    assert bateau.cases == [(5,5),(6,5)]