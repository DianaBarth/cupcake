from WonderWoerter import *
from WonderTexte import *

class Bewegung(object):
    def __init__(self, startUmgebung, wonderText:WonderText, wortVergleicher:WortVergleicher):
          self.wonderText = wonderText
          self.text = ""
          self.richtungstext =""  
          self.umgebung = startUmgebung
          self.position = startUmgebung.gebeStartBegrenzung()
          self.wortVergleicher = wortVergleicher
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

    def praktiziereUebergang(self, benutzereingabe, benutzerWort, vergleichsergebnis, uebergangstyp):
        #Rückgabewert = true wenn Übergang durchgeführt, ansonsten false
        uebergangsWort = self.umgebung.gebeUebergangsWort(uebergangstyp)
        
        if uebergangsWort is not None and uebergangsWort.gebeBezeichnung() ==  benutzerWort.gebeBezeichnung():  

            if self.umgebung.gebeBezeichnung() == "wasser":
                while self.position.gebeZ() < -1:
                    self.setzeEingabe("schwimme oben")
                    self.bewegeEbene(self.wortVergleicher.gebeWort("schwimmen"))


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
            if "nord" in vergleichsergebnis:
                if "nord" in benutzereingabe:
                    print("Du kannst nicht nach Norden " + benutzerWort.gebeBezeichnung() + ".")
                    print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
                elif "süd" in benutzereingabe:
                     self.bewegeEbene(benutzerWort)                     
                else:
                    print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
                    print("Wenn Du nicht nach Norden weiter willst, musst du erst wieder einen Schritt zurück nach Süden laufen!")                    
            elif "süd" in vergleichsergebnis:
                if "süd" in benutzereingabe:
                    print("Du kannst nicht nach Süden " + benutzerWort.gebeBezeichnung() + ".")
                    print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
                elif "nord" in benutzereingabe:
                     self.bewegeEbene(benutzerWort)                    
                else:
                    print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
                    print("Wenn Du nicht nach Süden weiter willst, musst du erst wieder einen Schritt zurück nach Norden laufen!")                    
            elif "ost" in vergleichsergebnis:
                if "ost" in benutzereingabe:
                    print("Du kannst nicht nach Osten " + benutzerWort.gebeBezeichnung() + ".")
                    print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
                elif "west" in benutzereingabe:
                    self.bewegeEbene(benutzerWort)
                    
                else:
                    print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
                    print("Wenn Du nicht nach Osten weiter willst, musst du erst wieder einen Schritt zurück nach Westen laufen!")                    
            elif "west" in vergleichsergebnis:
                if "west" in benutzereingabe:
                    print("Du kannst nicht nach Westen " + benutzerWort.gebeBezeichnung() + ".")
                    print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
                elif "ost" in benutzereingabe:
                     self.bewegeEbene(benutzerWort)
                    
                else:
                    print(self.umgebung.gebeUebergangssatz(vergleichsergebnis,uebergangstyp))
                    print("Wenn Du nicht nach Westen weiter willst, musst du erst wieder einen Schritt zurück nach Osten laufen!")                    
            else: 
                 self.bewegeEbene(benutzerWort)

            return False  

    def bewege(self, eingabe, bewegungsWort:Wort):
        self.eingabe =  eingabe
        
        self.uebergang = self.pruefeUebergang()
        self.wonderText.setzeText("")

        if  self.uebergang == False:    
            wort = self.umgebung.vergleicheWorte(eingabe)
            if wort is None:
                self.wonderText.ergaenzeText("Achtung,in diesem Gebiet (" + str(self.umgebung.gebeBezeichnung())+ ") kann man nicht " + bewegungsWort.gebeBezeichnung() + ".")
            elif "kleineres" not in self.grenzTest:
                    self.wonderText.ergaenzeText ( self.umgebung.gebeUebergangssatz(self.grenzTest, self.uebergangstyp))                 
                    self.uebergang = True                                 
            elif "kleineres" in self.grenzTest:
                # Bewegung durchführen
                if wort.gebeWortTyp() == WortTyp.Flaeche:
                    self.bewegeFläche(wort)             
                   
                elif wort.gebeWortTyp() == WortTyp.Ebene:
                    self.bewegeEbene(wort)          
                   
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

    def bewegeFläche(self, wort:Wort):

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
            self.wonderText.druckeEingabeNichtErkannt(self.eingabe)
            return False
        
        self.wonderText.ergaenzeText ("Du " +wort.gebeEineAusgabeZurEingabe(self.eingabe) + " nach " + self.richtungstext + ".")
        return True
    def bewegeEbene(self, wort:Wort):

        geschwindigkeit = self.umgebung.gebeGeschwindigkeit(wort)

        if "nord" in self.eingabe:
            self.nord(geschwindigkeit)
        elif "ost" in self.eingabe:
            self.ost(geschwindigkeit)
        elif "süd" in self.eingabe:
            self.süd(geschwindigkeit)
        elif "west" in self.eingabe  :
            self.west(geschwindigkeit)        
        elif "hoch" in self.eingabe or "oben" in self.eingabe:
            if "oben angestoßen" in self.umgebung.PruefeUntenUndOben(self.position):  
                self.wonderText.ergaenzeText ("Du kannst hier nicht weiter nach oben " + wort.gebeBezeichnung() + "!")               
                return True
            else:
                self.hoehe(geschwindigkeit)
        elif "runter" in self.eingabe or "unten" in self.eingabe:
            if "unten angestoßen" in self.umgebung.PruefeUntenUndOben(self.position):
                self.wonderText.ergaenzeText ("Du kannst hier nicht weiter nach unten " + wort.gebeBezeichnung() + "!")  
                return True              
            else:
                self.hoehe(- geschwindigkeit)            
        else:
            self.wonderText.druckeEingabeNichtErkannt(self.eingabe)
            return False
                
        self.wonderText.ergaenzeText ("Du " + wort.gebeEineAusgabeZurEingabe(self.eingabe) + " nach " + self.richtungstext + "." )
        return True
   
    def bewegeUebergang(self, wort:Wort):
        if wort.gebeBezeichnung() == "oeffnen":
           self.wonderText.ergaenzeText ("Du " + str(wort.gebeEineAusgabeZurEingabe(self.eingabe)) + ".")
        else:
            geschwindigkeit = self.umgebung.gebeGeschwindigkeit(wort)        
        
            if "hoch" in self.eingabe:
                self.hoehe(geschwindigkeit)
            elif "runter" in self.eingabe:
                self.hoehe(- geschwindigkeit)
            else:
                self.hoehe(geschwindigkeit)
        
            self.wonderText.ergaenzeText ("Du " + str(wort.gebeEineAusgabeZurEingabe(self.eingabe)) + " nach " + self.richtungstext + ".")
        
        
