
from Unterdateien.WonderVerben import *

class Bewegung(object):
    def __init__(self, startUmgebung):
          self.text = ""
          self.richtungstext =""  
          self.umgebung = startUmgebung
          self.position = startUmgebung.gebeStartBegrenzung()
         
          self.kannfliegen = False
          self.eingabe = "start"
          self.uebergang = False

    def druckeText(self):
         print(self.text)
    
    def druckePosition(self) :
        self.position.drucke

    def bewege(self, eingabe, verb):
        self.eingabe =  eingabe      

        EndgrenzTest = self.umgebung.testeEndBegrenzung(self.position) 
        if "kleineres" in EndgrenzTest :
            StartgrenzTest = self.umgebung.testeStartBegrenzung(self.position) 
            if "kleineres" in  StartgrenzTest:
                grenzTest = "kleineres"
            else:
                grenzTest = StartgrenzTest
        else:
            grenzTest = EndgrenzTest

        if  self.uebergang == False:    
            if "kleineres" in grenzTest:

                if verb.gebeVerbtyp() == VerbTyp.Flaeche:
                    self.bewegeFläche(verb)               
                    self.text = self.text +" \n" + self.position.gebePositionsAusgabe()

                elif self.umgebung.gebeUmgebungsTyp == VerbTyp.Ebene:
                    self.bewegeEbene((verb))             
                    self.text = self.text +" \n" + self.position.gebePositionsAusgabe()

            else:
                self.umgebung.gebeUebergangssatz(grenzTest)
                self.uebergang = True

        elif self.uebergang == True:
            if self.pruefeUebergang(eingabe,verb,grenzTest) == True:
                naechsteUmgebung = self.umgebung.gebeNaechsteUmgebung()
                naechsteUmgebung.setzeBewegung = self
                self.umgebung = naechsteUmgebung


            self.uebergang = False
            

    #Himmelsrichtungen

    def nord(self, geschwindigkeit):
        self.position.ändereY(geschwindigkeit)
        self.richtungstext = "Norden"
    
    def ost(self, geschwindigkeit):
        self.position.ändereX(geschwindigkeit)
        self.richtungstext = "Osten"

    def süd(self, geschwindigkeit):
        self.position.ändereY(-geschwindigkeit)
        self.richtungstext ="Süden"

    def west(self, geschwindigkeit):
        self.position.ändereX(-geschwindigkeit)
        self.richtungstext ="Westen"

    def hoehe(self, geschwindigkeit):
        self.position.ändereZ(geschwindigkeit)
        if geschwindigkeit > 0: 
            self.richtungstext = "oben"
        else :
            self.richtungstext = "unten" 

    #Bewegung allgemein

    def bewegeFläche(self, verb):

        geschwindigkeit = self.umgebung.gebeGeschwindigkeit(verb)

        if "nord" in self.eingabe:
            self.nord(geschwindigkeit)
        elif "ost" in self.eingabe:
            self.ost(geschwindigkeit)
        elif "süd" in self.eingabe:
            self.süd(geschwindigkeit)
        elif "west" in self.eingabe:
            self.west(geschwindigkeit)

        self.text = "Du " + verb.gebeEineAusgabeZurEingabe(self.eingabe) + " nach " + self.richtungstext + "."

    def bewegeEbene(self, verb):

        geschwindigkeit = self.umgebung.gebeGeschwindigkeit(verb)

        if "nord" in self.eingabe:
            self.nord(geschwindigkeit)
        elif "ost" in self.eingabe:
            self.ost(geschwindigkeit)
        elif "süd" in self.eingabe:
            self.süd(geschwindigkeit)
        elif "west" in self.eingabe  :
            self.west(geschwindigkeit)        
        elif "hoch" in self.eingabe:
            self.hoehe(geschwindigkeit)
        elif "runter" in self.eingabe:
            self.hoehe(- geschwindigkeit)

        self.text = "Du " + verb.gebeEineAusgabeZurEingabe(self.eingabe) + " nach " + self.richtungstext + "."
    
    def bewegeUebergang(self, verb):
        geschwindigkeit = self.umgebung.gebeGeschwindigkeit(verb)
        
        if "hoch" in self.eingabe:
            self.hoehe(geschwindigkeit)
        elif "runter" in self.eingabe:
            self.hoehe(- geschwindigkeit)
        else:
            self.hoehe(geschwindigkeit)

        self.text = "Du " + verb.gebeEineAusgabeZurEingabe(self.eingabe) + " nach " + self.richtungstext + "."
    
        
