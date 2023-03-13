#!/usr/bin/env python3

from WonderPosition import *
from WonderWoerter import *
from WonderBlumen import *
from WonderUmgebung import *
from WonderBewegung import *
from WonderTexte import *
from WonderInventar import *


class Spiel(object):
    def __init__(self):
        self.wortVergleicher = WortVergleicher()
        self.wondertext = WonderText()
        self.wonderInventar = WonderInventar()
        self.umgebungen = UmgebungsGenerator(self.wortVergleicher)      
        self.bewegung = Bewegung(self.umgebungen.gebeStartUmgebung(),self.wondertext)
        self.umgebungen.gebeStartUmgebung().setzeBewegung(self.bewegung)
        self.DoktormutterPosition = self.umgebung.gebeDoktormutterPosition()
  

    def spiele(self):

        self.wondertext.setzeText("=================WonderDoktorandin========================")
        self.wondertext.ergaenzeText("Du bist eine Doktorandin der Biologie. Deine Aufgabe ist es, 10 rießige Pflanzen zu finden und dann zu deiner Doktormutter zu bringen.")
        self.wondertext.druckeText()           
        self.wondertext.druckeAbschluss()


        while True:            
            usereingabe = input("> ").casefold()
            eingegebenesWort = wortVergleicher.vergleiche(usereingabe)

            if eingegebenesWort is not None:
                if eingegebenesWort.Worttyp == WortTyp.Flaeche or  eingegebenesWort.Worttyp == WortTyp.Ebene or  eingegebenesWort.Worttyp == WortTyp.Uebergang:
                    self.bewegung.bewege(usereingabe, eingegebenesWort)   
                    self.umgebung = self.bewegung.gebeUmgebung()
                    self.blume:WonderBlume = self.umgebung.gebeBlume(self.bewegung.gebePosition())
                    if self.blume is not None and self.blume.pruefegepflueckt() == False:
                        self.wondertext.ergaenzeText("Du siehst eine " + self.blume.identifiziere()+ ".")

                elif eingegebenesWort.Worttyp == WortTyp.Blumenpflege:
                    if self.blume is not None and self.blume.pruefegepflueckt() == False:
                        if eingegebenesWort.gebeBezeichnung() == "gießen":
                            self.wondertext.ergaenzeText ( self.blume.gieße())
                        elif eingegebenesWort.gebeBezeichnung() == "pflücken":
                            self.wonderInventar.SteckeBlumeInsInventar(self.blume)
                            self.wondertext.ergaenzeText(self.blume.pfluecke())
                    else:  
                        self.wondertext.ergaenzeText("Du kannst hier nicht " + eingegebenesWort.gebeBezeichnung() + ".")

                elif eingegebenesWort.Worttyp == WortTyp.Inventar:
                    self.wonderInventar.GebeInventarAusgabe()

            if self.wonderInventar.zaehleRiesigeBlumen >= 10:
                self.wondertext.ergaenzeText("Suche Deine Doktormutter! Deine Doktormutter befindet sich an der Position " + self.DoktormutterPosition.gebeX() +  "." + self.DoktormutterPosition.gebeY() + "." + self.DoktormutterPosition.gebeZ() )   
         
            self.wondertext.druckeText()           
            self.wondertext.druckeAbschluss()

meinspiel = Spiel()
meinspiel.spiele()