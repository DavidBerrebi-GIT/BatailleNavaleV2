from board import Board
from graphics import Graphics
import random
import tkinter as tk

def coordinates(event):
    global board_opponent
    x = event.x
    y = event.y
    board_opponent.shoot((x,y))

    
    print("end event")


random.seed(0)

board_player = Board()
board_player.put_random_all_boats()
board_opponent = Board()
board_opponent.put_random_all_boats()

board_player.shoot((0,4))
board_opponent.shoot((0,4))
board_player.shoot((1,3))
board_player.shoot((2,3))


window= Graphics()
window.draw_board_player(board_player)
window.draw_board_opponnent(board_opponent)
taille = tk.IntVar()
radio_button_taille2 = tk.Radiobutton(window.root, text ="1",variable = taille, value = 2)
radio_button_taille3 = tk.Radiobutton(window.root, text ="2",variable = taille, value = 3)
radio_button_taille4 = tk.Radiobutton(window.root, text ="3",variable = taille, value = 4)
radio_button_taille5 = tk.Radiobutton(window.root, text ="4",variable = taille, value = 5)
radio_button_taille2.pack()
radio_button_taille2.pack()
radio_button_taille3.pack()
radio_button_taille4.pack()
radio_button_taille5.pack()

window.canvas1.bind('<Button-1>', coordinates)
window.root.mainloop()