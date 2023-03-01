import random

class WonderBlume(object):
    def __init__(self, position, umgebung):
        self.groessen = ["winzige", "kleine", "mittelgroße", "große", "rießige"]
        self.position = position
        self.umgebungssatz = umgebung.gebeUmgebungssatz()
        self.groessenzahl = 1 
        self.hauptfarbe = random.choice(["rot", "gelbe", "blau"])
        self.unterfarbe = random.choice(["rosanen", "violetten", "purpurnen"])
        self.blattform = random.choice(["keinen", "runden", "stacheligen"])
        self.gepflueckt = False

    def identifiziere(self):
        return self.groessen(self.groessenzahl) + " Blume mit " + self.hauptfarbe + "-" + self.unterfarbe + " Blüten und " + self.blattform + " Blättern " +  self.umgebungssatz.

    def pfluecke(self):
          self.gepflueckt = True

    def pruefegepflueckt(self):
         return self.gepflueckt
    
    def gieße(self):
        if self.groessenzahl < len(self.groessen):
            self.groessenzahl = self.groessenzahl+1

class BlumenSpawner(object):    
        def __init__(self, umgebung): 
              
             
        def gebeBlumeVonPosition(self, position):