import random
from enum import Enum




class WonderText(object):
    def __init__(self):
          self.text = ""
    
    def setzeText(self,text):
        self.text = text

    def ergaenzeText(self,text):
         self.text = self.text + "\n" + text
       
    def druckeText(self):
         if self.text !="":
             print(self.text)
    
    def druckeAbschluss(self): 
        print("--------------------------------------")

    def druckeEingabeNichtErkannt(self,eingabe):
        print("Achtung, Eingabe '" + eingabe  +  "' nicht erkannt! Bitte versuche es erneut!")

class WonderBlume(object):
   
    def __init__(self, position, umgebung):
        self.text = ""
        self.groessen = ["winzige", "kleine", "mittelgroße", "große", "rießige"]
        self.position = position
        self.umgebungssatz = umgebung.gebeUmgebungssatz()
        self.groessenzahl = 1 
        self.hauptfarbe = random.choice(["rot", "gelbe", "blau"])
        self.unterfarbe = random.choice(["rosanen", "violetten", "purpurnen"])
        self.blattform = random.choice(["keinen", "runden", "stacheligen"])
        self.gepflueckt = False
    

    def gebePosition(self):
        return self.position

    def identifiziere(self):
        return self.groessen(self.groessenzahl) + " Blume mit " + self.hauptfarbe + "-" + self.unterfarbe + " Blüten und " + self.blattform + " Blättern " +  self.umgebungssatz
   
    def pruefegepflueckt(self):
         return self.gepflueckt
   
    def pfluecke(self):
        self.gepflueckt = True
        self.text = "du pflueckst die " + self.identifiziere + " und hast diese nun in deinem Inventar"
        return self.text

    def gieße(self):
        if self.groessenzahl < len(self.groessen):
            self.text = "du gießt die " + self.identifiziere + " und diese beginnt zu wachsen"
            self.groessenzahl = self.groessenzahl+1
        else:
            self.text = "du gießt die " + self.identifiziere + ", aber diese kann nicht weiter wachsen"
        return self.text
    
class BlumenSpawner(object):

    def __init__(self, umgebung, z):
        self.alleBlumen = [] 
        for x in range(umgebung.gebeStartBegrenzung().gebeX(), umgebung.gebeEndbegrenzung.gebeX() ):
            for y in  range(umgebung.gebeStartBegrenzung().gebeY(), umgebung.gebeEndbegrenzung.gebeY()):
                nordOst = Position(x,y,z)
                self.alleBlumen.append (WonderBlume(nordOst,umgebung))
                if x > 0:
                    nordWest = Position(-x,y,z)
                    self.alleBlumen.append (WonderBlume(nordWest,umgebung))
                if x!=y:
                    südOSt = Position(x,-y,z)
                    self.alleBlumen.append (WonderBlume(südOSt,umgebung))                  
                    if y > 0:
                        südWest = Position(-x,-y,z)
                        self.alleBlumen.append (WonderBlume(südWest,umgebung))  


    def gebeBlumeAnPosition(self, position):
        for blume in self.alleBlumen:
            if blume.gebePosition.gebeX() == position.gebeX() and blume.gebePosition.gebeY() == position.gebeY() and blume.gebePosition.gebeZ() == position.gebeZ():
                return blume 
