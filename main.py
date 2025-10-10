from board import Board
from boat import Boat
import random 



def shoot_input():
    s = input("Ou voulez vous tirer ? (lettre puis nombre: A10, D5 etc) ")
    y = ord(s[0].upper()) - ord('A')
    x = int(s[1:]) - 1
    while not(0<=x<10 and 0<=y<10):
        s = input("Choisissez de valeur valide ? lettre entre A et J et chiffre en 1 et 10 ")
        y = ord(s[0].upper()) - ord('A')
        x = int(s[1:]) - 1
    return x,y

def boat_input():
    s = input("Ou voulez vous tirer ? (lettre puis nombre: A10, D5 etc) ")
    y = ord(s[0].upper()) - ord('A')
    x = int(s[1:]) - 1
    while not(0<=x<10 and 0<=y<10):
        s = input("Choisissez de valeur valide ? lettre entre A et J et chiffre en 1 et 10 ")
        y = ord(s[0].upper()) - ord('A')
        x = int(s[1:]) - 1


def game():
    board1 = Board()
    board2 = Board()
    turn = 0

