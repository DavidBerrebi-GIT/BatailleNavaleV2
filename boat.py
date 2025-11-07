class Boat :
    def __init__(self, length =2, position = (0,0), vertical = False):
        self.length = length
        self.position = position
        self.vertical = vertical
        self.hp = length
        self.coule = False
       
        self.cells = []
        x,y = position
        for i in range(length):
            
            if vertical:
                self.cells.append((x+i,y))
            else: 
                self.cells.append((x,y+i))
    
    
    def hit(self):
        self.hp -=1
        if self.hp == 0:
            return True
        return False
