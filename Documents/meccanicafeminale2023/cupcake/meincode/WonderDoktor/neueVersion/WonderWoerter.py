import random
from enum import Enum

class WortTyp(Enum):
    Flaeche = 1
    Ebene = 2
    Uebergang = 3
    Inventar = 4
    Blumenpflege = 5
    

class Wort(object):
    def __init__(self, bezeichnung, WortTyp):
        self.bezeichnung = bezeichnung
        self.WortTyp = WortTyp
        self.varianten = {} 
       
    def gebeVariantenZaehler(self):
        return len(self.varianten)
        
    def gebeBezeichnung(self):
        return self.bezeichnung

    def gebeWortTyp(self):
        return self.WortTyp

    def fuegeVarianteHinzu(self,eingabe, ausgabe):  ## ausgabe als Array   
        self.varianten[eingabe] =  ausgabe

    def gebeEineAusgabeZurEingabe (self,eingabe):
        for eingabeVariante in self.gebeAlleMoeglichenEingaben():
            if eingabeVariante in eingabe:
                return random.choice(self.varianten[eingabeVariante])
        
        return False
    
    def gebeAlleMoeglichenEingaben(self):
        return self.varianten.keys()  
    
        
  
class WortGeneratorFlaeche(object):
    def  __init__(self,WortTyp):
      self.__initialisiereGehen(WortTyp)
      self.__initialisiereRennen(WortTyp)

    def gebeWorte(self):
        return [self.WortGehen, self.WortRennen]

    def __initialisiereGehen(self, WortTyp):
        self.WortGehen = Wort("gehen", WortTyp )
        self.WortGehen.fuegeVarianteHinzu("geh", ["gehst", "läufst", "schlenderst", "schleichst"])
        self.WortGehen.fuegeVarianteHinzu("lauf", ["gehst", "läufst", "marschierst"])
     

    def __initialisiereRennen(self,WortTyp):
        self.WortRennen = Wort("rennen", WortTyp)
        self.WortRennen.fuegeVarianteHinzu("eil", ["eilst", "hetzt", "jagest", "preschst" ])
        self.WortRennen.fuegeVarianteHinzu("renn", ["rennst", "joggst", "läufst schnell"])
       
class WortGeneratorEbene(object):
    def  __init__(self, WortTyp):
        self.__initialisiereSchwimmen(WortTyp)
        self.__initialisiereFliegen(WortTyp)
        self.__initialisiereSteigen(WortTyp)
       
    def gebeWorte(self):
        return [self.WortSchwimmen, self.WortFliegen, self.WortSteigen]
    
    def __initialisiereSchwimmen(self,WortTyp):
        self.WortSchwimmen = Wort("schwimmen", WortTyp)
        self.WortSchwimmen.fuegeVarianteHinzu("schwimm", ["schwimmst"])
   
    def __initialisiereFliegen(self,WortTyp):
        self.WortFliegen = Wort("fliegen", WortTyp)
        self.WortFliegen.fuegeVarianteHinzu("flieg", ["fliegst", "flatterst"])
       
    def __initialisiereSteigen(self, WortTyp):
        self.WortSteigen = Wort("steigen", WortTyp)
        self.WortSteigen.fuegeVarianteHinzu("steig", ["steigst die Treppe"])
       
class WortGeneratorUebergang(object):
    def  __init__(self,WortTyp):
        self.__initialisiereSpringen(WortTyp)

    def gebeWorte(self):
        return [self.WortSpringen]

    def __initialisiereSpringen(self, WortTyp):
        self.WortSpringen = Wort("springen", WortTyp)
        self.WortSpringen.fuegeVarianteHinzu("spring", ["springst", "hüpst"])
      
class WortGeneratorBlumenpflege(object):
    def  __init__(self,WortTyp):   
        self.__initialisiereGieße (WortTyp)
        self.__initialisierePfluecke(WortTyp)
       
    def gebeWorte(self):
        return [self.WortGießen, self.WortPfluecken]
    
    def __initialisiereGieße(self, WortTyp):
        self.WortGießen = Wort("gießen", WortTyp)
        self.WortGießen.fuegeVarianteHinzu("gieß", ["gießt", "bewässerst" "versorgst"])
        self.WortGießen.fuegeVarianteHinzu("giess", ["gießt", "bewässerst" "versorgst"])
        
    def __initialisierePfluecke(self, WortTyp):
        self.WortPfluecken = Wort("pflücken", WortTyp)
        self.WortPfluecken.fuegeVarianteHinzu("pflücke", ["pflückst", "entwendest", "entreisst"])

