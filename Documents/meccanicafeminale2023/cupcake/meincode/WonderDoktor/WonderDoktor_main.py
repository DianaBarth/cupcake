from Unterdateien.WonderBewegung import *
from Unterdateien.WonderVerben import *
from Unterdateien.WonderUmgebung import *

class Spiel(object):
    def __init__(self):
        self.verbvergleicher = VerbVergleicher()
        self.umgebungen = UmgebungsGenerator(self.verbvergleicher)      
        self.bewegung = Bewegung(self.umgebungen.gebeStartUmgebung())
        self.umgebungen.gebeStartUmgebung().setzeBewegung(self.bewegung)
        
    def spiele(self):

        print("=================WonderDoktor========================")

        while True:            
            usereingabe = input("> ").casefold()
            eingegebenesVerb = self.verbvergleicher.vergleiche(usereingabe)
            if eingegebenesVerb.verbtyp == VerbTyp.Flaeche or  eingegebenesVerb.verbtyp == VerbTyp.Ebene or  eingegebenesVerb.verbtyp == VerbTyp.Uebergang:
                self.bewegung.bewege(usereingabe, eingegebenesVerb)
            self.bewegung.druckeText()           

meinspiel = Spiel()
meinspiel.spiele()