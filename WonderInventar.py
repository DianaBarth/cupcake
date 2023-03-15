from WonderTexte import *
from WonderBlumen import *
from WonderWoerter import *

class WonderInventar(object):
    def __init__(self, wortvergleicher):
        self.inventar = []
        self.wortvergleicher = wortvergleicher
        self.text =""

    def SteckeBlumeInsInventar(self,blume:WonderBlume):
        self.inventar.append(blume)
        return "Du hast die Blume nun in deiner Tasche. Versuche nun dein Inventar anzusehen!"
 
    def zaehleRiesigeBlumen(self):
        zaehler=0
        for blume in self.inventar:
            if blume.ermittleObRiesig():
                zaehler = zaehler+1
        return zaehler
    
    def GebeInventarAusgabe(self):
        if len(self.inventar) == 0:
            self.text ="Du hast nichts im Inventar!"
        else:
            self.text = "Du " + self.wortvergleicher.gebeWort("Inventar").gebeEineAusgabeZurEingabe("Inventar") + " "
            if len(self.inventar) == 1:
                self.text =self.text + "genau eine Blume: \n"            
            else:
                self.text =self.text + str(len(self.inventar)) + " Blumen: \n"
                random.shuffle(self.inventar)       
            for blume in self.inventar:
                self.text =self.text + "- eine " + blume.identifiziere() + "\n"
            if self.zaehleRiesigeBlumen() ==0:
                self.text =self.text + "davon ist keine Blume rießig und für Denie Doktormutter geeignet \n"
            elif self.zaehleRiesigeBlumen()==1:
                self.text =self.text + "davon ist eine Blume rießig und für Deine Doktormutter geeignet \n"
            else:                
                self.text =self.text + "davon sind " + str(self.zaehleRiesigeBlumen()) + " Blumen rießig und für Deine Doktormutter geeignet \n"
        return self.text
