import tkinter as tk

class Graphics:
    ColorChart = {-1: "#fafafa", -2 : "#1658b4", -3:"#1658b4", -4 : "#ed8106", 0: "#23a418" }
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bataille Navale")
        self.root.minsize(1200, 700)

        self.canvas1 = tk.Canvas(self.root,width=1200, height=700, bg="white")

    

    def draw_board_player(self, board):
        for i in range(10):
            for j in range(10):
                value = board.cells[i][j] 
                if value >= 0:
                    value = 0
                if value == -3:
                    value = -1
                fill =  Graphics.ColorChart[value]
                self.canvas1.create_rectangle(2 + i*50, 2 + j*50, i*50 + 51 ,j*50 + 51 ,outline="black", fill=fill)
        self.canvas1.pack()

    def draw_board_opponnent(self, board):
        for i in range(10):
            for j in range(10):
                value = board.cells[i][j]
                if value >= 0:
                    value = -1
                if value == -3:
                    value = -1
                fill =  Graphics.ColorChart[value]
                self.canvas1.create_rectangle(2 + i*50 + 600, 2 + j*50, i*50 + 51 +600 ,j*50 + 51 ,outline="black", fill=fill)
        self.canvas1.pack()
    