from board import Board
from boat import Boat
from random import randint
from graphics import Graphics
import time


def put_all_boats(window,board):
    dic = {2: 3, 3 : 2, 4: 1, 5:1}
    def boat_remaining ():
        for key in dic.keys():
            if dic[key] >0:
                return True
        return False


    parameters = {"size":2, "pos" : (0,0), "state" : 0}
    #Trois etats, 0 non placé, 1 horizontale, 2 verticale
    def choose_boat(event):
        x=event.x/10
        size = [5,4,3,3,2,2,2]
        parameters["size"] = size[x]

    def choose_position(event):
        x=event.x/10
        y=event.y/10
        parameters["pos"] = (x,y)
        parameters["state"] = (parameters["state"] + 1)%3
        if parameters["state"] == 1:
            boat = Boat(parameters["size"], parameters["pos"], False)
            if not board.valid_boat(boat):
                parameters["state"] = 2
            
    def draw_boat(boat):
        pass
            


        
    
    window.canvas1.bind('<Button-1>', choose_position)
    window.canvas_remaining1.bind('<Button-1>', choose_boat)
    
    
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
    window = Graphics()
    board1 = Board()
    board2 = Board()
    turn = 1

    board2.put_random_all_boats()
    put_all_boats(window,board1)
    run = True
    gagnant = -1

    x = 0
    y = 0
    def coordinates(event):
        x = event.x //50
        y = event.y //50
        
    window.canvas2.bind('<Button-1>', coordinates)
    
    while run and gagnant == -1:
        window.draw_board_player(board1)
        window.draw_board_opponnent(board2)
        
        if turn == 1:
            
            board2.shoot((x,y))
            time.sleep(1)

            if board2.lost():
                gagnant = 1
            
        else:
            x = randint(0,9)
            y = randint(0,9)
            board1.shoot((x,y))
            time.sleep(1)
            if board1.lost():
                gagnant = 2
        time.sleep(1)
        
        
        
    if gagnant == 1:
        print("Bravo, vous avez remporté la bataille")
    if gagnant == 2:
        print("Vous avez perdu la bataille...")



