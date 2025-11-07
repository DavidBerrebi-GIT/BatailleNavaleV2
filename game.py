from board import Board
from boat import Boat
from random import randint
from random import choice
from graphics import Graphics
import time

def validate(window,board,parameters):
    if parameters["state"] == 0:
        return
    size = parameters["size"]
    pos = parameters["pos"]
    vertical = True if parameters["state"] == 2 else False
    boat = Boat(size,pos,vertical)
    board.put_boat(boat)
    window.draw_board_player(board)
    if len(board.boats) == 7:
        window.root.quit()
        window.button_validate.destroy()
        window.canvas1.unbind('<Button-1>')

    parameters["size"] = [5,4,3,3,2,2,2,2][len(board.boats)]
    parameters["state"] = 0

    



def put_all_boats(window,board):
    window.draw_board_player(board)

    parameters = {"size":5, "pos" : (-1,-1), "state" : 0}
    #Trois etats, 0 non placé, 1 horizontale, 2 verticale
    window.create_button(window.canvas_remaining1,450,0,6,10,"Valider",lambda : validate(window,board,parameters))
    
    

    def choose_position(event):
        x=event.y//50
        y=event.x//50
        if parameters["pos"] == (x,y):
            parameters["pos"] = (x,y)
            parameters["state"] = 2 if parameters["state"] == 1 else 1
        else:
            parameters["pos"] = (x,y)
            parameters["state"] = 1 if parameters["state"] == 0 else parameters["state"]
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
   

    winner = -1
    turn = 1
    

    def coordinates(event,turn):
        global winner
        if turn == 2:
            return
        x = event.y //50
        y = event.x //50
        
        turn = 1 if board2.cells[x][y] >= 0 else 2
        board2.shoot((x,y))  
        window.draw(board1,board2)  
        if board2.lost():
            winner = 1
            window.canvas2.unbind('<Button-1>')
            window.root.quit()
        if turn == 1:
            return
    
        
        
        while turn == 2:
            x,y=0,0
            while ia_hit:
                x,y = choice(ia_hit)
                ia_hit.remove((x,y))
                if board2.cells[x][y] >= 0 or board2.cells[x][y] == -1 :
                    break
            else:
                x = randint(0,9)
                y = randint(0,9)
                while board1.cells[x][y] in [-2,-4]:
                    x = randint(0,9)
                    y = randint(0,9)
                
            
            turn = 1 
            print(f"x : {x}, y : {y}, case : {board1.cells[x][y]}")
            if board1.cells[x][y] >= 0:
                turn = 2
                for (i,j) in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if board1.valid_cell((x+i,y+j)):
                        ia_hit.append((x+i,y+j))
                
                for (i,j) in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                    if board1.valid_cell((x+i,y+j)):
                        board1.shoot((x+i,y+j))
            board1.shoot((x,y))
        
            window.draw(board1,board2)
            
            if board1.lost():
                winner = 2
                window.canvas2.unbind('<Button-1>')
                window.root.quit()

            time.sleep(0.1)

    
    ia_hit = []
        


        
    window.canvas2.bind('<Button-1>',lambda e: coordinates(e,turn))
    draw_game()
    window.root.mainloop()
    
        
    if winner != -1:
        window.victory_screen(winner)

        



