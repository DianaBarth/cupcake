from WonderWoerter import *
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
        if "angestoßen" in endgrenzTest or "angestoßen" in startgrenzTest:
            self.uebergangstyp = "Ende der Ebene"
            self.grenztest = "angestoßen"
            return True
        elif "kleineres" in endgrenzTest and "kleineres" in startgrenzTest:
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

    def praktiziereUebergang(self, benutzereingabe, benutzerWort, vergleichsergebnis, uebergangstyp):
        
        uebergangsWort = self.umgebung.gebeUebergangsWort(uebergangstyp)
        
        if uebergangsWort.gebeBezeichnung() ==  benutzerWort.gebeBezeichnung():  
            self.umgebung.setzeGeschwindigkeitenFuerUebergang(uebergangstyp)
      
            anschlussWort = self.umgebung.gebeAnschlussWort(uebergangstyp)

            if "offset" in vergleichsergebnis:
                offsetWort = self.umgebung.gebeOffsetWort(uebergangstyp)   

                self.setzeEingabe(offsetWort.gebeBezeichnung() + " " + vergleichsergebnis)
                self.bewegeEbene(offsetWort)
          
                self.setzeEingabe(uebergangsWort.gebeBezeichnung() + " " + vergleichsergebnis)             
                self.bewegeUebergang(uebergangsWort)
                 
                self.setzeEingabe(anschlussWort.gebeBezeichnung() + " " + vergleichsergebnis)             
                self.bewegeEbene(anschlussWort)                        
            else:
                self.setzeEingabe(uebergangsWort.gebeBezeichnung() + " " + vergleichsergebnis)             
                self.bewegeUebergang(uebergangsWort)              
                self.setzeEingabe(anschlussWort.gebeBezeichnung() + " " + vergleichsergebnis)                          
                self.bewegeEbene(anschlussWort)                           
                self.umgebung.entferneGeschwindigkeitenFuerUebergang(uebergangstyp)            
            return True 
        else:
            if "nord" in vergleichsergebnis and "nord" in benutzereingabe   :
                print("Du kannst nicht nach Norden " + benutzerWort.gebeBezeichnung() + ".")
                print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
            elif "ost" in vergleichsergebnis and "ost" in benutzereingabe:
                print("Du kannst nicht nach Osten " + benutzerWort.gebeBezeichnung() + ".")
                print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
            elif "süd" in vergleichsergebnis and "süd" in benutzereingabe:
                print("Du kannst nicht nach Süden " + benutzerWort.gebeBezeichnung() + ".")
                print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
            elif "west" in vergleichsergebnis and "west" in benutzereingabe:
                print("Du kannst nicht nach Westen " + benutzerWort.gebeBezeichnung() + ".")
                print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
            else:  
                 self.bewegeEbene(benutzerWort)

            return False  

    def bewege(self, eingabe, bewegungsWort):
        self.eingabe =  eingabe
        
        self.uebergang = self.pruefeUebergang()
        self.wonderText.setzeText("")

        if  self.uebergang == False:    
            wort = self.umgebung.vergleicheWorte(eingabe)
            if wort is None:
                self.wonderText.ergaenzeText("Achtung,in diesem Gebiet (" + str(self.umgebung.gebeBezeichnung())+ ") kann man nicht " + bewegungsWort.gebeBezeichnung() + ".")
                
                if "kleineres" not in self.grenzTest:
                    self.wonderText.ergaenzeText ( self.umgebung.gebeUebergangssatz(self.grenzTest, self.uebergangstyp))                 
                    self.uebergang = True
            elif "angestoßen" in self.grenztest:
                self.wonderText.ergaenzeText("Achtung, Du stößt an die Grenze des Gebiets " + str(self.umgebung.gebeBezeichnung())+ ") und kannst nicht weiter  " + bewegungsWort.gebeBezeichnung() + ".")
                               
            elif "kleineres" in self.grenzTest:
                # Bewegung durchführen
                if wort.gebeWortTyp() == WortTyp.Flaeche:
                    self.bewegeFläche(Wort)             
                   
                elif wort.gebeWortTyp() == WortTyp.Ebene:
                    self.bewegeEbene((Wort))           
                   
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
            if self.praktiziereUebergang(eingabe,bewegungsWort,self.grenzTest, self.uebergangstyp) == True:
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

    def bewegeFläche(self, Wort):

        geschwindigkeit = self.umgebung.gebeGeschwindigkeit(Wort)

        if "nord" in self.eingabe:
            self.nord(geschwindigkeit)
        elif "ost" in self.eingabe:
            self.ost(geschwindigkeit)
        elif "süd" in self.eingabe:
            self.süd(geschwindigkeit)
        elif "west" in self.eingabe:
            self.west(geschwindigkeit)
        else:
            self.wonderText.druckeEingabeNichtErkannt(self.eingabe)
            return False
        
        self.wonderText.ergaenzeText ("Du " + Wort.gebeEineAusgabeZurEingabe(self.eingabe) + " nach " + self.richtungstext + ".")
        return True
    def bewegeEbene(self, Wort):

        geschwindigkeit = self.umgebung.gebeGeschwindigkeit(Wort)

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
            self.wonderText.druckeEingabeNichtErkannt(self.eingabe)
            return False
                
        self.wonderText.ergaenzeText ("Du " + Wort.gebeEineAusgabeZurEingabe(self.eingabe) + " nach " + self.richtungstext + "." )
        return True
   
    def bewegeUebergang(self, Wort):
        if Wort.gebeBezeichnung() == "oeffnen":
           self.wonderText.ergaenzeText ("Du " + str(Wort.gebeEineAusgabeZurEingabe(self.eingabe)) + ".")
        else:
            geschwindigkeit = self.umgebung.gebeGeschwindigkeit(Wort)        
        
            if "hoch" in self.eingabe:
                self.hoehe(geschwindigkeit)
            elif "runter" in self.eingabe:
                self.hoehe(- geschwindigkeit)
            else:
                self.hoehe(geschwindigkeit)
        
            self.wonderText.ergaenzeText ("Du " + str(Wort.gebeEineAusgabeZurEingabe(self.eingabe)) + " nach " + self.richtungstext + ".")
        
        
