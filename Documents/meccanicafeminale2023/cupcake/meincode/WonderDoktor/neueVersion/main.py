#!/usr/bin/env python3

from WonderPosition import *
from WonderVerben import *
from WonderBlumen import *
from WonderUmgebung import *
from WonderBewegung import *
from WonderTexte import *



class Spiel(object):
    def __init__(self):
        self.verbvergleicher = VerbVergleicher()
        self.wondertext = WonderText()
        self.umgebungen = UmgebungsGenerator(self.verbvergleicher)      
        self.bewegung = Bewegung(self.umgebungen.gebeStartUmgebung(),self.wondertext)
        self.umgebungen.gebeStartUmgebung().setzeBewegung(self.bewegung)
        
    def spiele(self):

        print("=================WonderDoktor========================")

        while True:            
            usereingabe = input("> ").casefold()
            eingegebenesVerb = self.verbvergleicher.vergleiche(usereingabe)
            if eingegebenesVerb is not None:
                if eingegebenesVerb.verbtyp == VerbTyp.Flaeche or  eingegebenesVerb.verbtyp == VerbTyp.Ebene or  eingegebenesVerb.verbtyp == VerbTyp.Uebergang:
                    self.bewegung.bewege(usereingabe, eingegebenesVerb)   
                    self.umgebung =  self.bewegung.gebeUmgebung()

##Achtung, hab hier funktioniert es nicht mehr!

                #    self.blume:WonderBlume = self.umgebung.gebeBlume(self.bewegung.gebePosition())
                #if self.blume.pruefegepflueckt() == False:
                #    self.wondertext.ergaenzeText("Du stehst vor einer " + self.blume.identifiziere())    
#               if eingegebenesVerb.vertyp == VerbTyp.Blumenpflege():
                  #  if self.blume.pruefegepflueckt() == False:
                  #      if eingegebenesVerb.gebeBezeichnung() == "gießen":
                  #          self.wondertext.setzeText ( blume.gieße())
                 #       elif eingegebenesVerb.gebeBezeichnung() == "pflücken":
#                            self.wondertext.setzeText(blume.pfluecke())


            self.wondertext.druckeText()           
            self.wondertext.druckeAbschluss()

meinspiel = Spiel()
meinspiel.spiele()