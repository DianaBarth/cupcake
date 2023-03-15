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
        self.bewegung = Bewegung(self.umgebungen.gebeStartUmgebung(),self.wondertext, self.wortVergleicher)
        self.umgebungen.gebeStartUmgebung().setzeBewegung(self.bewegung)
        self.DoktormutterPosition = self.umgebungen.gebeDoktormutterPosition()
        self.umgebung =  self.umgebungen.gebeStartUmgebung()

    def spiele(self):

        self.wondertext.setzeText("=================WonderDoktorandin========================" + "\n")
        self.wondertext.ergaenzeText("Du bist eine Doktorandin der Biologie. Deine Aufgabe ist es, 3 rießige Pflanzen zu finden und dann zu deiner Doktormutter zu bringen." + "\n") 
        self.wondertext.ergaenzeText("Deine Doktormutter befindet sich an der Position (X.Y.Z=)" + str(self.DoktormutterPosition.gebeX()) +  "." + str(self.DoktormutterPosition.gebeY()) + "." + str(self.DoktormutterPosition.gebeZ()) )   
        self.wondertext.ergaenzeText("Du bist aktuell auf der Wiese an Position 0.0.0 und kannst hier gehen oder rennen. Gib hierzu bitte 'gehe' oder 'renne' sowie eine der 4 Himmelsrichtungen ein.")
        self.wondertext.ergaenzeText("Um das Spiel vorzeitig zu beenden, gebe bitte 'beenden' ein.")

        self.wondertext.druckeText()           
        self.wondertext.druckeAbschluss()
        self.spiellaueft = True
        beendenAngetriggert = False

        while self.spiellaueft:            
           
            self.wondertext.setzeText("====================================================" + "\n")

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

                elif self.eingegebenesWort.gebeWortTyp() == WortTyp.SpielBeenden:
                    if beendenAngetriggert == False:
                          self.wondertext.ergaenzeText("Möchtest Du wirklich das Spiel vorzeitig beenden? Dann wiederhole Deine Eingabe!")
                          beendenAngetriggert = True
                    else:
                        self.wondertext.ergaenzeText("Du beendest nun das Spiel. Viel Spaß noch!")
                        self.spiellaueft = False
            else:
                self.wondertext.druckeEingabeNichtErkannt(usereingabe)

            if (self.bewegung.gebePosition().gebeX() == self.DoktormutterPosition.gebeX() and self.bewegung.gebePosition().gebeY() == self.DoktormutterPosition.gebeY()):
                self.wondertext.ergaenzeText("-----" + "\n")
                if self.wonderInventar.zaehleRiesigeBlumen() < 3:                    
                    self.wondertext.ergaenzeText("Vor dir steht deine Doktormutter, aber Du kannst ihr noch nicht genügend rießige Blumen vorweisen!")
                else:                  
                    self.wondertext.ergaenzeText("Vor Dir steht deine Doktormutter. Da Du genug rießige Blumen im Inventar hast, überreicht sie Dir Deinen Doktortitel! Du hast das Ziel des Spiels erreicht!")
                    self.spiellaueft = False   
            elif self.wonderInventar.zaehleRiesigeBlumen() >= 3:
                self.wondertext.ergaenzeText("-----" + "\n")
                self.wondertext.ergaenzeText("Suche Deine Doktormutter! Deine Doktormutter befindet sich an der Position " + str(self.DoktormutterPosition.gebeX()) +  "." + str(self.DoktormutterPosition.gebeY()) + "." + str(self.DoktormutterPosition.gebeZ()) )   
   

            self.wondertext.druckeText()           
            self.wondertext.druckeAbschluss()

meinspiel = Spiel()
meinspiel.spiele()