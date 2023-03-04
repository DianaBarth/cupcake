import random

from WonderUmgebung import Position, Umgebung

class WonderBlume(object):
   
    def __init__(self, position, umgebung):
        self.text = ""
        self.groessen = ["winzige", "kleine", "mittelgroße", "große", "rießige"]
        self.position = position
        self.umgebungssatz = umgebung.gebeUmgebungssatz()
        self.groessenzahl = 1 
        self.hauptfarbe = random.choice(["rot", "gelbe", "blau"])
        self.unterfarbe = random.choice(["rosanen", "violetten", "purpurnen"])
        self.blattform = random.choice(["keinen", "runden", "stacheligen"])
        self.gepflueckt = False
    

    def gebePosition(self):
        return self.position

    def identifiziere(self):
        return self.groessen(self.groessenzahl) + " Blume mit " + self.hauptfarbe + "-" + self.unterfarbe + " Blüten und " + self.blattform + " Blättern " +  self.umgebungssatz

    def pfluecke(self):
        self.gepflueckt = True
        self.text = "du pflueckst die " + self.identifiziere + " und hast diese nun in deinem Inventar"
        return self.text

    def pruefegepflueckt(self):
         return self.gepflueckt
    
    def gieße(self):
        if self.groessenzahl < len(self.groessen):
            self.text = "du gießt die " + self.identifiziere + " und diese beginnt zu wachsen"
            self.groessenzahl = self.groessenzahl+1
        else:
            self.text = "du gießt die " + self.identifiziere + ", aber diese kann nicht weiter wachsen"
        return self.text
    
class BlumenSpawner(object):

    def __init__(self, umgebung, z):
        self.alleBlumen = [] 
        for x in range(umgebung.gebeStartBegrenzung().gebeX(), umgebung.gebeEndbegrenzung.gebeX() ):
            for y in  range(umgebung.gebeStartBegrenzung().gebeY(), umgebung.gebeEndbegrenzung.gebeY()):
                nordOst = Position(x,y,z)
                self.alleBlumen.append (WonderBlume(nordOst,umgebung))
                if x > 0:
                    nordWest = Position(-x,y,z)
                    self.alleBlumen.append (WonderBlume(nordWest,umgebung))
                if x!=y:
                    südOSt = Position(x,-y,z)
                    self.alleBlumen.append (WonderBlume(südOSt,umgebung))                  
                    if y > 0:
                        südWest = Position(-x,-y,z)
                        self.alleBlumen.append (WonderBlume(südWest,umgebung))  


    def gebeBlumeAnPosition(self, position):
        for blume in self.alleBlumen:
            if blume.gebePosition.gebeX() == position.gebeX() and blume.gebePosition.gebeY() == position.gebeY() and blume.gebePosition.gebeZ() == position.gebeZ():
                return blume 