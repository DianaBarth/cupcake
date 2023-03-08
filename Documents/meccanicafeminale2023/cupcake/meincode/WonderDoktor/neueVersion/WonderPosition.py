class Position(object):
    def __init__(self,x,y,z):
        self.X = x
        self.Y = y
        self.Z = z        
    def ändereX(self,inkrement):
        self.X = self.X + inkrement       
    def ändereY(self,inkrement):
        self.Y = self.Y + inkrement        
    def ändereZ(self,inkrement):
        self.Z = self.Z + inkrement        
    def gebeX(self):
        return self.X
    def gebeY(self):
        return self.Y
    def gebeZ(self):
        return self.Z
    def gebePositionsAusgabe(self):
        return ("Du befindest dich an der Position " + str(self.gebeX()) + "." + str(self.gebeY()) + "." + str(self.gebeZ())) + "."
