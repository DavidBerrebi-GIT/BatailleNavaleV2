import random as R
from boat import Boat


class Board :
    
    def __init__(self):
        self.cells = [[-1 for _ in range(10) ] for _ in range(10)]
        self.boats = []
    
    
    def put_boat(self, boat):
        #On suppose la validité du placement avant d'appeler cette fonction
        nb = self.boats.length()
        
        x,y = boat.position
        for i in range(boat.length):
            if boat.vertical:
                self.cells[x+i][y] = nb << 1
                self._put_forbiden_cells((x+i,y))
            else :
                self.cells[x][y+i] = 1 << nb
                self._put_forbiden_cells((x,y+i))
    
    
    def _put_forbiden_cells(self, cell):
        x,y = cell
        for i in range(-1,2):
            for j in range(-1,2):
                if self._valid_cell((x+i,y+j)):
                    if self.cases[x+i][y+j] == 0:
                        self.cases[x+i][y+j] = 2
    
    
    def _valid_cell(self, cell):
        x,y = cell
        if 0 <= x < 10 and 0 <= y < 10:
            return True
        else:
            return False

