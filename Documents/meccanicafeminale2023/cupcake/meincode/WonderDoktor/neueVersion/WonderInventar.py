from WonderTexte import *
from WonderBlumen import *
from WonderWoerter import *

class WonderInventar(object):
    def __init__(self):
        self.inventar = []
        self.text =""

    def SteckeBlumeInsInventar(self,blume:WonderBlume):
        self.inventar.append(blume)
 
    def zaehleRiesigeBlumen(self):
        zaehler=0
        for blume in self.inventar:
            if blume.ermittleObRiesig():
                zaehler = zaehler+1
        return zaehler
    
    def GebeInventarAusgabe(self, eingegebenesWort:Wort):
        if self.inventar.count ==0:
            self.text =self.text + "Du hast nichts im Inventar!"
        else:
            self.text =self.text + "Du " + eingegebenesWort.gebeEineAusgabeZurEingabe()
            if self.inventar.count == 1:
                self.text =self.text + "genau eine Blume: "             
            else:
                self.text =self.text + self.inventar.count + " Blumen:"
                random.shuffle(self.inventar)       
            for blume in self.Inventar:
                self.text =self.text + blume.identifiziere()
            if self.zaehleRiesigeBlumen() ==0:
                self.text =self.text + "davon ist keine Blume rießig und für Deine Doktormutter geeignet"
            elif self.zaehleRiesigeBlumen()==1:
                self.text =self.text + "davon ist eine Blume rießig und für Deine Doktormutter geeignet"
            else:                
                self.text =self.text + "davon sind" + self.zaehleRiesigeBlumen() + "Blumen rießig und für Dine Doktormutter geeignet"
        return self.text
