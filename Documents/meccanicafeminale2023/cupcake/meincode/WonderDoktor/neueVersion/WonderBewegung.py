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

    def praktiziereUebergang(self, benutzereingabe, benutzerwort, vergleichsergebnis, uebergangstyp):
        
        uebergangswort = self.umgebung.gebeUebergangswort(uebergangstyp)
        
        if uebergangswort.gebeBezeichnung() ==  benutzerwort.gebeBezeichnung():  
            self.umgebung.setzeGeschwindigkeitenFuerUebergang(uebergangstyp)
      
            anschlusswort = self.umgebung.gebeAnschlusswort(uebergangstyp)

            if "offset" in vergleichsergebnis:
                offsetwort = self.umgebung.gebeOffsetwort(uebergangstyp)   

                self.setzeEingabe(offsetwort.gebeBezeichnung() + " " + vergleichsergebnis)
                self.bewegeEbene(offsetwort)
          
                self.setzeEingabe(uebergangswort.gebeBezeichnung() + " " + vergleichsergebnis)             
                self.bewegeUebergang(uebergangswort)
                 
                self.setzeEingabe(anschlusswort.gebeBezeichnung() + " " + vergleichsergebnis)             
                self.bewegeEbene(anschlusswort)                        
            else:
                self.setzeEingabe(uebergangswort.gebeBezeichnung() + " " + vergleichsergebnis)             
                self.bewegeUebergang(uebergangswort)              
                self.setzeEingabe(anschlusswort.gebeBezeichnung() + " " + vergleichsergebnis)                          
                self.bewegeEbene(anschlusswort)                           
                self.umgebung.entferneGeschwindigkeitenFuerUebergang(uebergangstyp)            
            return True 
        else:
            if "nord" in vergleichsergebnis and "nord" in benutzereingabe   :
                print("Du kannst nicht nach Norden " + benutzerwort.gebeBezeichnung() + ".")
                print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
            elif "ost" in vergleichsergebnis and "ost" in benutzereingabe:
                print("Du kannst nicht nach Osten " + benutzerwort.gebeBezeichnung() + ".")
                print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
            elif "süd" in vergleichsergebnis and "süd" in benutzereingabe:
                print("Du kannst nicht nach Süden " + benutzerwort.gebeBezeichnung() + ".")
                print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
            elif "west" in vergleichsergebnis and "west" in benutzereingabe:
                print("Du kannst nicht nach Westen " + benutzerwort.gebeBezeichnung() + ".")
                print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
            else:  
                 self.bewegeEbene(benutzerwort)

            return False  

    def bewege(self, eingabe, bewegungswort):
        self.eingabe =  eingabe
        
        self.uebergang = self.pruefeUebergang()
        self.wonderText.setzeText("")
        if  self.uebergang == False:    
            wort = self.umgebung.vergleicheworten(eingabe)
            if wort is None:
                self.wonderText.ergaenzeText("Achtung,in diesem Gebiet (" + str(self.umgebung.gebeBezeichnung())+ ") kann man nicht " + bewegungswort.gebeBezeichnung() + ".")
                
                if "kleineres" not in self.grenzTest:
                    self.wonderText.ergaenzeText ( self.umgebung.gebeUebergangssatz(self.grenzTest, self.uebergangstyp))                 
                    self.uebergang = True

            elif "kleineres" in self.grenzTest:
                # Bewegung durchführen
                if wort.gebeworttyp() == wortTyp.Flaeche:
                    self.bewegeFläche(wort)             
                   
                elif  wort.gebeworttyp() == wortTyp.Ebene:
                    self.bewegeEbene((wort))           
                   
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
            if self.praktiziereUebergang(eingabe,bewegungswort,self.grenzTest, self.uebergangstyp) == True:
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

    def bewegeFläche(self, wort):

        geschwindigkeit = self.umgebung.gebeGeschwindigkeit(wort)

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
        
        self.wonderText.ergaenzeText ("Du " + wort.gebeEineAusgabeZurEingabe(self.eingabe) + " nach " + self.richtungstext + ".")
        return True
    def bewegeEbene(self, wort):

        geschwindigkeit = self.umgebung.gebeGeschwindigkeit(wort)

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
                
        self.wonderText.ergaenzeText ("Du " + wort.gebeEineAusgabeZurEingabe(self.eingabe) + " nach " + self.richtungstext + "." )
        return True
    
    def bewegeUebergang(self, wort):
        geschwindigkeit = self.umgebung.gebeGeschwindigkeit(wort)
        
        if "hoch" in self.eingabe:
            self.hoehe(geschwindigkeit)
        elif "runter" in self.eingabe:
            self.hoehe(- geschwindigkeit)
        else:
            self.hoehe(geschwindigkeit)

        self.wonderText.ergaenzeText ("Du " + str(wort.gebeEineAusgabeZurEingabe(self.eingabe)) + " nach " + self.richtungstext + ".")
    
        
