from WonderVerben import *
from WonderTexte import *

class Bewegung(object):
    def __init__(self, startUmgebung, wonderText:WonderText):
          self.wonderText = wonderText
          self.text = ""
          self.richtungstext =""  
          self.umgebung = startUmgebung
          self.position = startUmgebung.gebeStartBegrenzung()
         
          self.kannfliegen = False
          self.eingabe = "start"
          self.uebergang = False

    def druckePosition(self) :
        return self.position.gebePositionsAusgabe()    
    
    def setzeEingabe(self,eingabe):
        self.eingabe = eingabe

    def gebeUmgebung(self):
        return self.umgebung
    
    def gebePosition(self):
        return self.position

    def pruefeUebergang(self):
            
        endgrenzTest = self.umgebung.testeEndBegrenzung(self.position) 
        startgrenzTest = self.umgebung.testeStartBegrenzung(self.position) 

        if "kleineres" in endgrenzTest and "kleineres" in startgrenzTest:
            self.uebergangstyp = "beides kleiner"
            self.grenzTest = "kleineres"
            return False
        elif "kleineres" not in endgrenzTest and "ende" in self.umgebung.gebeUebergangstypen():
            self.uebergangstyp = "ende"
            self.grenzTest = endgrenzTest
            return True
        elif "kleineres" not in startgrenzTest and "start" in self.umgebung.gebeUebergangstypen():
            self.uebergangstyp = "start"
            self.grenzTest = startgrenzTest
            return True
        else:
            self.uebergangstyp ="grenze nicht vorhanden"
            self.grenzTest = "kleineres"
            return False

    def praktiziereUebergang(self, benutzereingabe, benutzerverb, vergleichsergebnis, uebergangstyp):
        
        uebergangsVerb = self.umgebung.gebeUebergangsVerb(uebergangstyp)
        
        if uebergangsVerb.gebeBezeichnung() ==  benutzerverb.gebeBezeichnung():  
            self.umgebung.setzeGeschwindigkeitenFuerUebergang(uebergangstyp)
      
            anschlussVerb = self.umgebung.gebeAnschlussVerb(uebergangstyp)

            if "offset" in vergleichsergebnis:
                offsetVerb = self.umgebung.gebeOffsetVerb(uebergangstyp)   

                self.setzeEingabe(offsetVerb.gebeBezeichnung() + " " + vergleichsergebnis)
                self.bewegeEbene(offsetVerb)
          
                self.setzeEingabe(uebergangsVerb.gebeBezeichnung() + " " + vergleichsergebnis)             
                self.bewegeUebergang(uebergangsVerb)
                 
                self.setzeEingabe(anschlussVerb.gebeBezeichnung() + " " + vergleichsergebnis)             
                self.bewegeEbene(anschlussVerb)                        
            else:
                self.setzeEingabe(uebergangsVerb.gebeBezeichnung() + " " + vergleichsergebnis)             
                self.bewegeUebergang(uebergangsVerb)              
                self.setzeEingabe(anschlussVerb.gebeBezeichnung() + " " + vergleichsergebnis)                          
                self.bewegeEbene(anschlussVerb)                           
                self.umgebung.entferneGeschwindigkeitenFuerUebergang(uebergangstyp)            
            return True 
        else:
            if "nord" in vergleichsergebnis and "nord" in benutzereingabe   :
                print("Du kannst nicht nach Norden " + benutzerverb.gebeBezeichnung() + ".")
                print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
            elif "ost" in vergleichsergebnis and "ost" in benutzereingabe:
                print("Du kannst nicht nach Osten " + benutzerverb.gebeBezeichnung() + ".")
                print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
            elif "süd" in vergleichsergebnis and "süd" in benutzereingabe:
                print("Du kannst nicht nach Süden " + benutzerverb.gebeBezeichnung() + ".")
                print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
            elif "west" in vergleichsergebnis and "west" in benutzereingabe:
                print("Du kannst nicht nach Westen " + benutzerverb.gebeBezeichnung() + ".")
                print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
            else:  
                 self.bewegeEbene(benutzerverb)

            return False  

    def bewege(self, eingabe, bewegungsverb):
        self.eingabe =  eingabe
        
        self.uebergang = self.pruefeUebergang()
        self.wonderText.setzeText("")
        if  self.uebergang == False:    
            verb = self.umgebung.vergleicheVerben(eingabe)
            if verb is None:
                self.wonderText.ergaenzeText("Achtung,in diesem Gebiet (" + str(self.umgebung.gebeBezeichnung())+ ") kann man nicht " + bewegungsverb.gebeBezeichnung() + ".")
                
                if "kleineres" not in self.grenzTest:
                    self.wonderText.ergaenzeText ( self.umgebung.gebeUebergangssatz(self.grenzTest, self.uebergangstyp))                 
                    self.uebergang = True

            elif "kleineres" in self.grenzTest:
                # Bewegung durchführen
                if verb.gebeVerbtyp() == VerbTyp.Flaeche:
                    self.bewegeFläche(verb)             
                   
                elif  verb.gebeVerbtyp() == VerbTyp.Ebene:
                    self.bewegeEbene((verb))           
                   
                ##erneut prüfen, um wenn man jetzt an der Grenze ist Übergangssatz anzuzeigen
                self.uebergang = self.pruefeUebergang()
                if "kleineres" not in self.grenzTest:
                    self.wonderText.ergaenzeText ( self.umgebung.gebeUebergangssatz(self.grenzTest, self.uebergangstyp))                  
                    self.uebergang = True
            else:
                ##Übergangsatz anzeigen
                self.wonderText.setzeText(self.umgebung.gebeUebergangssatz(self.grenzTest, self.uebergangstyp))
                self.uebergang = True

             ##Position am Ende angeben
            self.wonderText.ergaenzeText(self.position.gebePositionsAusgabe())

        elif self.uebergang == True:         
            if self.praktiziereUebergang(eingabe,bewegungsverb,self.grenzTest, self.uebergangstyp) == True:
                ##Übergang durchführen             
                self.umgebung = self.umgebung.gebeNaechsteUmgebung(self, self.uebergangstyp)
            
            self.wonderText.ergaenzeText (self.position.gebePositionsAusgabe())
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
        else:
            self.Wondertext.druckeEingabeNichtErkannt()
            return False
        
        self.wonderText.ergaenzeText ("Du " + verb.gebeEineAusgabeZurEingabe(self.eingabe) + " nach " + self.richtungstext + ".")
        return True
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
        else:
            self.Wondertext.druckeEingabeNichtErkannt()
            return False
                
        self.wonderText.ergaenzeText ("Du " + verb.gebeEineAusgabeZurEingabe(self.eingabe) + " nach " + self.richtungstext + "." )
        return True
    
    def bewegeUebergang(self, verb):
        geschwindigkeit = self.umgebung.gebeGeschwindigkeit(verb)
        
        if "hoch" in self.eingabe:
            self.hoehe(geschwindigkeit)
        elif "runter" in self.eingabe:
            self.hoehe(- geschwindigkeit)
        else:
            self.hoehe(geschwindigkeit)

        self.wonderText.ergaenzeText ("Du " + str(verb.gebeEineAusgabeZurEingabe(self.eingabe)) + " nach " + self.richtungstext + ".")
    
        
