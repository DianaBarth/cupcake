from Unterdateien.WonderTexte import *
from Unterdateien.WonderVerben import *
from Unterdateien.WonderBewegung import *
from Unterdateien.WonderUmgebung import *
from Unterdateien.WonderBlumen import *
#
class Spiel(object):
    def __init__(self):
        self.verbvergleicher = VerbVergleicher()
        self.wondertext = WonderText()
        self.umgebungen = UmgebungsGenerator(self.verbvergleicher)      
        self.bewegung = Bewegung(self.umgebungen.gebeStartUmgebung(self.wondertext))
        self.umgebungen.gebeStartUmgebung().setzeBewegung(self.bewegung)
        
    def spiele(self):

        print("=================WonderDoktor========================")

        while True:            
            usereingabe = input("> ").casefold()
            eingegebenesVerb = self.verbvergleicher.vergleiche(usereingabe)
            if eingegebenesVerb is not None:
                if eingegebenesVerb.verbtyp == VerbTyp.Flaeche or  eingegebenesVerb.verbtyp == VerbTyp.Ebene or  eingegebenesVerb.verbtyp == VerbTyp.Uebergang:
                    self.bewegung.bewege(usereingabe, eingegebenesVerb)   
                    self.blume = self.bewegung.gebeUmgebung().gebeBlume(self.bewegung.gebePosition())
                    if self.blume.pruefegepflueckt() == False:
                        "Du stehst vor einer " + self.blume.identifiziere()    
                if eingegebenesVerb.vertyp == VerbTyp.Blumenpflege():
                    if self.blume.pruefegepflueckt() == False:
                        if eingegebenesVerb.gebeBezeichnung() == "gießen":
                            self.wondertext.setzeText ( self.blume.gieße())
                        elif eingegebenesVerb.gebeBezeichnung() == "pflücken":
                            self.wondertext.setzeText(self.blume.pfluecke())


            self.wondetext.druckeText()           
            self.wondetext.druckePosition()  
            self.wondetext.druckeAbschluss()

meinspiel = Spiel()
meinspiel.spiele()