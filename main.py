from board import Board
from boat import Boat


def input_position(string):
    s = input(string)
    y = ord(s[0].upper()) - ord('A')
    x = int(s[1:]) - 1
    return (x,y)

def shoot_input():
    x,y = input_position("Ou voulez vous tirer ? (lettre puis nombre: A10, D5 etc) ")
    while not(0<=x<10 and 0<=y<10):
        x,y = input_position("Choisissez des valeurs valides, lettre entre A et J et chiffre en 1 et 10 ")
    return x,y

def boat_input():
    s = input("Code Navire :")
    if not valid_code_boat(s):
        s = input("Entrez un code Navire valide :")
    size = int(s[0])
    vertical = True if s[1] == 'V' else False
    y = ord(s[2].upper()) - ord('A')
    x = int(s[3:]) - 1
    return size,(x,y),vertical

def valid_code_boat(s):
    if s[0] not in "2345":
        return False
    if s[1].upper not in "HV":
        return False
    if s[2].upper not in "ABCDEFGHIJ":
        return False
    if s[3:] not in ["1","2","3","4","5","6","7","8","9","10"]:
        return False
    return True


def game():
    board1 = Board()
    board2 = Board()
    turn = 0

    board2.put_random_all_boats()



