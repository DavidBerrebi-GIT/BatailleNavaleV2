from board import Board
from boat import Boat
from random import randint
from graphics import Graphics
import time

def validate(event,board,parameters):
    if parameters["state"] == 0:
        return
    size = parameters["size"]
    pos = parameters["pos"]
    vertical = True if parameters["state"] == 2 else False
    boat = Boat(size,pos,vertical)
    board.put_boat(boat)
def put_all_boats(window,board):
    window.draw_board_player(board)

    parameters = {"size":2, "pos" : (-1,-1), "state" : 0}
    #Trois etats, 0 non placé, 1 horizontale, 2 verticale
    button_validate = window.create_button(window.canvas_remaining1,450,0,6,10,"Valider",lambda : validate(board,parameters))
    
    

    def choose_position(event):
        x=event.y//50
        y=event.x//50
        if parameters["pos"] == (x,y):
            parameters["pos"] = (x,y)
            parameters["state"] = (parameters["state"] + 1)%3
        else:
            parameters["pos"] = (x,y)
            parameters["state"] = 1
        if parameters["state"] == 1:
            boat = Boat(parameters["size"], parameters["pos"], False)
            if not board.valid_boat(boat):
                parameters["state"] = 2
            else:
                window.draw_board_player(board)
                window.draw_boat(boat)
        if parameters["state"] == 2:
            boat = Boat(parameters["size"], parameters["pos"], True)
            if not board.valid_boat(boat):
                parameters["state"] = 0
            else:
                window.draw_board_player(board)
                window.draw_boat(boat)
        if parameters["state"] == 0:
            window.draw_board_player(board)

            


        
    
    window.canvas1.bind('<Button-1>', choose_position)

    window.root.mainloop()
    
    
    
       



def game():
    window = Graphics()
    board1 = Board()
    board2 = Board()
    
    draw_game = lambda : window.draw(board1,board2)

    board2.put_random_all_boats()
    window.draw_board_opponnent(board2)
    
    put_all_boats(window,board1)
    
    run = True
    gagnant = -1
    turn = 1
    
    pos = [-1,-1]
    def coordinates(event):
        x = event.x //50
        y = event.y //50
        if x > 10:
            x = -1
        if y > 10:
            y = -1
        pos[0] = x
        pos[1] = y
        
    window.canvas2.bind('<Button-1>', coordinates)
    draw_game()
    
    while run and gagnant == -1:
        
        if turn == 1:
            if pos[0] == -1 or pos[1] == -1:
                continue
            x,y = pos[0], pos[1]
            board2.shoot((x,y))
            
            if board2.lost():
                gagnant = 1
            window.draw(board1,board2)
            turn = 2
        else:
            x = randint(0,9)
            y = randint(0,9)
            board1.shoot((x,y))
            time.sleep(1)
            if board1.lost():
                gagnant = 2
            turn = 1
            window.draw(board1,board2)
        time.sleep(1)
        window.root.mainloop()
        
        
        
    if gagnant == 1:
        print("Bravo, vous avez remporté la bataille")
    if gagnant == 2:
        print("Vous avez perdu la bataille...")



