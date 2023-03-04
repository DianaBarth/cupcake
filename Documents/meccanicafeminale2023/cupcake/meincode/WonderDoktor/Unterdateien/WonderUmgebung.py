from WonderBlumen import *

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
    
    def __init__(self, bezeichung,  startbegrenzung, endbegrenzung, verbvergleicher, blumenhoehe, umgebungssatzFuerBlumen):   
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
        self.startUmgebung = Umgebung ("wiese","von der Wiese", self.StartPosition, self.grenzPositionStartWasser, verbvergleicher  )                                   
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