class Bewegung(object):
    def __init__(self, startUmgebung, WonderText):
          self.WonderText = WonderText
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
                self.WonderText.druckeText()
                
            else:
                self.setzeEingabe(uebergangsVerb.gebeBezeichnung() + " " + vergleichsergebnis)             
                self.bewegeUebergang(uebergangsVerb)              
                self.setzeEingabe(anschlussVerb.gebeBezeichnung() + " " + vergleichsergebnis)                          
                self.bewegeEbene(anschlussVerb)                           
                self.umgebung.entferneGeschwindigkeitenFuerUebergang(uebergangstyp)
                self.WonderText.druckeText()
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
       
        if  self.uebergang == False:    
            verb = self.umgebung.vergleicheVerben(eingabe)
            if verb is None:
                self.WonderText.setzeText("Achtung,in diesem Gebiet (" + str(self.umgebung.gebeBezeichnung())+ ") kann man nicht " + bewegungsverb.gebeBezeichnung() + ".")
                
                if "kleineres" not in self.grenzTest:
                    self.WonderText.ergaenzeText ( self.umgebung.gebeUebergangssatz(self.grenzTest, self.uebergangstyp))                 
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
                    self.WonderText.ergaenzeText ( self.umgebung.gebeUebergangssatz(self.grenzTest, self.uebergangstyp))                  
                    self.uebergang = True
            else:
                ##Übergangsatz anzeigen
                self.WonderText.setzeText(self.umgebung.gebeUebergangssatz(self.grenzTest, self.uebergangstyp))
                self.uebergang = True

             ##Position am Ende angeben
            self.text = self.text +" \n" + self.position.gebePositionsAusgabe()

        elif self.uebergang == True:         
            if self.praktiziereUebergang(eingabe,bewegungsverb,self.grenzTest, self.uebergangstyp) == True:
                ##Übergang durchführen             
                self.umgebung = self.umgebung.gebeNaechsteUmgebung(self, self.uebergangstyp)
            
            self.WonderText.ergaenzeText (self.position.gebePositionsAusgabe())
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
        
        self.WonderText.setzeText ("Du " + verb.gebeEineAusgabeZurEingabe(self.eingabe) + " nach " + self.richtungstext + ".")
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
                
        self.WonderText.setzeText ("Du " + verb.gebeEineAusgabeZurEingabe(self.eingabe) + " nach " + self.richtungstext + "." )
        return True
    
    def bewegeUebergang(self, verb):
        geschwindigkeit = self.umgebung.gebeGeschwindigkeit(verb)
        
        if "hoch" in self.eingabe:
            self.hoehe(geschwindigkeit)
        elif "runter" in self.eingabe:
            self.hoehe(- geschwindigkeit)
        else:
            self.hoehe(geschwindigkeit)

        self.WonderText.setzeText ("Du " + str(verb.gebeEineAusgabeZurEingabe(self.eingabe)) + " nach " + self.richtungstext + ".")

class Position(object):
    def __init__(self,x,y,z):
        self.X = x
        self.Y = y
        self.Z = z        
    def ändereX(self,inkrement):
        self.X = self.X + inkrement       
    def ändereY(self,inkrement):
        self.Y = self.Y + inkrement        
    def ändereZ(self,inkrement):
        self.Z = self.Z + inkrement        
    def gebeX(self):
        return self.X
    def gebeY(self):
        return self.Y
    def gebeZ(self):
        return self.Z
    def gebePositionsAusgabe(self):
        return ("Du befindest dich an der Position " + str(self.gebeX()) + "." + str(self.gebeY()) + "." + str(self.gebeZ())) + "."

