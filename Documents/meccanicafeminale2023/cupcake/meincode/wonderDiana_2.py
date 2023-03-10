import random

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
    def drucke(self):
        print("Du befindest dich an der Position " + str(self.gebeX()) + "." + str(self.gebeY()) + "." + str(self.gebeZ()))

class Verb(object):
    def __init__(self, bezeichnung):
        self.bezeichnung = bezeichnung
        self.variante = {} ##key = mögliche Eingabe, Value= mehrere mögliche Ausgaben
        
    def gebeBezeichnung(self):
        self.bezeichnung

    def fuegeVarianteHinzu(self,eingabe, ausgabe):     
        self.variante.update({eingabe : ausgabe})

    def gebeEineAusgabeZurEingabe (self,eingabe):
        for kombination in self.variante.keys:
            if eingabe in kombination:
                return random.choice(self.variante[eingabe])

    def gebeAlleMoeglichenEingaben(self):
        return self.variante.keys  

class Umgebung(object):
    
    def __init__(self, bezeichung, endbegrenzung, wechselVerb):
        self.bezeichung =bezeichung
        self.geschwindigkeiten = {}
        self.verbtypen = {}
        self.endbegrenzung = endbegrenzung
        self.offset = 0
        self.naechsteUmgebung = None
        self.wechselVerb = wechselVerb

    def setzeNaechsteUmgebung(self,naechsteUmgebung) :
        self.naechsteUmgebung = naechsteUmgebung
    
    def setzeOffset(self, offset):
        self.offset = offset
    
    def setzeGeschwindigkeit(self, verb, wert, typ):
        self.geschwindigkeiten.update ({verb : wert } )         
        self.verbtypen.update ({verb : typ})

    def gebeBezeichnung(self):
        return self.bezeichung
        
    def gebeGeschwindigkeit(self,verb):
        return self.geschwindigkeiten[verb]
  
    def gebeVerbtyp(self,verb):
        return self.verbtypen[verb]

    def gebeVerben(self):
        return self.geschwindigkeiten.keys()

    def gebeWechselverb(self):
        return self.wechselVerb

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

class Bewegung(object):
    def __init__(self, startPosition, startUmgebung):
          self.text = ""
          self.richtungstext =""  
          self.position = startPosition
          self.umgebung = startUmgebung
          self.kannfliegen = False
          self.eingabe = "start"

    def druckeText(self):
         print(self.text)
    
    def druckePosition(self) :
        self.position.drucke

    def bewege(self, eingabe):
        self.eingabe =  eingabe

        for verb in  self.umgebung.gebeVerben() :    

            for verbVariation in verb.gebeAlleMoeglichenEingaben():     
                   
                if verbVariation in self.eingabe:
                    
                    grenzTest = self.umgebung.testeEndBegrenzung(self.position) 
                
                    if "kleineres" in grenzTest:

                        anwendung = self.umgebung.gebeVerbtyp(verb)
                        if anwendung == "Fläche":
                            self.bewegeFläche(verb.gebeEineAusgabeZurEingabe(verbVariation))
                        elif anwendung =="Ebene":
                            self.bewegeEbene(verb.gebeEineAusgabeZurEingabe(verbVariation))

                    elif "genau" in grenzTest:
                            self.text = "Du stehst genau an einer Grenze."
                    
                    elif "offset" in grenzTest:
                        self.text = "du stehst kurz vor einer Grenze"


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

        self.text = "Du " + verb + " nach " + self.richtungstext

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

        self.text = "Du " + verb + " nach " + self.richtungstext

