import random as R
from boat import Boat


class Board :
    car = {-1 : "⸳", -2 : "~", 0 : "□", -3 : "▩"}    
    def __init__(self):
        self.cells = [[-1 for _ in range(10) ] for _ in range(10)]
        self.boats = []
    
    
    def put_boat(self, boat):
        #On suppose la validité du placement avant d'appeler cette fonction
        nb = len(self.boats)
        
        x,y = boat.position
        self.boats.append(boat)
        for i in range(boat.length):
            if boat.vertical:
                self.cells[x+i][y] = nb 
                self._put_forbiden_cells((x+i,y))
            else :
                self.cells[x][y+i] = nb 
                self._put_forbiden_cells((x,y+i))
    
    
    def _put_forbiden_cells(self, cell):
        x,y = cell
        for i in range(-1,2):
            for j in range(-1,2):
                if self._valid_cell((x+i,y+j)):
                    if self.cells[x+i][y+j] == 0:
                        self.cells[x+i][y+j] = 2
    
    
    def _valid_cell(self, cell):
        x,y = cell
        if 0 <= x < 10 and 0 <= y < 10:
            return True
        else:
            return False
        

    def show(self, hided = True):
        print("\n  ABCDEFGHIJ")
        for x in range(10):
            print()
            print(f"{x+1:2}", end="")
            for y in range(10):
                valeur = self.cells[x][y]
                #Le plateau n'affiche pas les navires en partie normal
                if hided and valeur >= 0:
                    valeur = -1
                elif valeur >= 0:
                    valeur = 0
                print(Board.car[valeur], end="")
        print()