class Umgebung(object):
    
    def __init__(self, bezeichung,umgebungssatzFuerBlumen,  startbegrenzung, endbegrenzung, verbvergleicher, blumenhoehe):  

        self.verbvergleicher = verbvergleicher
        self.bezeichung =bezeichung
        self.umgebungssatzFuerBlumen = umgebungssatzFuerBlumen
        self.startbegrenzung = startbegrenzung
        self.endbegrenzung = endbegrenzung

        self.geschwindigkeiten = {}
               
        self.offset = 0
        self.naechsteUmgebung = None
        self.moeglicheEingaben = {}

        self.ueberganstypen = []
        self.uebergangssatzGenau = {}
        self.uebergangssatzOffset = {}
        self.uebergangsgeschwindigkeit = {}
        self.uebergangsVerb = {}
        self.offsetVerb = {}
        self.anschlussVerb = {}
        self.anschlussgeschwindigkeit = {}
        self.naechsteUmgebung = {}

        self.BlumenSpawner = BlumenSpawner(self, blumenhoehe)

    def gebeBlume(self, position):
       return self.BlumenSpawner.gebeBlumeAnPosition(position)

    def setzeBewegung(self, bewegung):
        self.bewegung = bewegung


    def setzeOffset(self, offset):
        self.offset = offset
    
    def setzeGeschwindigkeit(self, verb, geschwindigkeit):
        self.geschwindigkeiten[verb.gebeBezeichnung()] = geschwindigkeit 

    def entferneGeschwindigkeit(self,verb):
        del self.geschwindigkeiten[verb.gebeBezeichnung()]
    
    def setzeGeschwindigkeitenFuerUebergang(self, typ):
        self.setzeGeschwindigkeit(self.uebergangsVerb[typ],  self.uebergangsgeschwindigkeit[typ])
        self.setzeGeschwindigkeit(self.anschlussVerb[typ],  self.anschlussgeschwindigkeit[typ])

    def entferneGeschwindigkeitenFuerUebergang(self, typ):
        self.entferneGeschwindigkeit(self.uebergangsVerb[typ])
        self.entferneGeschwindigkeit(self.anschlussVerb[typ])

    def setzeUebergang(self, typ, uebergangssatzGenau, uebergangssatzOffset,uebergangsVerbBezeichnung, uebergangsgeschwindigkeit, offsetVerbBezeichung, anschlussVerbBezeichnug, anschlussgeschwindigkeit, naechsteUmgebung):
        self.ueberganstypen.append (typ)
        self.uebergangssatzGenau[typ] = uebergangssatzGenau
        self.uebergangssatzOffset[typ] = uebergangssatzOffset
        self.uebergangsgeschwindigkeit[typ] = uebergangsgeschwindigkeit
        self.uebergangsVerb[typ] = self.verbvergleicher.gebeVerb(uebergangsVerbBezeichnung)
        self.offsetVerb[typ] = self.verbvergleicher.gebeVerb(offsetVerbBezeichung)
        self.anschlussVerb[typ] = self.verbvergleicher.gebeVerb(anschlussVerbBezeichnug)
        self.anschlussgeschwindigkeit[typ] = anschlussgeschwindigkeit
        self.naechsteUmgebung[typ] = naechsteUmgebung
    
    def gebeOffsetVerb(self,typ):
        return self.offsetVerb[typ]  

    def gebeUebergangsVerb(self,typ):
        return self.uebergangsVerb[typ]
        
    def gebeAnschlussVerb(self,typ):
        return self.anschlussVerb[typ] 

    def gebeUebergangstypen(self):
        return self.ueberganstypen

    def gebeBezeichnung(self):      
        return self.bezeichung
    
    def gebeGeschwindigkeit(self, verb):   
        return self.geschwindigkeiten[verb.gebeBezeichnung()]
    
    def gebeStartBegrenzung(self):
        return self.startbegrenzung
    
    def gebeEndbegrenzung(self):
        return self.endbegrenzung
    
    def gebeVerben(self):
        return self.geschwindigkeiten.keys()
    
    def gebeUmgebungssatzFuerBlumen(self):
        return self.umgebungssatzFuerBlumen

    def gebeUebergangsVerb(self, uebergangstyp):
        return self.uebergangsVerb[uebergangstyp]
    
    def gebeUebergangssatz(self, vergleichsergebnis, uebergangstyp):
        if "offset" in vergleichsergebnis:
            return (self.uebergangssatzOffset[uebergangstyp])     
        else:
            return (self.uebergangssatzGenau[uebergangstyp])
    
    def gebeNaechsteUmgebung(self, bewegung, uebergangstyp):
         self.naechsteUmgebung[uebergangstyp].setzeBewegung(bewegung)
         return self.naechsteUmgebung[uebergangstyp]

    def vergleicheVerben(self,eingabe):
        for umgebungsVerbBezeichnung in self.gebeVerben():
           umgebungsverb = self.verbvergleicher.gebeVerb(umgebungsVerbBezeichnung)
           for verb in umgebungsverb.gebeAlleMoeglichenEingaben():
                if verb in eingabe:
                    return umgebungsverb
        return None

    def testeEndBegrenzung(self, userposition):
        if (userposition.gebeX() == self.endbegrenzung.gebeX()  and userposition.gebeY() == self.endbegrenzung.gebeY() ):
            return "genau nord-west oben" ## ecke
        elif (userposition.gebeX() == self.endbegrenzung.gebeX() - self.offset and userposition.gebeY() == self.endbegrenzung.gebeY() - self.offset):
            return "offset nord-west oben" ## ecke
        elif (userposition.gebeX() == self.endbegrenzung.gebeX() and userposition.gebeY() == - self.endbegrenzung.gebeY()):
            return "genau süd-west" ## ecke
        elif (userposition.gebeX() == self.endbegrenzung.gebeX() - self.offset and userposition.gebeY() == - self.endbegrenzung.gebeY() + self.offset):
            return "offset süd-west" ## ecke
        elif (userposition.gebeX() == - self.endbegrenzung.gebeX() and userposition.gebeY() == - self.endbegrenzung.gebeY()):
            return "genau süd-ost" ## ecke
        elif (userposition.gebeX() == - self.endbegrenzung.gebeX() + self.offset and userposition.gebeY() == - (self.endbegrenzung.gebeY()) + self.offset):
            return "offset süd-ost" ## ecke
        elif userposition.gebeX() == self.endbegrenzung.gebeX():
            return "genau ost"
        elif userposition.gebeX() == self.endbegrenzung.gebeX() - self.offset:
            return "offset ost"
        elif userposition.gebeX() == - self.endbegrenzung.gebeX():
            return "genau west"
        elif userposition.gebeX() == - self.endbegrenzung.gebeX() + self.offset:
            return "offset west"
        elif userposition.gebeY() == self.endbegrenzung.gebeY():
            return "genau nord"
        elif userposition.gebeY() == self.endbegrenzung.gebeY() - self.offset:
            return "offset nord"
        elif userposition.gebeY() == - self.endbegrenzung.gebeY():
            return "genau süd"
        elif userposition.gebeY() == - self.endbegrenzung.gebeY() + self.offset:
            return "offset süd"     
        else:
            return "kleineres" 
        
    def testeStartBegrenzung(self,userposition):
        if (userposition.gebeX() == self.startbegrenzung.gebeX()  and userposition.gebeY() == self.startbegrenzung.gebeY() ):
            return "genau süd-ost oben" ## ecke
        elif (userposition.gebeX() == self.startbegrenzung.gebeX() - self.offset and userposition.gebeY() == self.startbegrenzung.gebeY() - self.offset):
            return "offset süd-ost oben" ## ecke
        elif (userposition.gebeX() == self.startbegrenzung.gebeX() and userposition.gebeY() == - self.startbegrenzung.gebeY()):
            return "genau nord-ost" ## ecke
        elif (userposition.gebeX() == self.startbegrenzung.gebeX() - self.offset and userposition.gebeY() == - self.startbegrenzung.gebeY() + self.offset):
            return "offset nord-ost" ## ecke
        elif (userposition.gebeX() == - self.startbegrenzung.gebeX() and userposition.gebeY() == - self.startbegrenzung.gebeY()):
            return "genau nord-west" ## ecke
        elif (userposition.gebeX() == - self.startbegrenzung.gebeX() + self.offset and userposition.gebeY() == - (self.startbegrenzung.gebeY()) + self.offset):
            return "offset nord-west" ## ecke
        elif userposition.gebeX() == self.startbegrenzung.gebeX():
            return "genau west"
        elif userposition.gebeX() == self.startbegrenzung.gebeX() - self.offset:
            return "offset west"
        elif userposition.gebeX() == - self.startbegrenzung.gebeX():
            return "genau ost"
        elif userposition.gebeX() == - self.startbegrenzung.gebeX() + self.offset:
            return "offset ost"
        elif userposition.gebeY() == self.startbegrenzung.gebeY():
            return "genau süd"
        elif userposition.gebeY() == self.startbegrenzung.gebeY() - self.offset:
            return "offset süd"
        elif userposition.gebeY() == - self.startbegrenzung.gebeY():
            return "genau nord"
        elif userposition.gebeY() == - self.startbegrenzung.gebeY() + self.offset:
            return "offset nord"     
        else:
            return "kleineres" 
        