class Spiel(object):
    def __init__(self):
        self.__initialisiereVerben()
        self.__initialisierePositionen()
        self.__initialisereUmgebungen()
        self.bewegung = Bewegung(Position(0,0,0), self.startUmgebung)
         
    def  __initialisiereVerben(self):
        self.__initialisiereGehen()
        self.__initialisiereRennen()
        self.__initialisiereSchwimmen()
        self.__initialisiereSteigen()
        self.__initialisiereSpringen()
        self.__initialisiereForsche()

    def __initialisiereGehen(self):
        self.VerbGehen = Verb("gehen")
        self.VerbGehen.fuegeVarianteHinzu("geh", ["gehst", "läufst", "schlenderst", "schleichst"])
        self.VerbGehen.fuegeVarianteHinzu("lauf", ["gehst", "läufst", "marschierst"])
        
    def __initialisiereRennen(self):
        self.VerbRennen = Verb("rennen")
        self.VerbRennen.fuegeVarianteHinzu("eil", ["eilst", "hetzt", "jagest", "preschst" ])
        self.VerbRennen.fuegeVarianteHinzu("renn", ["rennst", "joggst", "läufst schnell"])
 
    def __initialisiereSchwimmen(self):
        self.VerbSchwimmen = Verb("schwimmen")
        self.VerbSchwimmen.fuegeVarianteHinzu("schwimm", ["schwimmst"])

    def __initialisiereSteigen(self):
        self.VerbSteigen = Verb("steigen")
        self.VerbSteigen.fuegeVarianteHinzu("steig", ["steigst", "erklimmst"])

    def __initialisiereSpringen(self):
        self.VerbSpringen = Verb("springen")
        self.VerbSpringen.fuegeVarianteHinzu("spring", ["springst", "hüpst"])

    def __initialisiereForsche(self):
        self.VerbForschen = Verb("forschen")
        self.VerbForschen.fuegeVarianteHinzu("forsch", ["forschst", "analysierst", "untersuchst"])
        self.VerbForschen.fuegeVarianteHinzu("analysiere", ["forschst", "analysierst", "untersuchst"])
        self.VerbForschen.fuegeVarianteHinzu("untersuch", ["forschst", "analysierst", "untersuchst"])
 
    def __initialisiereForsche(self):
        self.VerbForschen = Verb("sprechen")
        self.VerbForschen.fuegeVarianteHinzu("sprech", ["sprichst", "redest"])
        self.VerbForschen.fuegeVarianteHinzu("red", ["sprichst", "redest"])

    def __initialisierePositionen(self):
        self.grenzPositionStartWasser = Position(12,12,-1)
        self.grenzPositionWasserWald = Position(40,40,0)
        self.grenzPositionWaldTreppe = Position (50,50,10)
        self.grenzPositiondoktormutter = Position(55,55,10)

    def __initialisereUmgebungen(self):
        self.__initialisiereStartUmgebung()
        self.__initialisiereWasserUmgebung()
        self.__intiialiereWaldUmgebung()
        self.__initialisiereTreppeUmgebung()
        
        self.startUmgebung.setzeNaechsteUmgebung(self.wasserUmgebung)
        self.wasserUmgebung.setzeNaechsteUmgebung(self.waldUmgebung)
        self.waldUmgebung.setzeNaechsteUmgebung(self.treppeUmgegung)

    def __initialisiereStartUmgebung(self):
        self.startUmgebung = Umgebung("start",self.grenzPositionStartWasser,  self.VerbSpringen) 
        self.startUmgebung.setzeGeschwindigkeit( self.VerbGehen,2, "Fläche")
        self.startUmgebung.setzeGeschwindigkeit(self.VerbRennen,4, "Fläche")
        self.startUmgebung.setzeOffset(2)

    def __initialisiereWasserUmgebung(self):
        self.wasserUmgebung = Umgebung("wasser",self.grenzPositionWasserWald,  self.VerbSpringen) 
        self.wasserUmgebung.setzeGeschwindigkeit(self.VerbSchwimmen,4, "Ebene")

    def __intiialiereWaldUmgebung(self):
        self.waldUmgebung = Umgebung("wald",self.grenzPositionWaldTreppe, self.VerbSteigen) 
        self.waldUmgebung.setzeGeschwindigkeit( self.VerbGehen, 1, "Fläche")
        self.waldUmgebung.setzeGeschwindigkeit(self.VerbRennen,2 , "Fläche")
        self.waldUmgebung.setzeOffset(1)

    def __initialisiereTreppeUmgebung(self):
        self.treppeUmgegung = Umgebung("treppe", self.grenzPositiondoktormutter, self.VerbForschen)
        self.treppeUmgegung.setzeGeschwindigkeit(self.VerbSteigen,4, "Ebene")

    ##   Inventar  = []

    def spiele(self):

        print("=================WonderDoktor========================")

        while True:            
            usereingabe = input("> ").casefold()
            self.bewegung.bewege(usereingabe)
            self.bewegung.druckeText()
            self.bewegung.druckePosition()

meinspiel = Spiel()
meinspiel.spiele