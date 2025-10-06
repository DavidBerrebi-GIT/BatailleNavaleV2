class Bateau :
    def __init__(self, taille, position, verticale = False):
        self.taille = taille
        self.position = position
        self.verticale = verticale
        self.coule = False
       
        self.cases = []
        x,y = position
        for i in range(taille):
            
            if verticale:
                self.cases.append((x+i,y))
            else: 
                self.cases.append((x,y))