class UmgebungsGenerator:
    def __init__(self, verbvergleicher):
        self.verbvergleicher = verbvergleicher
   
        self.__initialisierePositionen()
        self.__initialisiereStartUmgebung(verbvergleicher)
        self.__initialisiereWasserUmgebung(verbvergleicher)
        self.__intiialiereWaldUmgebung(verbvergleicher)
    #    self.__initialisiereTreppeUmgebung(verbvergleicher)
    
    
        self.startUmgebung.setzeUebergang("ende",
            "Du stehst vor einem großen See. wenn Du willst, kannst Du jetzt ins Wasser springen und danach schwimmen.",
            "Du siehst in der Nähe einen großen See. Wenn Du willst, kannst Du jetzt ins Wasser springen und danach schwimmen.", 
            "springen", -1, "gehen","schwimmen", 4, self.wasserUmgebung)  
        
        self.wasserUmgebung.setzeUebergang("start",
            "Du stößt an das Ufer zum Startgebiet an. Wenn Du willst, kannst Du jetzt aus dem Wasser springen und danach weiter gehen oder rennen",
            "Du siehst in der Nähe das Ufer zum Startgebiet. Wenn Du willst, kannst Du jetzt aus dem Wasser springen und danach weiter gehen/rennen",
             "springen", 1, "schwimmen",  "gehen", 2,  self.startUmgebung)
        
        self.wasserUmgebung.setzeUebergang("ende",
            "Du stößt an das Ufer an. Dahinter siehst Du einen Wald. Wenn Du willst, kannst Du jetzt aus dem Wasser springen und danach weiter gehen oder rennen",
            "Du siehst in der Nähe das Ufer. Dahinter siehst Du einen Wald.  Wenn Du willst, kannst Du jetzt aus dem Wasser springen und danach weiter gehen/rennen",
             "springen", 1, "schwimmen",  "gehen", 1, self.waldUmgebung)

        self.waldUmgebung.setzeUebergang("start", "Du stehst vor einem großen See. wenn Du willst, kannst Du jetzt ins wasser springen und danach schwimmen.",
            "Du siehst in der Nähe einen großen See. Wenn Du willst, kannst Du jetzt ins wasser springen und danach schwimmen.", 
            "springen", -1, "gehen","schwimmen", 4, self.wasserUmgebung)  
                                         
        self.waldUmgebung.setzeUebergang("ende",
            "Du stehst direkt vor einer großen Treppe. Wenn du willst kannst du diese nun hochsteigen.",
            "Du siehst in der Nähe eine große Treppe. Wenn du willst kannst du diese nun hochsteigen.",
             "gehen", 1, "steigen",  "steigen", 1,  self.waldUmgebung)                         
                                         
    
    def gebeStartUmgebung(self):
        return self.startUmgebung

    def __initialisierePositionen(self):
        self.StartPosition = Position(0,0,0)
        self.grenzPositionStartWasser = Position(20,20,-1)
        self.grenzPositionWasserWald = Position(40,40,0)
        self.grenzPositionWaldTreppe = Position (60,60,10)
  
    def __initialisiereStartUmgebung(self,verbvergleicher):
        self.startUmgebung = Umgebung ("wiese","von der Wiese", self.StartPosition, self.grenzPositionStartWasser, verbvergleicher, 1 )                                   
        self.startUmgebung.setzeGeschwindigkeit(self.verbvergleicher.gebeVerb("gehen"),2)
        self.startUmgebung.setzeGeschwindigkeit(self.verbvergleicher.gebeVerb("rennen"),4)
        self.startUmgebung.setzeOffset(2)

    def __initialisiereWasserUmgebung(self,verbvergleicher):
        self.wasserUmgebung = Umgebung("wasser","aus dem Wasser",self.grenzPositionStartWasser, self.grenzPositionWasserWald,verbvergleicher)
        self.wasserUmgebung.setzeGeschwindigkeit(self.verbvergleicher.gebeVerb("schwimmen"),4)

    def __intiialiereWaldUmgebung(self,verbvergleicher):
        self.waldUmgebung = Umgebung("wald","aus dem Wald", self.grenzPositionWasserWald,self.grenzPositionWaldTreppe,verbvergleicher)
        self.waldUmgebung.setzeGeschwindigkeit(self.verbvergleicher.gebeVerb("gehen"), 1)
        self.waldUmgebung.setzeGeschwindigkeit(self.verbvergleicher.gebeVerb("rennen"),2)
        self.waldUmgebung.setzeOffset(1)



