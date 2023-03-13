from WonderBlumen import *
from WonderPosition import Position
from WonderWoerter import WortVergleicher

class Umgebung(object):
    
    def __init__(self, bezeichung,umgebungssatzFuerBlumen, startbegrenzung:Position, endbegrenzung:Position, Wortvergleicher:WortVergleicher, blumenhoehe):  

        self.Wortvergleicher = Wortvergleicher
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
        self.uebergangsWort = {}
        self.offsetWort = {}
        self.anschlussWort = {}
        self.anschlussgeschwindigkeit = {}
        self.naechsteUmgebung = {}

        if blumenhoehe is not None:
            self.blumenSpawner = BlumenSpawner(self.startbegrenzung, self.endbegrenzung,blumenhoehe, self.umgebungssatzFuerBlumen)

    def gebeBlume(self, position:Position)->WonderBlume:
        return self.blumenSpawner.gebeBlumeAnPosition(position)
     

    def setzeBewegung(self, bewegung):
        self.bewegung = bewegung


    def setzeOffset(self, offset):
        self.offset = offset
    
    def setzeGeschwindigkeit(self, Wort, geschwindigkeit):
        self.geschwindigkeiten[Wort.gebeBezeichnung()] = geschwindigkeit 

    def entferneGeschwindigkeit(self,Wort):
        del self.geschwindigkeiten[Wort.gebeBezeichnung()]
    
    def setzeGeschwindigkeitenFuerUebergang(self, typ):
        self.setzeGeschwindigkeit(self.uebergangsWort[typ],  self.uebergangsgeschwindigkeit[typ])
        self.setzeGeschwindigkeit(self.anschlussWort[typ],  self.anschlussgeschwindigkeit[typ])

    def entferneGeschwindigkeitenFuerUebergang(self, typ):
        self.entferneGeschwindigkeit(self.uebergangsWort[typ])
        self.entferneGeschwindigkeit(self.anschlussWort[typ])

    def setzeUebergang(self, typ, uebergangssatzGenau, uebergangssatzOffset,uebergangsWortBezeichnung, uebergangsgeschwindigkeit, offsetWortBezeichung, anschlussWortBezeichnug, anschlussgeschwindigkeit, naechsteUmgebung):
        self.ueberganstypen.append (typ)
        self.uebergangssatzGenau[typ] = uebergangssatzGenau
        self.uebergangssatzOffset[typ] = uebergangssatzOffset
        self.uebergangsgeschwindigkeit[typ] = uebergangsgeschwindigkeit
        self.uebergangsWort[typ] = self.Wortvergleicher.gebeWort(uebergangsWortBezeichnung)
        self.offsetWort[typ] = self.Wortvergleicher.gebeWort(offsetWortBezeichung)
        self.anschlussWort[typ] = self.Wortvergleicher.gebeWort(anschlussWortBezeichnug)
        self.anschlussgeschwindigkeit[typ] = anschlussgeschwindigkeit
        self.naechsteUmgebung[typ] = naechsteUmgebung
    
    def gebeOffsetWort(self,typ):
        return self.offsetWort[typ]  

    def gebeUebergangsWort(self,typ):
        return self.uebergangsWort[typ]
        
    def gebeAnschlussWort(self,typ):
        return self.anschlussWort[typ] 

    def gebeUebergangstypen(self):
        return self.ueberganstypen

    def gebeBezeichnung(self):      
        return self.bezeichung
    
    def gebeGeschwindigkeit(self, Wort):   
        return self.geschwindigkeiten[Wort.gebeBezeichnung()]
    
    def gebeStartBegrenzung(self):
        return self.startbegrenzung
    
    def gebeEndbegrenzung(self):
        return self.endbegrenzung
    
    def gebeWorte(self):
        return self.geschwindigkeiten.keys()
    
    def gebeUmgebungssatzFuerBlumen(self):
        return self.umgebungssatzFuerBlumen

    def gebeUebergangsWort(self, uebergangstyp):
        return self.uebergangsWort[uebergangstyp]
    
    def gebeUebergangssatz(self, vergleichsergebnis, uebergangstyp):
        if "offset" in vergleichsergebnis:
            return (self.uebergangssatzOffset[uebergangstyp])     
        else:
            return (self.uebergangssatzGenau[uebergangstyp])
    
    def gebeNaechsteUmgebung(self, bewegung, uebergangstyp):
         self.naechsteUmgebung[uebergangstyp].setzeBewegung(bewegung)
         return self.naechsteUmgebung[uebergangstyp]

    def vergleicheWorte(self,eingabe):
        for umgebungsWortBezeichnung in self.gebeWorte():
           umgebungsWort = self.Wortvergleicher.gebeWort(umgebungsWortBezeichnung)
           for Wort in umgebungsWort.gebeAlleMoeglichenEingaben():
                if Wort in eingabe:
                    return umgebungsWort
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
    def __init__(self, Wortvergleicher):
        self.Wortvergleicher = Wortvergleicher
   
        self.__initialisierePositionen()
        self.__initialisiereStartUmgebung(Wortvergleicher)
        self.__initialisiereWasserUmgebung(Wortvergleicher)
        self.__initialisiereWaldUmgebung(Wortvergleicher)
        self.__initialisiereTreppeUmgebung(Wortvergleicher)
        self.__initialisiereUniUmgebung(Wortvergleicher)
    
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
        
        self.treppeUmgebung.setzeUebergang("start",
            "Du bist am Fuß der Treppe angekommen, und bist wieder im Wald. Hier kannst du wieder gehen oder rennen.",
            "Du bist fast am Fuß der Treppe angekommen, und bist wieder im Wald. Hier kannst du wieder gehen oder rennen.",
             "gehen", 1, "steigen",  "gehen", 1, self.waldUmgebung)

        self.treppeUmgebung.setzeUebergang("ende",                                            
            "Du sehst nun direkt vor dem Universitätsgebäude. Hier kannst du nur gehen. Suche Deine Doktormutter!",
            "Du sehst nun fast direkt vor dem Universitätsgebäude. Hier kannst du nur gehen. Suche Deine Doktormutter!"
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
        x = random.choice(plusx,minusx)
        y= random.choice(plusy, minusy)
        return Position(x,y,z)      

    def __initialisierePositionen(self):
        self.StartPosition = Position(0,0,0)
        self.grenzPositionStartWasser = Position(10,10,-1)
        self.grenzPositionWasserWald = Position(20,20,0)
        self.grenzPositionWaldTreppe = Position (30,30,0)
        self.grenzPositionTreppeUni = Position(40,40,10)
        self.grenzPositionUniEnde = Position(50,50,10)
  
    def __initialisiereStartUmgebung(self,Wortvergleicher):
        self.startUmgebung = Umgebung ("wiese","von der Wiese", self.StartPosition, self.grenzPositionStartWasser, Wortvergleicher,0 )                                   
        self.startUmgebung.setzeGeschwindigkeit(self.Wortvergleicher.gebeWort("gehen"),2)
        self.startUmgebung.setzeGeschwindigkeit(self.Wortvergleicher.gebeWort("rennen"),4)
        self.startUmgebung.setzeOffset(2)

    def __initialisiereWasserUmgebung(self,Wortvergleicher):
        self.wasserUmgebung = Umgebung("wasser","aus dem Wasser",self.grenzPositionStartWasser, self.grenzPositionWasserWald,Wortvergleicher,-5)
        self.wasserUmgebung.setzeGeschwindigkeit(self.Wortvergleicher.gebeWort("schwimmen"),4)

    def __initialisiereWaldUmgebung(self,Wortvergleicher):
        self.waldUmgebung = Umgebung("wald","aus dem Wald", self.grenzPositionWasserWald,self.grenzPositionWaldTreppe,Wortvergleicher,0)
        self.waldUmgebung.setzeGeschwindigkeit(self.Wortvergleicher.gebeWort("gehen"), 1)
        self.waldUmgebung.setzeGeschwindigkeit(self.Wortvergleicher.gebeWort("rennen"),2)
        self.waldUmgebung.setzeOffset(1)

    def __initialisiereTreppeUmgebung(self,Wortvergleicher):
        self.treppeUmgebung = Umgebung("Treppe","", self.grenzPositionWaldTreppe,self.grenzPositionTreppeUni,Wortvergleicher,None)
        self.treppeUmgebung.setzeGeschwindigkeit(self.Wortvergleicher.gebeWort("steigen"), 1)
        self.treppeUmgebung.setzeOffset(1)

    def __initialisiereUniUmgebung(self,Wortvergleicher):
        self.uniUmgebung = Umgebung("Treppe","", self.grenzPositionTreppeUni,self.grenzPositionUniEnde,Wortvergleicher,None)
        self.uniUmgebung.setzeGeschwindigkeit(self.Wortvergleicher.gebeWort("gehen"), 1)
        self.uniUmgebung.setzeOffset(1)