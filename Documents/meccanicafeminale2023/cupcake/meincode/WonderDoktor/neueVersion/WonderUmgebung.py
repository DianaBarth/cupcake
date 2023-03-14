from WonderBlumen import *
from WonderPosition import *
from WonderWoerter import *

class Umgebung(object):
    
    def __init__(self, bezeichung,umgebungssatzFuerBlumen, startbegrenzung:Position, endbegrenzung:Position,wortvergleicher:WortVergleicher, blumenhoehe):  

        self.wortvergleicher =wortvergleicher
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
        self.uebergangswort = {}
        self.offsetwort = {}
        self.anschlusswort = {}
        self.anschlussgeschwindigkeit = {}
        self.naechsteUmgebung = {}
        self.blumenhoehe = blumenhoehe
        if blumenhoehe is not None:
            self.blumenSpawner = BlumenSpawner(self.startbegrenzung, self.endbegrenzung,blumenhoehe, self.umgebungssatzFuerBlumen)

    def gebeBlume(self, position:Position)->WonderBlume:
        if self.blumenhoehe is not None:
            return self.blumenSpawner.gebeBlumeAnPosition(position)
        else:
            return None

    def setzeBewegung(self, bewegung):
        self.bewegung = bewegung


    def setzeOffset(self, offset):
        self.offset = offset
    
    def setzeGeschwindigkeit(self,wort, geschwindigkeit):
        if self.geschwindigkeiten.__contains__(wort.gebeBezeichnung()) == False:
            self.geschwindigkeiten[wort.gebeBezeichnung()] = geschwindigkeit 

    def entferneGeschwindigkeit(self,wort:Wort):
        if self.geschwindigkeiten.__contains__(wort.gebeBezeichnung()) == True:
            del self.geschwindigkeiten[wort.gebeBezeichnung()]
    
    def setzeGeschwindigkeitenFuerUebergang(self, typ):
        self.setzeGeschwindigkeit(self.uebergangswort[typ],  self.uebergangsgeschwindigkeit[typ])
        self.setzeGeschwindigkeit(self.anschlusswort[typ],  self.anschlussgeschwindigkeit[typ])

    def entferneGeschwindigkeitenFuerUebergang(self, typ):
        self.entferneGeschwindigkeit(self.uebergangswort[typ])
        self.entferneGeschwindigkeit(self.anschlusswort[typ])

    def setzeUebergang(self, typ, uebergangssatzGenau, uebergangssatzOffset,uebergangswortBezeichnung, uebergangsgeschwindigkeit, offsetwortBezeichung, anschlusswortBezeichnug, anschlussgeschwindigkeit, naechsteUmgebung):
        self.ueberganstypen.append (typ)
        self.uebergangssatzGenau[typ] = uebergangssatzGenau
        self.uebergangssatzOffset[typ] = uebergangssatzOffset
        self.uebergangsgeschwindigkeit[typ] = uebergangsgeschwindigkeit
        self.uebergangswort[typ] = self.wortvergleicher.gebeWort(uebergangswortBezeichnung)
        self.offsetwort[typ] = self.wortvergleicher.gebeWort(offsetwortBezeichung)
        self.anschlusswort[typ] = self.wortvergleicher.gebeWort(anschlusswortBezeichnug)
        self.anschlussgeschwindigkeit[typ] = anschlussgeschwindigkeit
        self.naechsteUmgebung[typ] = naechsteUmgebung
    
    def gebeOffsetWort(self,typ):
        return self.offsetwort[typ]  

    def gebeUebergangswort(self,typ):
        return self.uebergangswort[typ]
        
    def gebeAnschlussWort(self,typ):
        return self.anschlusswort[typ] 

    def gebeUebergangstypen(self):
        return self.ueberganstypen

    def gebeBezeichnung(self):      
        return self.bezeichung
    
    def gebeGeschwindigkeit(self,wort):   
        return self.geschwindigkeiten[wort.gebeBezeichnung()]
    
    def gebeStartBegrenzung(self):
        return self.startbegrenzung
    
    def gebeEndbegrenzung(self):
        return self.endbegrenzung
    
    def gebeWorte(self):
        return self.geschwindigkeiten.keys()
    
    def gebeUmgebungssatzFuerBlumen(self):
        return self.umgebungssatzFuerBlumen

    def gebeUebergangsWort(self, uebergangstyp):
        return self.uebergangswort[uebergangstyp]
    
    def gebeUebergangssatz(self, vergleichsergebnis, uebergangstyp):
        if "offset" in vergleichsergebnis:
            return (self.uebergangssatzOffset[uebergangstyp])     
        else:
            return (self.uebergangssatzGenau[uebergangstyp])
    
    def gebeNaechsteUmgebung(self, bewegung, uebergangstyp):
         self.naechsteUmgebung[uebergangstyp].setzeBewegung(bewegung)
         return self.naechsteUmgebung[uebergangstyp]

    def vergleicheWorte(self,eingabe):
        for umgebungswortBezeichnung in self.gebeWorte():
           umgebungswort = self.wortvergleicher.gebeWort(umgebungswortBezeichnung)
           for wort in umgebungswort.gebeAlleMoeglichenEingaben():
                if wort in eingabe:
                    return umgebungswort
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
    def __init__(self,wortvergleicher):
        self.wortvergleicher =wortvergleicher
   
        self.__initialisierePositionen()
        self.__initialisiereStartUmgebung(wortvergleicher)
        self.__initialisiereWasserUmgebung(wortvergleicher)
        self.__initialisiereWaldUmgebung(wortvergleicher)
        self.__initialisiereTreppeUmgebung(wortvergleicher)
        self.__initialisiereUniUmgebung(wortvergleicher)
    
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
             "steigen", 1, "steigen",  "steigen", 1,  self.treppeUmgebung)                         
        
        self.treppeUmgebung.setzeUebergang("start",
            "Du bist am Fuß der Treppe angekommen, und bist wieder im Wald. Hier kannst du wieder gehen oder rennen.",
            "Du bist fast am Fuß der Treppe angekommen, und bist wieder im Wald. Hier kannst du wieder gehen oder rennen.",
             "gehen", 1, "steigen",  "gehen", 1, self.waldUmgebung)

        self.treppeUmgebung.setzeUebergang("ende",                                            
            "Du sehst nun direkt vor dem Universitätsgebäude. Hier kannst du nur gehen. Suche Deine Doktormutter!",
            "Du sehst nun fast direkt vor dem Universitätsgebäude. Hier kannst du nur gehen. Suche Deine Doktormutter!",
             "gehen", 1, "steigen",  "gehen", 1, self.uniUmgebung)
        
        self.uniUmgebung.setzeUebergang("start",
            "Du bist wieder der Treppe angekommen und kannst diese hinunter steigen.",
            "Du bist fast wieder der Treppe angekommen und kannst diese hinunter steigen.",
             "gehen", 1, "gehen",  "steigen", 1, self.treppeUmgebung)

    def gebeStartUmgebung(self):
        return self.startUmgebung
    
    def gebeDoktormutterPosition(self):
        plusx = random.randint(self.grenzPositionTreppeUni.gebeX(),self.grenzPositionUniEnde.gebeX()) 
        plusy = random.randint(self.grenzPositionTreppeUni.gebeY(),self.grenzPositionUniEnde.gebeY()) 
        z = random.randint(self.grenzPositionTreppeUni.gebeZ(),self.grenzPositionUniEnde.gebeZ()) 
        minusx = plusx*-1
        minusy = plusy*-1
        x = random.choice([plusx,minusx])
        y= random.choice([plusy, minusy])
        return Position(x,y,z)      

    def __initialisierePositionen(self):
        self.StartPosition = Position(0,0,0)
        self.grenzPositionStartWasser = Position(20,20,-1)
        self.grenzPositionWasserWald = Position(40,40,-1)
        self.grenzPositionWaldTreppe = Position (60,60,0)
        self.grenzPositionTreppeUni = Position(80,80,10)
        self.grenzPositionUniEnde = Position(100,100,10)
  
    def __initialisiereStartUmgebung(self,wortvergleicher):
        self.startUmgebung = Umgebung ("wiese","von der Wiese", self.StartPosition, self.grenzPositionStartWasser,wortvergleicher,0 )                                   
        self.startUmgebung.setzeGeschwindigkeit(self.wortvergleicher.gebeWort("gehen"),2)
        self.startUmgebung.setzeGeschwindigkeit(self.wortvergleicher.gebeWort("rennen"),4)
        self.startUmgebung.setzeOffset(2)

    def __initialisiereWasserUmgebung(self,wortvergleicher):
        self.wasserUmgebung = Umgebung("wasser","aus dem Wasser",self.grenzPositionStartWasser, self.grenzPositionWasserWald,wortvergleicher,-5)
        self.wasserUmgebung.setzeGeschwindigkeit(self.wortvergleicher.gebeWort("schwimmen"),4)

    def __initialisiereWaldUmgebung(self,wortvergleicher):
        self.waldUmgebung = Umgebung("wald","aus dem Wald", self.grenzPositionWasserWald,self.grenzPositionWaldTreppe,wortvergleicher,0)
        self.waldUmgebung.setzeGeschwindigkeit(self.wortvergleicher.gebeWort("gehen"), 1)
        self.waldUmgebung.setzeGeschwindigkeit(self.wortvergleicher.gebeWort("rennen"),2)
        self.waldUmgebung.setzeOffset(1)

    def __initialisiereTreppeUmgebung(self,wortvergleicher):
        self.treppeUmgebung = Umgebung("Treppe","", self.grenzPositionWaldTreppe,self.grenzPositionTreppeUni,wortvergleicher,None)
        self.treppeUmgebung.setzeGeschwindigkeit(self.wortvergleicher.gebeWort("steigen"), 1)
        self.treppeUmgebung.setzeOffset(1)

    def __initialisiereUniUmgebung(self,wortvergleicher):
        self.uniUmgebung = Umgebung("Treppe","", self.grenzPositionTreppeUni,self.grenzPositionUniEnde,wortvergleicher,None)
        self.uniUmgebung.setzeGeschwindigkeit(self.wortvergleicher.gebeWort("gehen"), 1)
        self.uniUmgebung.setzeOffset(1)