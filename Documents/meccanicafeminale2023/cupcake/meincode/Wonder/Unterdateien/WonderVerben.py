import random
from enum import Enum

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
        self.VerbGehen.fuegeVarianteHinzu("geh", ["gehst", "l??ufst", "schlenderst", "schleichst"])
        self.VerbGehen.fuegeVarianteHinzu("lauf", ["gehst", "l??ufst", "marschierst"])
     

    def __initialisiereRennen(self,verbtyp):
        self.VerbRennen = Verb("rennen", verbtyp)
        self.VerbRennen.fuegeVarianteHinzu("eil", ["eilst", "hetzt", "jagest", "preschst" ])
        self.VerbRennen.fuegeVarianteHinzu("renn", ["rennst", "joggst", "l??ufst schnell"])
       
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
        self.VerbSpringen.fuegeVarianteHinzu("spring", ["springst", "h??pst"])
      
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
        self.__initialisiereGie??e (verbtyp)
        self.__initialisierePfluecke(verbtyp)
       
    def gebeVerben(self):
        return [self.VerbForschen, self.VerbSprechen]
    
    def __initialisiereGie??e(self, verbtyp):
        self.VerbGie??en = Verb("gie??en", verbtyp)
        self.VerbGie??en.fuegeVarianteHinzu("gie??", ["gie??t", "bew??sserst" "versorgst"])
    
    def __initialisierePfluecke(self, verbtyp):
        self.VerbPfluecken = Verb("pfl??cken", verbtyp)
        self.VerbPfluecken.fuegeVarianteHinzu("pfl??cke", ["pfl??ckst", "entwendest", "entreisst"])