class VerbTyp(Enum):
    Flaeche = 1
    Ebene = 2
    Uebergang = 3
    Interaktion = 4
    Blumenpflege = 5

class Verb(object):
    def __init__(self, bezeichnung, verbtyp):
        self.bezeichnung = bezeichnung
        self.verbtyp = verbtyp
        self.varianten = {} 
       
    def gebeVariantenZaehler(self):
        return len(self.varianten)
        
    def gebeBezeichnung(self):
        return self.bezeichnung

    def gebeVerbtyp(self):
        return self.verbtyp

    def fuegeVarianteHinzu(self,eingabe, ausgabe):  ## ausgabe als Array   
        self.varianten[eingabe] =  ausgabe

    def gebeEineAusgabeZurEingabe (self,eingabe):
        for eingabeVariante in self.gebeAlleMoeglichenEingaben():
            if eingabeVariante in eingabe:
                return random.choice(self.varianten[eingabeVariante])
        
        return False
    
    def gebeAlleMoeglichenEingaben(self):
        return self.varianten.keys()  

class VerbVergleicher(object):
    def  __init__(self):
        self.verbGeneratoren = VerbGeneratoren()

    def vergleiche(self,eingabe):
        for verbGenerator in self.verbGeneratoren.gebeGeneratoren():
            for verbGen in verbGenerator.gebeVerben():
                for verb in verbGen.gebeAlleMoeglichenEingaben():
                    if verb in eingabe:
                        return verbGen
        return None
    
    def gebeVerb(self, bezeichnung):
        for verbGenerator in self.verbGeneratoren.gebeGeneratoren():
            for verb in verbGenerator.gebeVerben() :
                if  verb.gebeBezeichnung() == bezeichnung:
                    return verb
        return None
    
