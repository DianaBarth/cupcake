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
        self.wonderInventar = WonderInventar(self.wortVergleicher)
        self.umgebungen = UmgebungsGenerator(self.wortVergleicher)      
        self.bewegung = Bewegung(self.umgebungen.gebeStartUmgebung(),self.wondertext)
        self.umgebungen.gebeStartUmgebung().setzeBewegung(self.bewegung)
        self.DoktormutterPosition = self.umgebungen.gebeDoktormutterPosition()
        self.umgebung =  self.umgebungen.gebeStartUmgebung()

    def spiele(self):

        self.wondertext.setzeText("=================WonderDoktorandin========================" + "\n")
        self.wondertext.ergaenzeText("Du bist eine Doktorandin der Biologie. Deine Aufgabe ist es, 3 rießige Pflanzen zu finden und dann zu deiner Doktormutter zu bringen." + "\n") 
        self.wondertext.ergaenzeText("Deine Doktormutter befindet sich an der Position " + str(self.DoktormutterPosition.gebeX()) +  "." + str(self.DoktormutterPosition.gebeY()) + "." + str(self.DoktormutterPosition.gebeZ()) )   
        self.wondertext.ergaenzeText("Du bist aktuell auf der Wiese und kannst hier gehen oder rennen. Gib hierzu bitte 'gehe' oder 'renne' sowie eine der 4 Himmerlsrichtungen ein.")
        self.wondertext.druckeText()           
        self.wondertext.druckeAbschluss()
        self.spiellaueft = True

        while self.spiellaueft:            
            usereingabe = input("Bitte gib hier deinen nächste gewünschte Tätigkeit ein: ").casefold()
            self.eingegebenesWort = self.wortVergleicher.vergleiche(usereingabe)

            if self.eingegebenesWort is not None:
                if self.eingegebenesWort.gebeWortTyp() == WortTyp.Flaeche or  self.eingegebenesWort.gebeWortTyp() == WortTyp.Ebene or  self.eingegebenesWort.gebeWortTyp() == WortTyp.Uebergang:
                    self.bewegung.bewege(usereingabe, self.eingegebenesWort)   
                    self.umgebung = self.bewegung.gebeUmgebung()
                    self.blume:WonderBlume = self.umgebung.gebeBlume(self.bewegung.gebePosition())
                    if self.blume is not None and self.blume.pruefegepflueckt() == False:
                        self.wondertext.ergaenzeText("Du siehst eine " + self.blume.identifiziere()+ ".")
                        self.wondertext.ergaenzeText("Du kannst Blumen gießen und pflücken.")
                elif self.eingegebenesWort.gebeWortTyp() == WortTyp.Blumenpflege:
                    if self.blume is not None and self.blume.pruefegepflueckt() == False:
                        if self.eingegebenesWort.gebeBezeichnung() == "gießen":
                            self.wondertext.ergaenzeText ( self.blume.gieße())
                        elif self.eingegebenesWort.gebeBezeichnung() == "pflücken":                     
                            self.wondertext.ergaenzeText(self.blume.pfluecke())
                            self.wondertext.ergaenzeText(self.wonderInventar.SteckeBlumeInsInventar(self.blume))                                       
                    else:  
                        self.wondertext.ergaenzeText("Du kannst hier nicht " + self.eingegebenesWort.gebeBezeichnung() + ".")

                elif self.eingegebenesWort.gebeWortTyp() == WortTyp.Inventar:
                    self.wondertext.ergaenzeText(self.wonderInventar.GebeInventarAusgabe())
    
            else:
                self.wondertext.druckeEingabeNichtErkannt(usereingabe)


            if (self.bewegung.gebePosition() != self.DoktormutterPosition):
                if self.wonderInventar.zaehleRiesigeBlumen() >= 3:
                     self.wondertext.ergaenzeText("Suche Deine Doktormutter! Deine Doktormutter befindet sich an der Position " + str(self.DoktormutterPosition.gebeX()) +  "." + str(self.DoktormutterPosition.gebeY()) + "." + str(self.DoktormutterPosition.gebeZ()) )   
            else:
                if self.wonderInventar.zaehleRiesigeBlumen() < 10:
                    self.wondertext.ergaenzeText("Vor dir steht deine Doktormutter, aber du kannst ihr noch nicht genügend rießige Blumen vorweisen!")
                else:
                    self.wondertext.ergaenzeText("Vor dir steht deine Doktormutter. Da du genug rießige Blumen im Inventar hast, überreicht sie dir deinen Doktortitel! Du hast das Ziel des Spiels erreicht!")
                    self.spiellaueft = False   
         
            self.wondertext.druckeText()           
            self.wondertext.druckeAbschluss()

meinspiel = Spiel()
meinspiel.spiele()