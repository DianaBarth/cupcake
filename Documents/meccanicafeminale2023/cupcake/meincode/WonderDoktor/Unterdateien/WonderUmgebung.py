
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
    
    def __init__(self, bezeichung,startbegrenzung, endbegrenzung, verbvergleicher):   
        self.verbvergleicher = verbvergleicher
        self.bezeichung =bezeichung
        self.startbegrenzung = startbegrenzung
        self.endbegrenzung = endbegrenzung
        self.geschwindigkeiten = {}
               
        self.offset = 0
        self.naechsteUmgebung = None
        self.moeglicheEingaben = {}

        self.uebergangssatzGenau = {}
        self.uebergangssatzOffset = {}
        self.uebergangsVerb = {}
        self.offsetVerb = {}
        self.anschlussVerb = {}
        self.naechsteUmgebung = {}

    def setzeBewegung(self, bewegung):
        self.bewegung = bewegung


    def setzeOffset(self, offset):
        self.offset = offset
    
    def setzeGeschwindigkeit(self, verb, geschwindigkeit):
        self.geschwindigkeiten[verb.gebeBezeichnung()] = geschwindigkeit 
    
    def setzeUebergang(self, typ, uebergangssatzGenau, uebergangssatzOffset,uebergangsVerbBezeichnung, offsetVerbBezeichung, anschlussVerbBezeichnug, naechsteUmgebung):
        self.uebergangssatzGenau[typ] = uebergangssatzGenau
        self.uebergangssatzOffset[typ] = uebergangssatzOffset
        self.uebergangsVerb[typ] = self.verbvergleicher.gebeVerb(uebergangsVerbBezeichnung)
        self.offsetVerb[typ] = self.verbvergleicher.gebeVerb(offsetVerbBezeichung)
        self.anschlussVerb[typ] = self.verbvergleicher.gebeVerb(anschlussVerbBezeichnug)
        self.naechsteUmgebung[typ] = naechsteUmgebung
    
    def gebeBezeichnung(self):      
        return self.bezeichung
    
    def gebeGeschwindigkeit(self, verb):   
        return self.geschwindigkeiten[verb.gebeBezeichnung()]
    
    def gebeStartBegrenzung(self):
        return self.startbegrenzung

    def gebeVerben(self):
        return self.geschwindigkeiten.keys()

    def gebeWechselverb(self):
        return self.wechselVerb
    
    def gebeUebergangssatz(self, vergleichsergebnis):
        if "offset" in vergleichsergebnis:
            print(self.uebergangssatzOffset)     
        else:
            print(self.uebergangssatzGenau)
    
    def gebeNaechsteUmgebung(self):
         return self.naechsteUmgebung 

    def pruefeUebergang(self, benutzereingabe, benutzerverb, vergleichsergebnis, uebergangstyp):

        if self.uebergangsVerb[uebergangstyp].gebeBezeichung() ==  benutzerverb.gebeBezeichung():  
            if "offset" in vergleichsergebnis:
                self.bewegung.bewegeEbene(self.offsetVerb[uebergangstyp])
                self.bewegung.druckeText()
                self.bewegung.bewegeUebergang(self.uebergangsVerb[uebergangstyp])
                self.bewegung.druckeText()             
                self.bewegung.bewegeEbene(self.anschlussVerb[uebergangstyp])
                self.bewegung.druckeText()
            else:
                self.bewegung.bewegeUebergang(self.uebergangsVerb[uebergangstyp])
                self.bewegung.druckeText()
                self.bewegung.bewegeEbene(self.anschlussVerb[uebergangstyp])
                self.bewegung.druckeText()
            return True
        else:
            if "nord" in vergleichsergebnis and "nord" in benutzereingabe   :
                print("Du kannst nicht nach Norden " + self.benutzerverb.gebeBezeichnung() + ".")
                self.gebeUebergangssatz(vergleichsergebnis)
            elif "ost" in vergleichsergebnis and "ost" in benutzereingabe:
                print("Du kannst nicht nach Osten " + self.benutzerverb.gebeBezeichnung() + ".")
                self.gebeUebergangssatz(vergleichsergebnis)
            elif "süd" in vergleichsergebnis and "süd" in benutzereingabe:
                print("Du kannst nicht nach Süden " + self.benutzerverb.gebeBezeichnung() + ".")
                self.gebeUebergangssatz(vergleichsergebnis)
            elif "west" in vergleichsergebnis and "west" in benutzereingabe:
                print("Du kannst nicht ach Westen " + self.benutzerverb.gebeBezeichnung() + ".")
                self.gebeUebergangssatz(vergleichsergebnis)
            else:  
                 self.bewegung.bewegeEbene(benutzerverb)

            return False
            
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
            "Du stehst vor einem großen See. wenn Du willst, kannst Du jetzt ins wasser springen und danach schwimmen.",
            "Du siehst in der Nähe einen großen See. Wenn Du willst, kannst Du jetzt ins wasser springen und danach schwimmen.", 
            "springen","gehen","schwimmen", self.wasserUmgebung)  
        
        self.wasserUmgebung.setzeUebergang("start",
            "Du stößt an das Ufer zum Startgebiet an. Wenn Du willst, kannst Du jetzt aus dem Wasser springen und danach weiter gehen oder rennen",
            "Du siehst in der Nähe das Ufer zum Startgebiet. Wenn Du willst, kannst Du jetzt aus dem Wasser springen und danach weiter gehen/rennen",
             "springen", "schwimmen",  "gehen",  self.startUmgebung)
        
        self.wasserUmgebung.setzeUebergang("ende",
            "Du stößt an das Ufer an. Dahinter siehst Du einen Wald. Wenn Du willst, kannst Du jetzt aus dem Wasser springen und danach weiter gehen oder rennen",
            "Du siehst in der Nähe das Ufer. Dahinter siehst Du einen Wald.  Wenn Du willst, kannst Du jetzt aus dem Wasser springen und danach weiter gehen/rennen",
             "springen", "schwimmen",  "gehen",  self.waldUmgebung)

        self.waldUmgebung.setzeUebergang("start", "Du stehst vor einem großen See. wenn Du willst, kannst Du jetzt ins wasser springen und danach schwimmen.",
            "Du siehst in der Nähe einen großen See. Wenn Du willst, kannst Du jetzt ins wasser springen und danach schwimmen.", 
            "springen","gehen","schwimmen", self.wasserUmgebung)  
                                         
        self.waldUmgebung.setzeUebergang("ende",
            "Du stehst direkt vor einer großen Treppe. Wenn du willst kannst du diese nun hochsteigen.",
            "Du siehst in der Nähe eine große Treppe. Wenn du willst kannst du diese nun hochsteigen.",
             "steigen", "steigen",  "steigen",  self.waldUmgebung)                         
                                         
    
    def gebeStartUmgebung(self):
        return self.startUmgebung

    def __initialisierePositionen(self):
        self.grenzStartPosition = Position(0,0,0)
        self.grenzPositionStartWasser = Position(12,12,-1)
        self.grenzPositionWasserWald = Position(40,40,0)
        self.grenzPositionWaldTreppe = Position (50,50,10)
  
    def __initialisiereStartUmgebung(self,verbvergleicher):
        self.startUmgebung = Umgebung ("start",self.grenzStartPosition, self.grenzPositionStartWasser, verbvergleicher   )                                   
        self.startUmgebung.setzeGeschwindigkeit(self.verbvergleicher.gebeVerb("gehen"),2)
        self.startUmgebung.setzeGeschwindigkeit(self.verbvergleicher.gebeVerb("rennen"),4)
        self.startUmgebung.setzeOffset(2)

    def __initialisiereWasserUmgebung(self,verbvergleicher):
        self.wasserUmgebung = Umgebung("wasser",self.grenzPositionStartWasser, self.grenzPositionWasserWald,verbvergleicher)
        self.wasserUmgebung.setzeGeschwindigkeit(self.verbvergleicher.gebeVerb("schwimmen"),4)

    def __intiialiereWaldUmgebung(self,verbvergleicher):
        self.waldUmgebung = Umgebung("wald",self.grenzPositionWasserWald,self.grenzPositionWaldTreppe,verbvergleicher)
        self.waldUmgebung.setzeGeschwindigkeit(self.verbvergleicher.gebeVerb("gehen"), 1)
        self.waldUmgebung.setzeGeschwindigkeit(self.verbvergleicher.gebeVerb("rennen"),2)
        self.waldUmgebung.setzeOffset(1)

