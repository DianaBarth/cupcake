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
    
    def __init__(self, bezeichung, endBegrenzung, wechselVerb):
        self.bezeichung =bezeichung
        self.geschwindigkeiten = {}
        self.verbtypen = {}
        self.endBegrenzung = endBegrenzung
        self.offset = 0
        self.naechsteUmgebung = None
        self.wechselVerb = wechselVerb

    def setzeNaechsteUmgebung(self,naechsteUmgebung)    
        self.naechsteUmgebung = naechsteUmgebung
    
    def setzeOffset(self, offset)
        self.offset = offset
    
    def setzeGeschwindigkeit(self, verb, wert, typ)
        self.geschwindigkeiten[verb] = wert          
        self.verbtypen[verb] = typ

    def gebeBezeichnung(self):
        return self.bezeichung
        
    def gebeGeschwindigkeit(self,verb):
        return self.geschwindigkeiten[verb]
  
    def gebeVerbtyp(self,verb):
        return self.verbtypen[verb]

    def gebeVerben(self):
        return self.geschwindigkeiten.keys()

    def gebeWechselverb(self):
        retrun self.wechselVerb

    def testeEndBegrenzung(self, userposition):
        if (userposition.gebeX() == endbegrenzung.gebeX()  and userposition.gebeY() == endbegrenzung.gebeY() ):
            return "genau nord-west oben" ## ecke
        elif (userposition.gebeX() == endbegrenzung.gebeX() - self.offset and userposition.gebeY() == endbegrenzung.gebeY() - self.offset):
            return "offset nord-west oben" ## ecke
        elif (userposition.gebeX() == endbegrenzung.gebeX() and userposition.gebeY() == - endbegrenzung.gebeY()):
            return "genau süd-west" ## ecke
        elif (userposition.gebeX() == endbegrenzung.gebeX() - self.offset and userposition.gebeY() == - endbegrenzung.gebeY() + self.offset):
            return "offset süd-west" ## ecke
        elif (userposition.gebeX() == - endbegrenzung.gebeX() and userposition.gebeY() == - endbegrenzung.gebeY()):
            return "genau süd-ost" ## ecke
        elif (userposition.gebeX() == - endbegrenzung.gebeX() + self.offset and userposition.gebeY() == - (endbegrenzung.gebeY()) + self.offset):
            return "offset süd-ost" ## ecke
        elif userposition.gebeX() == endbegrenzung.gebeX():
            return "genau ost"
        elif userposition.gebeX() == endbegrenzung.gebeX() - self.offset:
            return "offset ost"
        elif userposition.gebeX() == - endbegrenzung.gebeX():
            return "genau west"
        elif userposition.gebeX() == - endbegrenzung.gebeX() + self.offset:
            return "offset west"
        elif userposition.gebeY() == endbegrenzung.gebeY():
            return "genau nord"
        elif userposition.gebeY() == endbegrenzung.gebeY() - self.offset:
            return "offset nord"
        elif userposition.gebeY() == - endbegrenzung.gebeY():
            return "genau süd"
        elif userposition.gebeY() == - endbegrenzung.gebeY() + self.offset:
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
                
               grenzTest = self.umgebung.testeEndBegrenzung(self.position) 
               
               if grenzTest == "kleineres":

                    anwendung = self.umgebung.gebeVerbtyp(verb)
                    if anwendung == "Fläche":
                        self.bewegeFläche(verb)
                    elif anwendung =="Ebene":
                        self.bewegeEbene(verb)

                elif "genau" in grenzTest :
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

    startUmgebung = Umgebung("start",grenzPositionStartWasser,  "springe") 
    startUmgebung.setzeGeschwindigkeit("gehst",2, "Fläche")
    startUmgebung.setzeGeschwindigkeit("rennst",4, "Fläche")
    startUmgebung.setzeOffset(2)
  
    wasserUmgebung = Umgebung("wasser",grenzPositionWasserWald, "springe") 
    wassertUmgebung.setzeGeschwindigkeit("schwimmst",4, "Ebene")

    waldUmgebung = Umgebung("wald",grenzPositionWaldTreppe, "steige") 
    waldUmgebung.setzeGeschwindigkeit("gehst", 1, "Fläche")
    waldUmgebung.setzeGeschwindigkeit("rennst",2 , "Fläche")
    waldUmgebung.setzeOffset(1)

    treppeUmgegung = Umgenung("treppe", grenzPositiondoktormutter, "spreche")
    treppeUmgegung.setzeGeschwindigkeit("steigst",4, "Ebene")

    startUmgebung.setzeNaechsteUmgebung(wasserUmgebung)
    wasserUmgebung.setzeNaechsteUmgebung(waldUmgebung)
    waldUmgebung.setzeNaechsteUmgebung(treppeUmgegung)

    bewegung = Bewegung(Position(0,0,0), startUmgebung)

    while True:
        
        usereingabe = input("> ").casefold()
        bewegung.bewege(usereingabe)
        bewegung.druckeText()
        bewegung.druckePosition()
        
    Inventar  = []
    
    while True:

hauptProgramm()