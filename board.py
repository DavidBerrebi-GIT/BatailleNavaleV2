import random as R
from boat import Boat


class Board :
    #-1 case vide, -2 tir dans l'eau, -3 zone interdite à bord d'un bateau, -4 bateau touché, autre nub du navire
    car = {-1 : "⸳", -2 : "~", -3 : ":", 0 : "□", -4 : "▩"}    
    def __init__(self):
        self.cells = [[-1 for _ in range(10) ] for _ in range(10)]
        self.boats = []
        self.sinked = []
    
    
    def put_boat(self, boat):
        #On suppose la validité du placement avant d'appeler cette fonction
        nb = len(self.boats)
        
        x,y = boat.position
        self.boats.append(boat)
        self.sinked.append(False)
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
                    if self.cells[x+i][y+j] == -1:
                        self.cells[x+i][y+j] = -3
    
    
    def _valid_cell(self, cell):
        x,y = cell
        if 0 <= x < 10 and 0 <= y < 10:
            return True
        else:
            return False
        
    def hit(self, indice_boat):
        if self.sinked[indice_boat]:
            return
        boat = self.boats[indice_boat]
        sinked = boat.hit()
        if sinked:
            self.sink(indice_boat)

    def sink(self, indice_boat):
        boat = self.boats[indice_boat]
        self.sinked[indice_boat] = True
        cells = boat.cells
        for cell in cells:
            x,y = cell
            for i in range(-1,2):
                for j in range (-1,2):
                    if self._valid_cell((x+i,y+j)) and self.cells[x+i][y+j] == -3:
                        self.cells[x+i][y+j] = -2


    def show(self, hided = True):
        print("\n  ABCDEFGHIJ")
        for x in range(10):
            print()
            print(f"{x+1:2}", end="")
            for y in range(10):
                valeur = self.cells[x][y]
                #Le plateau n'affiche pas les navires en partie normal
                if hided and (valeur >= 0 or valeur == -3):
                    valeur = -1
                elif valeur >= 0:
                    valeur = 0
                print(Board.car[valeur], end="")
        print()