class WortGeneratorInventar(object):
    def  __init__(self,WortTyp):   
        self.__initialisiereSchaue (WortTyp)
        self.__initialisiereInventar(WortTyp)
        
    def gebeWorte(self):
        return [self.WortSchauen, self.WortInventar]    
    
    def __initialisiereSchaue(self, WortTyp):
        self.WortSchauen = Wort("schauen", WortTyp)
        self.WortSchauen.fuegeVarianteHinzu("schau", ["schaust ins Inventar und siehst ", "guckst ins Inventar und erblickst " "blickst ins Inventar und begutachtest ","schaust in die Tasche und erkennst", "guckst in die Tasche und siehst " "blickst ind die Tasche und erkennst ", "schaust in den Beutel und siehst ", "guckst in den Beutel und erkennst" "blickst in den Beutel und begutachtest"])
        self.WortSchauen.fuegeVarianteHinzu("guck", ["schaust ins Inventar und siehst ", "guckst ins Inventar und erblickst " "blickst ins Inventar und begutachtest ","schaust in die Tasche und erkennst", "guckst in die Tasche und siehst " "blickst ind die Tasche und erkennst ", "schaust in den Beutel und siehst ", "guckst in den Beutel und erkennst" "blickst in den Beutel und begutachtest"])
        self.WortSchauen.fuegeVarianteHinzu("blick", ["schaust ins Inventar und siehst ", "guckst ins Inventar und erblickst " "blickst ins Inventar und begutachtest ","schaust in die Tasche und erkennst", "guckst in die Tasche und siehst " "blickst ind die Tasche und erkennst ", "schaust in den Beutel und siehst ", "guckst in den Beutel und erkennst" "blickst in den Beutel und begutachtest"])
             
    def __initialisiereInventar(self, WortTyp):
        self.WortInventar = Wort("Inventar", WortTyp)
        self.WortInventar.fuegeVarianteHinzu("Invantar", ["schaust ins Inventar und siehst ", "guckst ins Inventar und erblickst " "blickst ins Inventar und begutachtest ","schaust in die Tasche und erkennst", "guckst in die Tasche und siehst " "blickst ind die Tasche und erkennst ", "schaust in den Beutel und siehst ", "guckst in den Beutel und erkennst" "blickst in den Beutel und begutachtest"])
        self.WortInventar.fuegeVarianteHinzu("Tasche",["schaust ins Inventar und siehst ", "guckst ins Inventar und erblickst " "blickst ins Inventar und begutachtest ","schaust in die Tasche und erkennst", "guckst in die Tasche und siehst " "blickst ind die Tasche und erkennst ", "schaust in den Beutel und siehst ", "guckst in den Beutel und erkennst" "blickst in den Beutel und begutachtest"])
        self.WortInventar.fuegeVarianteHinzu("Beutel",["schaust ins Inventar und siehst ", "guckst ins Inventar und erblickst " "blickst ins Inventar und begutachtest ","schaust in die Tasche und erkennst", "guckst in die Tasche und siehst " "blickst ind die Tasche und erkennst ", "schaust in den Beutel und siehst ", "guckst in den Beutel und erkennst" "blickst in den Beutel und begutachtest"])

class WortGeneratoren(object):
    def  __init__(self):
       self.flaechenWorte =  WortGeneratorFlaeche(WortTyp.Flaeche)
       self.ebenenWorte = WortGeneratorEbene(WortTyp.Ebene)
       self.uebergangWorte = WortGeneratorUebergang(WortTyp.Uebergang)
       self.blumenpflegeWorte = WortGeneratorBlumenpflege(WortTyp.Blumenpflege)
    
    def gebeGeneratoren(self):
       yield self.flaechenWorte
       yield self.ebenenWorte
       yield self.uebergangWorte    
       yield self.blumenpflegeWorte

class WortVergleicher(object):
    def  __init__(self):
        self.WortGeneratoren = WortGeneratoren()

    def vergleiche(self,eingabe):
        for WortGenerator in self.WortGeneratoren.gebeGeneratoren():
            for WortGen in WortGenerator.gebeWorte():
                for Wort in WortGen.gebeAlleMoeglichenEingaben():
                    if Wort in eingabe:
                        return WortGen
        return None
    
    def gebeWort(self, bezeichnung):
        for WortGenerator in self.WortGeneratoren.gebeGeneratoren():
            for Wort in WortGenerator.gebeWorte() :
                if  Wort.gebeBezeichnung() == bezeichnung:
                    return Wort
        return None