class VerbGeneratoren(object):
    def  __init__(self):
       self.flaechenVerben =  VerbGeneratorFlaeche(VerbTyp.Flaeche)
       self.ebenenVerben = VerbGeneratorEbene(VerbTyp.Ebene)
       self.uebergangVerben = VerbGeneratorUebergang(VerbTyp.Uebergang)
       self.interaktionsVerben = VerbGeneratorInteraktion(VerbTyp.Interaktion)
       self.blumenpflegeVerben = VerbGeneratorBlumenpflege(VerbTyp.Blumenpflege)
    
    def gebeGeneratoren(self):
       yield self.flaechenVerben
       yield self.ebenenVerben
       yield self.uebergangVerben    
       yield self.interaktionsVerben
       yield self.blumenpflegeVerben

class VerbGeneratorFlaeche(object):
    def  __init__(self,verbtyp):
      self.__initialisiereGehen(verbtyp)
      self.__initialisiereRennen(verbtyp)

    def gebeVerben(self):
        return [self.VerbGehen, self.VerbRennen]

    def __initialisiereGehen(self, verbtyp):
        self.VerbGehen = Verb("gehen", verbtyp )
        self.VerbGehen.fuegeVarianteHinzu("geh", ["gehst", "läufst", "schlenderst", "schleichst"])
        self.VerbGehen.fuegeVarianteHinzu("lauf", ["gehst", "läufst", "marschierst"])
     

    def __initialisiereRennen(self,verbtyp):
        self.VerbRennen = Verb("rennen", verbtyp)
        self.VerbRennen.fuegeVarianteHinzu("eil", ["eilst", "hetzt", "jagest", "preschst" ])
        self.VerbRennen.fuegeVarianteHinzu("renn", ["rennst", "joggst", "läufst schnell"])
       
