from board import Board
from boat import Boat
from random import randint

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
    while not valid_code_boat(s):
        s = input("Entrez un code Navire valide :")
    size = int(s[0])
    vertical = True if s[1] == 'V' else False
    y = ord(s[2].upper()) - ord('A')
    x = int(s[3:]) - 1
    return size,(x,y),vertical

def valid_code_boat(s):
    if s[0] not in "2345":
        return False
    if s[1].upper() not in "HV":
        return False
    if s[2].upper() not in "ABCDEFGHIJ":
        return False
    if s[3:] not in ["1","2","3","4","5","6","7","8","9","10"]:
        return False
    return True

def put_all_boats(board):
    dic = {2: 3, 3 : 2, 4: 1, 5:1}
    def boat_remaining ():
        for key in dic.keys():
            if dic[key] >0:
                return True
        return False

    rand = input("Placement aléatoire des navires ? [y/n]")
    if rand == "y":
        board.put_random_all_boats()
        print("Les navires ont été posés aléatoirement.")
        board.show(False)
        return
    
    while boat_remaining():
        print(f"Il reste ces navires à poser: □□ :{dic[2]} □□□:{dic[3]} □□□□:{dic[4]} □□□□□:{dic[5]}")
        board.show(False)
        size, position, vertical = boat_input()
        boat = Boat(size,position,vertical)
        if dic[size] == 0:
            print(f"Tous les navire de taille {size} ont déjà été posés. Choisissez une autre taile de navire")
            continue
        if not board.valid_boat(boat):
            print("La position du navire est invalide.")
            continue
        else:
          dic[size] -= 1
          board.put_boat(boat)
    print("Tous les navire ont été posés.")

        

def game():
    board1 = Board()
    board2 = Board()
    turn = 1

    board2.put_random_all_boats()
    put_all_boats(board1)
    run = True
    gagnant = -1
    while run and gagnant == -1:
        if turn == 1:
            board2.show()
            x,y = shoot_input()
            board2.shoot((x,y))
            board2.show()
            if board2.cells[x][y] == -2:
                print("Aucun navire touché ")
                turn = 2
            else:
                print("Navire touché!!")
            if board2.lost():
                gagnant = 1
        else:
            x = randint(0,9)
            y = randint(0,9)
            board1.shoot((x,y))
            board1.show(False)
            if board1.cells[x][y] == -2:
                print("L'ennemie a raté son tir")
                turn = 1
            else:
                print("Un de nos navire est touché!!")
            if board1.lost():
                gagnant = 2
        
        
    if gagnant == 1:
        print("Bravo, vous avez remporté la bataille")
    if gagnant == 2:
        print("Vous avez perdu la bataille...")



