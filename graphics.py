import tkinter as tk

class Graphics:
    ColorChart = {-1: "#fafafa", -2 : "#1658b4", -3:"#1658b4", -4 : "#ed8106", 0: "#23a418" }
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bataille Navale")
        self.root.minsize(1200, 700)

        self.root.columnconfigure(0,weight=10)
        self.root.columnconfigure(1,weight=10)
        self.root.columnconfigure(2,weight=1 )

        

        self.canvas1 = tk.Canvas(self.root,width=500, height=500, bg="white")
        self.canvas1.grid(column=0,row=0)
        self.canvas2 = tk.Canvas(self.root,width=500, height=500, bg="white")
        self.canvas2.grid(column=1,row=0)
        

        self.canvas_remaining1 = tk.Canvas(self.root,width=500, height=150, bg="white")
        self.canvas_remaining1.grid(column=0,row=1)
        self.canvas_remaining2 = tk.Canvas(self.root,width=500, height=150, bg="white")
        self.canvas_remaining2.grid(column=1,row=1)

        

    

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
        self.canvas1.grid(column=0,row=0)
        self.draw_remaining_boat(board,1)

    def draw_board_opponnent(self, board):
        for i in range(10):
            for j in range(10):
                value = board.cells[i][j]
                if value >= 0:
                    value = -1
                if value == -3:
                    value = -1
                fill =  Graphics.ColorChart[value]
                self.canvas2.create_rectangle(2 + i*50, 2 + j*50, i*50 + 51,j*50 + 51 ,outline="black", fill=fill)
        self.canvas2.grid(column=1,row=0)
        self.draw_remaining_boat(board,2)
    
    def draw_remaining_boat(self,board,player):
        size = 30
        canvas = self.canvas_remaining1 if player == 1 else self.canvas_remaining2
        for i in range(7):
            color = Graphics.ColorChart[-1] if  board.sinked[i] else Graphics.ColorChart[0]

            for j in range(board.boats[i].length):
                canvas.create_rectangle(2 +  size * i, 2 + size * j, size * (i + 1), size * (j+1), outline="black", fill=color)
                

