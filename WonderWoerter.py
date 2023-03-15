import random
from enum import Enum

class WortTyp(Enum):
    Flaeche = 1
    Ebene = 2
    Uebergang = 3
    Inventar = 4
    Blumenpflege = 5
    SpielBeenden = 6
    

class Wort(object):
    def __init__(self, bezeichnung, wortTyp: WortTyp):
        self.bezeichnung = bezeichnung
        self.wortTyp = wortTyp
        self.varianten = {} 
       
    def gebeVariantenZaehler(self):
        return len(self.varianten)
        
    def gebeBezeichnung(self):
        return self.bezeichnung

    def gebeWortTyp(self):
        return self.wortTyp

    def fuegeVarianteHinzu(self,eingabe, ausgabe):  ## ausgabe als Array   
        self.varianten[eingabe] =  ausgabe

    def gebeEineAusgabeZurEingabe (self,eingabe):
        for eingabeVariante in self.gebeAlleMoeglichenEingaben():
            if eingabeVariante in eingabe:
                return random.choice(self.varianten[eingabeVariante])
        
        return False
    
    def gebeAlleMoeglichenEingaben(self):
        return self.varianten.keys()  
           
class WortGeneratorSpielBeenden(object):
    def  __init__(self, wortTyp:WortTyp):
      self.__initialisiereSpielBeenden(wortTyp)
     
    def gebeWorte(self):
        return [self.wortBeenden]

    def __initialisiereSpielBeenden(self, wortTyp:WortTyp):
         self.wortBeenden = Wort("spielBeeenden", wortTyp )
         self.wortBeenden.fuegeVarianteHinzu("beenden",["beendest das Spiel"])
         self.wortBeenden.fuegeVarianteHinzu("ende", ["beendest das Spiel"])
         self.wortBeenden.fuegeVarianteHinzu("raus", ["beendest das Spiel"])

class WortGeneratorFlaeche(object):
    def  __init__(self, wortTyp:WortTyp):
      self.__initialisiereGehen(wortTyp)
      self.__initialisiereRennen(wortTyp)

    def gebeWorte(self):
        return [ self.wortGehen,  self.wortRennen]

    def __initialisiereGehen(self, wortTyp:WortTyp):
         self.wortGehen = Wort("gehen", wortTyp )
         self.wortGehen.fuegeVarianteHinzu("geh", ["gehst", "läufst", "schlenderst", "schleichst"])
         self.wortGehen.fuegeVarianteHinzu("lauf", ["gehst", "läufst", "marschierst"])
     

    def __initialisiereRennen(self, wortTyp:WortTyp):
         self.wortRennen = Wort("rennen", wortTyp)
         self.wortRennen.fuegeVarianteHinzu("eil", ["eilst", "hetzt", "jagest", "preschst" ])
         self.wortRennen.fuegeVarianteHinzu("renn", ["rennst", "joggst", "läufst schnell"])
       
class WortGeneratorEbene(object):
    def  __init__(self, wortTyp:WortTyp):
        self.__initialisiereSchwimmen(wortTyp)       
       
    def gebeWorte(self):
        return [ self.wortSchwimmen]
    
    def __initialisiereSchwimmen(self, wortTyp:WortTyp):
         self.wortSchwimmen = Wort("schwimmen", wortTyp)
         self.wortSchwimmen.fuegeVarianteHinzu("schwimm", ["schwimmst"])
   
       
class WortGeneratorUebergang(object):
    def  __init__(self, wortTyp:WortTyp):
        self.__initialisiereSpringen(wortTyp)
        self.__initialisiereTuereOeffnen(wortTyp)
    def gebeWorte(self):
        return [ self.wortSpringen,  self.wortOeffnen]

    def __initialisiereSpringen(self, wortTyp:WortTyp):
         self.wortSpringen = Wort("springen", wortTyp)
         self.wortSpringen.fuegeVarianteHinzu("spring", ["springst", "hüpst"])

    def __initialisiereTuereOeffnen(self, wortTyp:WortTyp):
         self.wortOeffnen = Wort("oeffnen", wortTyp)
         self.wortOeffnen.fuegeVarianteHinzu("öffne", ["öffnest die Türe"])
         self.wortOeffnen.fuegeVarianteHinzu("oeffne", ["öffnest die Türe"])
         self.wortOeffnen.fuegeVarianteHinzu("Tür", ["öffnest die Türe"])
         self.wortOeffnen.fuegeVarianteHinzu("Tuer", ["öffnest die Türe"])

class WortGeneratorBlumenpflege(object):
    def  __init__(self, wortTyp:WortTyp):   
        self.__initialisiereGieße (wortTyp)
        self.__initialisierePfluecke(wortTyp)
       
    def gebeWorte(self):
        return [ self.wortGießen,  self.wortPfluecken]
    
    def __initialisiereGieße(self, wortTyp:WortTyp):
         self.wortGießen = Wort("gießen", wortTyp)
         self.wortGießen.fuegeVarianteHinzu("gieß", ["gießt", "bewässerst" "versorgst"])
         self.wortGießen.fuegeVarianteHinzu("giess", ["gießt", "bewässerst" "versorgst"])
        
    def __initialisierePfluecke(self, wortTyp:WortTyp):
         self.wortPfluecken = Wort("pflücken", wortTyp)
         self.wortPfluecken.fuegeVarianteHinzu("pflück", ["pflückst", "entwendest", "entreisst"])
         self.wortPfluecken.fuegeVarianteHinzu("pflueck", ["pflückst", "entwendest", "entreisst"])

