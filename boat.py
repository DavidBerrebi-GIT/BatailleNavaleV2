class Boat :
    def __init__(self, length, position, vertical = False):
        self.length = length
        self.position = position
        self.vertical = vertical
        self.pv = length
        self.coule = False
       
        self.cells = []
        x,y = position
        for i in range(length):
            
            if vertical:
                self.cells.append((x+i,y))
            else: 
                self.cells.append((x,y))
    
    
    def hit(self):
        self.pv -=1
        if self.pv == 0:
            return True
        return False
