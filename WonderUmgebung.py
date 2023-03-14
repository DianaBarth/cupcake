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
        self.uebergangsworte = {}
        self.offsetworte = {}
        self.anschlussworte = {}
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

    def setzeUnterUndObereGrenze(self,unten, oben):
        self.unten = unten
        self.oben = oben

    def setzeOffset(self, offset):
        self.offset = offset
    
    def setzeGeschwindigkeit(self,wort, geschwindigkeit):
        if self.geschwindigkeiten.__contains__(wort.gebeBezeichnung()) == False:
            self.geschwindigkeiten[wort.gebeBezeichnung()] = geschwindigkeit 

    def entferneGeschwindigkeit(self,wort:Wort):
        if self.geschwindigkeiten.__contains__(wort.gebeBezeichnung()) == True:
            del self.geschwindigkeiten[wort.gebeBezeichnung()]
    
    def setzeGeschwindigkeitenFuerUebergang(self, typ):
        self.setzeGeschwindigkeit(self.uebergangsworte[typ],  self.uebergangsgeschwindigkeit[typ])
        self.setzeGeschwindigkeit(self.anschlussworte[typ],  self.anschlussgeschwindigkeit[typ])

    def entferneGeschwindigkeitenFuerUebergang(self, typ):
        self.entferneGeschwindigkeit(self.uebergangsworte[typ])
        self.entferneGeschwindigkeit(self.anschlussworte[typ])

    def setzeUebergang(self, typ, uebergangssatzGenau, uebergangssatzOffset,uebergangswortBezeichnung, uebergangsgeschwindigkeit, offsetwortBezeichung, anschlusswortBezeichnug, anschlussgeschwindigkeit, naechsteUmgebung):
        self.ueberganstypen.append (typ)
        self.uebergangssatzGenau[typ] = uebergangssatzGenau
        self.uebergangssatzOffset[typ] = uebergangssatzOffset
        self.uebergangsgeschwindigkeit[typ] = uebergangsgeschwindigkeit
        self.uebergangsworte[typ] = self.wortvergleicher.gebeWort(uebergangswortBezeichnung)
        self.offsetworte[typ] = self.wortvergleicher.gebeWort(offsetwortBezeichung)
        self.anschlussworte[typ] = self.wortvergleicher.gebeWort(anschlusswortBezeichnug)
        self.anschlussgeschwindigkeit[typ] = anschlussgeschwindigkeit
        self.naechsteUmgebung[typ] = naechsteUmgebung
    
    def gebeOffsetWort(self,typ):
        return self.offsetworte[typ]  

    def gebeUebergangsWort(self,typ):
        if self.uebergangsworte.__contains__(typ) == True:
            return self.uebergangsworte[typ]
        else:
            return None
        
    def gebeAnschlussWort(self,typ):
        if self.anschlussworte.__contains__(typ) == True:
            return self.anschlussworte[typ] 
        else:
            return None
        
    def gebeUebergangstypen(self):
        return self.ueberganstypen

    def gebeBezeichnung(self):      
        return self.bezeichung
    
    def gebeGeschwindigkeit(self,wort):   
        if self.geschwindigkeiten.__contains__(wort.gebeBezeichnung()) == True:
            return self.geschwindigkeiten[wort.gebeBezeichnung()]
        else:
            return 1

        
    
    def gebeStartBegrenzung(self):
        return self.startbegrenzung
    
    def gebeEndbegrenzung(self):
        return self.endbegrenzung
    
    def gebeWorte(self):
        return self.geschwindigkeiten.keys()
    
    def gebeUmgebungssatzFuerBlumen(self):
        return self.umgebungssatzFuerBlumen

    def gebeuebergangsworte(self, uebergangstyp):
        return self.uebergangsworte[uebergangstyp]
    
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
        elif userposition.gebeZ() == self.unten:
            return "unten angestoßen"
        elif userposition.gebeZ() == self.oben:
            return "oben angestoßen"   
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
        self.__initialisiereUniUmgebung(wortvergleicher)
    
        self.startUmgebung.setzeUebergang("ende",
            "Du stehst vor einem großen See. wenn Du willst, kannst Du jetzt ins Wasser springen und danach in alle Himmelsrichtunge und nach unten bzw. oben schwimmen.",
            "Du siehst in der Nähe einen großen See. Wenn Du willst, kannst Du jetzt ins Wasser springen und  und danach in alle Himmelsrichtunge und nach unten bzw. oben schwimmen.",
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
            "Du stehst direkt vor dem Eingang Deiner Universität. Wenn du willst, kannst Du die Türe öffnen und danach weiter gehen.",
            "Du siehst in der Nähe den Eingang zur Universität.  Wenn du willst, kannst Du die Türe öffnen und danach weiter gehen.",
             "oeffnen", 1, "gehen",  "gehen", 1,  self.uniUmgebung)                         
        
        self.uniUmgebung.setzeUebergang("start",
            "Du bist wieder vor der Türe zum Wald angekommen. Wenn Du willst kannst du die Türe öffnen und danach wieder gehen und rennen.",
            "Du bist fast wieder vor der Türe zum Wald angekommne. Wenn Du willst kannst du die Türe öffnen und danach wieder gehen und rennen.",
             "oeffnen", 1, "gehen",  "gehen", 1, self.waldUmgebung)

    def gebeStartUmgebung(self):
        return self.startUmgebung
    
    def gebeDoktormutterPosition(self):
        plusx = random.randint(self.grenzPositionWaldUni.gebeX(),self.grenzPositionUniEnde.gebeX()) 
        plusy = random.randint(self.grenzPositionWaldUni.gebeY(),self.grenzPositionUniEnde.gebeY()) 
        z = random.randint(self.grenzPositionWaldUni.gebeZ(),self.grenzPositionUniEnde.gebeZ()) 
        minusx = plusx*-1
        minusy = plusy*-1
        x = random.choice([plusx,minusx])
        y= random.choice([plusy, minusy])
        return Position(x,y,z)      

    def __initialisierePositionen(self):
        self.StartPosition = Position(0,0,0)
        self.grenzPositionStartWasser = Position(20,20,-1)
        self.grenzPositionWasserWald = Position(40,40,-1)
        self.grenzPositionWaldUni = Position (60,60,0)
        self.grenzPositionUniEnde = Position(70,70,0)
  
    def __initialisiereStartUmgebung(self,wortvergleicher):
        self.startUmgebung = Umgebung ("wiese","von der Wiese", self.StartPosition, self.grenzPositionStartWasser,wortvergleicher,0 )                                   
        self.startUmgebung.setzeGeschwindigkeit(self.wortvergleicher.gebeWort("gehen"),2)
        self.startUmgebung.setzeGeschwindigkeit(self.wortvergleicher.gebeWort("rennen"),4)
        self.startUmgebung.setzeOffset(2)
        self.startUmgebung.setzeUnterUndObereGrenze(-1,1)

    def __initialisiereWasserUmgebung(self,wortvergleicher):
        self.wasserUmgebung = Umgebung("wasser","aus dem Wasser",self.grenzPositionStartWasser, self.grenzPositionWasserWald,wortvergleicher,-8)
        self.wasserUmgebung.setzeGeschwindigkeit(self.wortvergleicher.gebeWort("schwimmen"),4)
        self.wasserUmgebung.setzeUnterUndObereGrenze(-8,0)

    def __initialisiereWaldUmgebung(self,wortvergleicher):
        self.waldUmgebung = Umgebung("wald","aus dem Wald", self.grenzPositionWasserWald,self.grenzPositionWaldUni,wortvergleicher,0)
        self.waldUmgebung.setzeGeschwindigkeit(self.wortvergleicher.gebeWort("gehen"), 1)
        self.waldUmgebung.setzeGeschwindigkeit(self.wortvergleicher.gebeWort("rennen"),2)
        self.waldUmgebung.setzeOffset(1)
        self.waldUmgebung.setzeUnterUndObereGrenze(-1,1)

    def __initialisiereUniUmgebung(self,wortvergleicher):
        self.uniUmgebung = Umgebung("Universität","", self.grenzPositionWaldUni,self.grenzPositionUniEnde,wortvergleicher,None)
        self.uniUmgebung.setzeGeschwindigkeit(self.wortvergleicher.gebeWort("gehen"), 1)
        self.uniUmgebung.setzeOffset(1)    
        self.uniUmgebung.setzeUnterUndObereGrenze(-1,1)