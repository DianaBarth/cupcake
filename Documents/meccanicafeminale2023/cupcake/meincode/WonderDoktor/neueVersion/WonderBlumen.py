import random

from WonderPosition import Position

class WonderBlume(object):
   
    def __init__(self, position:Position, umgebungssatz):
        self.text = ""
        self.groessen = ["winzige", "kleine", "mittelgroße", "große", "rießige"]
        self.position = position
        self.umgebungssatz = umgebungssatz
        self.groessenzahl = 0 
        self.hauptfarbe = random.choice(["rot", "gelbe", "blau"])
        self.unterfarbe = random.choice(["rosanen", "violetten", "purpurnen"])
        self.blattform = random.choice(["keinen", "runden", "stacheligen"])
        self.gepflueckt:bool = False
    
    def ermittleObRiesig(self):
        if self.groessenzahl < len(self.groessen)-1:
            return False
        else:
            return True

    def gebePosition(self)->Position:
        return self.position

    def identifiziere(self):
        if self.gepflueckt == False:
            return self.groessen[self.groessenzahl] + " Blume mit " + self.hauptfarbe + "-" + self.unterfarbe + " Blüten und " + self.blattform + " Blättern " 
        else:
            return self.groessen[self.groessenzahl] + " Blume mit " + self.hauptfarbe + "-" + self.unterfarbe + " Blüten und " + self.blattform + " Blättern " + self.umgebungssatz

    def pruefegepflueckt(self)-> bool:
         return self.gepflueckt
   
    def pfluecke(self):
        self.gepflueckt = True
        self.text = "du pflueckst die " + self.identifiziere() + " und hast diese nun in deinem Inventar."
        return self.text

    def gieße(self):
        if self.groessenzahl < len(self.groessen)-1:
            self.text = "du gießt die " + self.identifiziere() + "und diese beginnt zu wachsen."
            self.groessenzahl = self.groessenzahl+1
            self.text = self.text + "\n" + "Dies ist nune eine " + self.identifiziere() + "."
        else:
            self.text = "du gießt die " + self.identifiziere() + ", aber diese kann nicht weiter wachsen."
        return self.text
    
class BlumenSpawner(object):

    def __init__(self, startBegrenzung:Position, endBegrenzung:Position, z, umgebungssatz):
        self.alleBlumen =  [] 
        for x in range(startBegrenzung.gebeX(), endBegrenzung.gebeX() ):
            for y in  range(startBegrenzung.gebeY(), endBegrenzung.gebeY()):
                 #mit einer Wahrscheinlichkeit ist keine Blume vorhanden
                if random.choice[True,False,False,False] == True:
                    nordOst = Position(x,y,z)
                    self.alleBlumen.append (WonderBlume(nordOst,umgebungssatz))
                if x > 0:
                    if random.choice[True,False,False,False] == True:
                        nordWest = Position(-x,y,z)
                        self.alleBlumen.append (WonderBlume(nordWest,umgebungssatz))
                if x!=y:                   
                    if random.choice[True,False,False,False] == True:
                        self.alleBlumen.append (WonderBlume(südOst,umgebungssatz))   
                        südOst = Position(x,-y,z)               
                    if y > 0:
                        if random.choice[True,False,False,False] == True:
                            südWest = Position(-x,-y,z)
                            self.alleBlumen.append (WonderBlume(südWest,umgebungssatz))  


    def gebeBlumeAnPosition(self, position:Position)->WonderBlume:
        for blume in self.alleBlumen:
            if blume.gebePosition().gebeX() == position.gebeX() and blume.gebePosition().gebeY() == position.gebeY() and blume.gebePosition().gebeZ() == position.gebeZ():
                return blume 
        return None