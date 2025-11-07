import tkinter as tk

class Graphics:
    ColorChart = {-1: "#fafafa", -2 : "#1658b4", -3:"#6283b1", -4 : "#ed8106", 0: "#23a418" }
    board_cell_size = 50
    remaining_cell_size = 30
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bataille Navale")
        self.root.minsize(1200, 700)

        self.root.columnconfigure(0,weight=10)
        self.root.columnconfigure(1,weight=10)

        

        self.canvas1 = tk.Canvas(self.root,width=500, height=500, bg="white")
        self.canvas1.grid(column=0,row=0)
        self.canvas2 = tk.Canvas(self.root,width=500, height=500, bg="white")
        self.canvas2.grid(column=1,row=0)
        

        self.canvas_remaining1 = tk.Canvas(self.root,width=500, height=150, bg="white")
        self.canvas_remaining1.grid(column=0,row=1)
        self.canvas_remaining2 = tk.Canvas(self.root,width=500, height=150, bg="white")
        self.canvas_remaining2.grid(column=1,row=1)

        
    def draw_cell(self,canvas,x,y,color,size,xoffset = 0, yoffset = 0,tag=""):
        canvas.create_rectangle(2 + yoffset + y*size, 2 + xoffset + x*size, (y + 1)*size + 1 ,(x+1)*size + 1 ,outline="black", fill=color,tag=tag)

    def draw_board_player(self, board):
        size = Graphics.board_cell_size
        for i in range(10):
            for j in range(10):
                value = board.cells[i][j] 
                if value >= 0:
                    value = 0
             #   if value == -3:
             #      value = -1
                fill =  Graphics.ColorChart[value]
                self.draw_cell(self.canvas1,i,j,fill,size)
        self.canvas1.grid(column=0,row=0)
        self.draw_remaining_boat(board,1)

    def draw_board_opponnent(self, board):
        size = Graphics.board_cell_size
        for i in range(10):
            for j in range(10):
                value = board.cells[i][j]
                if value >= 0:
                    value = -1
                if value == -3:
                    value = -1
                fill =  Graphics.ColorChart[value]
                self.draw_cell(self.canvas2,i,j,fill, size)
        self.canvas2.grid(column=1,row=0)
        self.draw_remaining_boat(board,2)
    
    def draw_remaining_boat(self,board,player):
        size = Graphics.remaining_cell_size
        canvas = self.canvas_remaining1 if player == 1 else self.canvas_remaining2
        for i in range(len(board.boats)):
            color = Graphics.ColorChart[-1] if board.sinked[i] else Graphics.ColorChart[0]

            for j in range(board.boats[i].length):
                self.draw_cell(canvas,j,i,color,size,yoffset=2)
    
    def draw(self,board1,board2):
        self.draw_board_player(board1)
        self.draw_board_opponnent(board2)
        self.root.update()


    def draw_boat(self,boat):
        x,y = boat.position
        dx,dy = (1,0)if boat.vertical else (0,1)
        for i in range(boat.length):
            self.draw_cell(self.canvas1, x + i * dx, y + i*dy,"#76dd8e",Graphics.board_cell_size)

    def create_button(self,canvas,x,y,w,h,text,function):

        button = tk.Button(canvas,width=w, height = h, text=text, command=function,bg="#76dd8e")
        button.place(x=x,y=y)

        self.button_validate = button
    def victory_screen(self,text):
        self.canvas1.destroy()
        self.canvas2.destroy()
        self.canvas_remaining1.destroy()
        self.canvas_remaining2.destroy()
        
        self.root.columnconfigure(1,weight=0)
        self.canvas_victory = tk.Canvas(self.root,width=1200, height=500, bg="white")
        self.canvas_victory.create_text(600,300,texte=text)
        self.root.update()