class WortGeneratorInventar(object):
    def  __init__(self, wortTyp:WortTyp):   
        self.__initialisiereSchaue (wortTyp)
        self.__initialisiereInventar(wortTyp)
        
    def gebeWorte(self):
        return [ self.wortSchauen,  self.wortInventar]    
    
    def __initialisiereSchaue(self, wortTyp:WortTyp):
         self.wortSchauen = Wort("schauen", wortTyp)
         self.wortSchauen.fuegeVarianteHinzu("schau", ["schaust ins Inventar und siehst ", "guckst ins Inventar und erblickst ", "blickst ins Inventar und begutachtest ","schaust in die Tasche und erkennst", "guckst in die Tasche und siehst " ,"blickst in die Tasche und erkennst ", "schaust in den Beutel und siehst ", "guckst in den Beutel und erkennst" ,"blickst in den Beutel und begutachtest"])
         self.wortSchauen.fuegeVarianteHinzu("guck", ["schaust ins Inventar und siehst ", "guckst ins Inventar und erblickst " ,"blickst ins Inventar und begutachtest ","schaust in die Tasche und erkennst", "guckst in die Tasche und siehst ", "blickst ind die Tasche und erkennst ", "schaust in den Beutel und siehst ", "guckst in den Beutel und erkennst" ,"blickst in den Beutel und begutachtest"])
         self.wortSchauen.fuegeVarianteHinzu("blick", ["schaust ins Inventar und siehst ", "guckst ins Inventar und erblickst ", "blickst ins Inventar und begutachtest ","schaust in die Tasche und erkennst", "guckst in die Tasche und siehst " ,"blickst ind die Tasche und erkennst ", "schaust in den Beutel und siehst ", "guckst in den Beutel und erkennst", "blickst in den Beutel und begutachtest"])
             
    def __initialisiereInventar(self, wortTyp:WortTyp):
         self.wortInventar = Wort("Inventar", wortTyp)
         self.wortInventar.fuegeVarianteHinzu("Inventar", ["schaust ins Inventar und siehst ", "guckst ins Inventar und erblickst " ,"blickst ins Inventar und begutachtest ","schaust in die Tasche und erkennst", "guckst in die Tasche und siehst " ,"blickst ind die Tasche und erkennst ", "schaust in den Beutel und siehst ", "guckst in den Beutel und erkennst" ,"blickst in den Beutel und begutachtest"])
         self.wortInventar.fuegeVarianteHinzu("Tasche",["schaust ins Inventar und siehst ", "guckst ins Inventar und erblickst ", "blickst ins Inventar und begutachtest ","schaust in die Tasche und erkennst", "guckst in die Tasche und siehst ", "blickst ind die Tasche und erkennst ", "schaust in den Beutel und siehst ", "guckst in den Beutel und erkennst" ,"blickst in den Beutel und begutachtest"])
         self.wortInventar.fuegeVarianteHinzu("Beutel",["schaust ins Inventar und siehst ", "guckst ins Inventar und erblickst ", "blickst ins Inventar und begutachtest ","schaust in die Tasche und erkennst", "guckst in die Tasche und siehst ", "blickst ind die Tasche und erkennst ", "schaust in den Beutel und siehst ", "guckst in den Beutel und erkennst" ,"blickst in den Beutel und begutachtest"])

class WortGeneratoren(object):
    def  __init__(self):
        self.flaechenWorte =  WortGeneratorFlaeche(WortTyp.Flaeche)
        self.ebenenWorte = WortGeneratorEbene(WortTyp.Ebene)
        self.uebergangWorte = WortGeneratorUebergang(WortTyp.Uebergang)
        self.blumenpflegeWorte = WortGeneratorBlumenpflege(WortTyp.Blumenpflege)
        self.inventarWorte = WortGeneratorInventar(WortTyp.Inventar)
        self.spielbeendenWorte =  WortGeneratorSpielBeenden(WortTyp.SpielBeenden)
        
    def gebeGeneratoren(self):
        yield self.flaechenWorte
        yield self.ebenenWorte
        yield self.uebergangWorte    
        yield self.blumenpflegeWorte
        yield self.inventarWorte
        yield self.spielbeendenWorte
        
class WortVergleicher(object):
    def  __init__(self):
         self.wortGeneratoren = WortGeneratoren()

    def vergleiche(self,eingabe):
        for WortGenerator in  self.wortGeneratoren.gebeGeneratoren():
            for WortGen in WortGenerator.gebeWorte():
                for Wort in WortGen.gebeAlleMoeglichenEingaben():
                    if Wort in eingabe:
                        return WortGen
        return None
    
    def gebeWort(self, bezeichnung):
        for WortGenerator in  self.wortGeneratoren.gebeGeneratoren():
            for Wort in WortGenerator.gebeWorte() :
                if  Wort.gebeBezeichnung() == bezeichnung:
                    return Wort
        return None