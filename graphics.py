import tkinter as tk

class Graphics:
    ColorChart = {}
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bataille Navale")
        self.root.minsize(1200, 700)

        self.canvas1 = tk.Canvas(self.root,width=1200, height=700, bg="white")
        self.canvas2 = tk.Canvas(self.root,width=1200, height=700, bg="white")
    

    def draw_board(self, canvas, board):
        for i in range(10):
            for j in range(10):
                value = board.cells[i][j]
                fill =  Graphics.ColorChart[value]
                canvas.create_rectangle(2 + i*50, 2 + j*50, i*50 + 51 ,j*50 + 51 ,outline="black", fill=fill)
        canvas.pack()