class VerbGeneratorEbene(object):
    def  __init__(self, verbtyp):
        self.__initialisiereSchwimmen(verbtyp)
        self.__initialisiereFliegen(verbtyp)
        self.__initialisiereSteigen(verbtyp)
       
    def gebeVerben(self):
        return [self.VerbSchwimmen, self.VerbFliegen, self.VerbSteigen]
    
    def __initialisiereSchwimmen(self,verbtyp):
        self.VerbSchwimmen = Verb("schwimmen", verbtyp)
        self.VerbSchwimmen.fuegeVarianteHinzu("schwimm", ["schwimmst"])
    

    def __initialisiereFliegen(self,verbtyp):
        self.VerbFliegen = Verb("fliegen", verbtyp)
        self.VerbFliegen.fuegeVarianteHinzu("flieg", ["fliegst", "flatterst"])
       
    def __initialisiereSteigen(self, verbtyp):
        self.VerbSteigen = Verb("steigen", verbtyp)
        self.VerbSteigen.fuegeVarianteHinzu("steig", ["steigst die Treppe"])
       
class VerbGeneratorUebergang(object):
    def  __init__(self,verbtyp):
        self.__initialisiereSpringen(verbtyp)

    def gebeVerben(self):
        return [self.VerbSpringen]

    def __initialisiereSpringen(self, verbtyp):
        self.VerbSpringen = Verb("springen", verbtyp)
        self.VerbSpringen.fuegeVarianteHinzu("spring", ["springst", "hüpst"])
      
class VerbGeneratorInteraktion(object):
    def  __init__(self,verbtyp):
       # self.__initialisiereForsche(verbtyp)
        self.__initialisiereSprechen (verbtyp)
    
    def gebeVerben(self):
        return [self.VerbForschen, self.VerbSprechen]

   # def __initialisiereForsche(self, verbtyp):
   #     self.VerbForschen = Verb("forschen", verbtyp)
   #     self.VerbForschen.fuegeVarianteHinzu("forsch", ["forschst", "analysierst", "untersuchst"])
   #    self.VerbForschen.fuegeVarianteHinzu("analysiere", ["forschst", "analysierst", "untersuchst"])
   #    self.VerbForschen.fuegeVarianteHinzu("untersuch", ["forschst", "analysierst", "untersuchst"])
      

    def __initialisiereSprechen(self, verbtyp):
        self.VerbSprechen = Verb("sprechen", verbtyp)
        self.VerbSprechen.fuegeVarianteHinzu("sprech", ["sprichst", "redest"])
        self.VerbSprechen.fuegeVarianteHinzu("red", ["sprichst", "redest"])
             
class VerbGeneratorBlumenpflege(object):
    def  __init__(self,verbtyp):   
        self.__initialisiereGieße (verbtyp)
        self.__initialisierePfluecke(verbtyp)
       
    def gebeVerben(self):
        return [self.VerbForschen, self.VerbSprechen]
    
    def __initialisiereGieße(self, verbtyp):
        self.VerbGießen = Verb("gießen", verbtyp)
        self.VerbGießen.fuegeVarianteHinzu("gieß", ["gießt", "bewässerst" "versorgst"])
    
    def __initialisierePfluecke(self, verbtyp):
        self.VerbPfluecken = Verb("pflücken", verbtyp)
        self.VerbPfluecken.fuegeVarianteHinzu("pflücke", ["pflückst", "entwendest", "entreisst"])

        
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