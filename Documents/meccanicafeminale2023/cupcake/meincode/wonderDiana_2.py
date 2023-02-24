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

class Umgebung(object):
    
    def __init__(self, bezeichung,startBegrenzung, endBegrenzung):
        self.bezeichung =bezeichung
        self.geschwindigkeiten = {}
        self.verbtypen = {}
        self.startBegrenzung = startBegrenzung
        self.endBegrenzung = endBegrenzung
      
    def gebeBezeichnung(self):
        return self.bezeichung
        
    def setzeGeschwindigkeit(self, verb, wert, typ)
        self.geschwindigkeiten[verb] = wert          
        self.verbtypen[verb] = typ

    def gebeGeschwindigkeit(self,verb):
        return self.geschwindigkeiten[verb]
  
    def gebeVerbtyp(self,verb):
        return self.verbtypen[verb]

    def gebeVerben(self):
        return self.geschwindigkeiten.keys()

    def testeEndBegrenzung(self, userposition):
        if (userposition.gebeX() == endbegrenzung.gebeX()  and userposition.gebeY() == endbegrenzung.gebeY() ):
            return "genau nord-west oben" ## ecke
        elif (userposition.gebeX() == endbegrenzung.gebeX() - offset and userposition.gebeY() == endbegrenzung.gebeY() - offset):
            return "offset nord-west oben" ## ecke
        elif (userposition.gebeX() == endbegrenzung.gebeX() and userposition.gebeY() == - endbegrenzung.gebeY()):
            return "genau süd-west" ## ecke
        elif (userposition.gebeX() == endbegrenzung.gebeX() - offset and userposition.gebeY() == - endbegrenzung.gebeY() + offset):
            return "offset süd-west" ## ecke
        elif (userposition.gebeX() == - endbegrenzung.gebeX() and userposition.gebeY() == - endbegrenzung.gebeY()):
            return "genau süd-ost" ## ecke
        elif (userposition.gebeX() == - endbegrenzung.gebeX() + offset and userposition.gebeY() == - (endbegrenzung.gebeY()) + offset):
            return "offset süd-ost" ## ecke
        elif userposition.gebeX() == endbegrenzung.gebeX():
            return "genau ost"
        elif userposition.gebeX() == endbegrenzung.gebeX() - offset:
            return "offset ost"
        elif userposition.gebeX() == - endbegrenzung.gebeX():
            return "genau west"
        elif userposition.gebeX() == - endbegrenzung.gebeX() + offset:
            return "offset west"
        elif userposition.gebeY() == endbegrenzung.gebeY():
            return "genau nord"
        elif userposition.gebeY() == endbegrenzung.gebeY() - offset:
            return "offset nord"
        elif userposition.gebeY() == - endbegrenzung.gebeY():
            return "genau süd"
        elif userposition.gebeY() == - endbegrenzung.gebeY() + offset:
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
          self.eingabe = "start

    def druckeText(self):
         print(self.text)
    
    def druckePosition(self) :
        self.position.drucke

    def bewege(self, eingabe):
        self.eingabe =  eingabe

        for verb in  self.umgebung.gebeVerben()            
            if verb in self.eingabe:
                anwendung = self.umgebung.gebeVerbtyp(verb)
                if anwendung == "Fläche":
                    self.bewegeFläche(verb)
                elif anwendung =="Ebene":
                    self.bewegeEbene(verb)

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
        else 
            self.richtungstext = "unten" 

    #Bewegung allgemein

    def bewegeFläche(self, verb)

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

    def bewegeEbene(self, verb)
    
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

def hauptProgramm
    intro_text = "================= Dr. WonderDiana ====================="
    print(intro_text)

    beginning_text = "Du bist Doktorandin zu Beginn kannst Du eine Doktorarbeit schreiben und in alle Himmelsrichtungen (Nord,Ost,Süd,West) gehen oder rennen. Du musst erst weitere Fähigkeiten erlernen, bevor Du diese anwenden kannst. bitte gebe ´GEHE´ und die Richtung ein, um zu gehen und ´RENNE´  und die Richtung ein um zu rennen. mit ´wo bin ich?` erhälst Du Deine Position." 
    print(beginning_text)

    grenzPositionStartWasser = Position(12,12,-1)
    grenzPositionWasserWald = Position(40,40,0)
    grenzPositionWaldTreppe = Position (50,50,10)
    grenzPositiondoktormutter = Position(55,55,10)

    startUmgebung = Umgebung("start",Position(0,0,0),grenzPositionStartWasser) 
    startUmgebung.setzeGeschwindigkeit("gehst",2, "Fläche")
    startUmgebung.setzeGeschwindigkeit("rennst",4, "Fläche")
  
    wasserUmgebung = Umgebung("wasser",grenzPositionStartWasser,grenzPositionWasserWald) 
    wassertUmgebung.setzeGeschwindigkeit("schwimmst",4, "Ebene")

    waldUmgebung = Umgebung("start",grenzPositionWasserWald,grenzPositionWasserWald) 
    waldUmgebung.setzeGeschwindigkeit("gehst", 1, "Fläche")
    waldUmgebung.setzeGeschwindigkeit("rennst",2 , "Fläche")

    treppeUmgegung = Umgenung("treppe, "grenzPositionWasserWald, grenzPositionWaldTreppe)
    treppeUmgegung.setzeGeschwindigkeit("steigst",4, "Ebene")

    bewegung = Bewegung(Position(0,0,0), startUmgebung)

    letzeUserself.eingabe ="starte"
    doktormutterPosition = startPosition 

    Inventar  = []
    
    while True:

hauptProgramm()