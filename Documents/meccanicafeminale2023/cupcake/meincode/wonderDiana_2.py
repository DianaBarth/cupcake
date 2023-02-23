

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

def vergleichePositionen(userposition,vergleichsposition, offset):
    if (userposition.gebeX() == vergleichsposition.gebeX()  and userposition.gebeY() == vergleichsposition.gebeY() ):
        return "genau nord-west oben" ## ecke
    elif (userposition.gebeX() == vergleichsposition.gebeX() - offset and userposition.gebeY() == vergleichsposition.gebeY() - offset):
        return "offset nord-west oben" ## ecke
    elif (userposition.gebeX() == vergleichsposition.gebeX() and userposition.gebeY() == - vergleichsposition.gebeY()):
        return "genau süd-west" ## ecke
    elif (userposition.gebeX() == vergleichsposition.gebeX() - offset and userposition.gebeY() == - vergleichsposition.gebeY() + offset):
        return "offset süd-west" ## ecke
    elif (userposition.gebeX() == - vergleichsposition.gebeX() and userposition.gebeY() == - vergleichsposition.gebeY()):
        return "genau süd-ost" ## ecke
    elif (userposition.gebeX() == - vergleichsposition.gebeX() + offset and userposition.gebeY() == - (vergleichsposition.gebeY()) + offset):
        return "offset süd-ost" ## ecke
    elif userposition.gebeX() == vergleichsposition.gebeX():
        return "genau ost"
    elif userposition.gebeX() == vergleichsposition.gebeX() - offset:
        return "offset ost"
    elif userposition.gebeX() == - vergleichsposition.gebeX():
        return "genau west"
    elif userposition.gebeX() == - vergleichsposition.gebeX() + offset:
        return "offset west"
    elif userposition.gebeY() == vergleichsposition.gebeY():
        return "genau nord"
    elif userposition.gebeY() == vergleichsposition.gebeY() - offset:
        return "offset nord"
    elif userposition.gebeY() == - vergleichsposition.gebeY():
        return "genau süd"
    elif userposition.gebeY() == - vergleichsposition.gebeY() + offset:
        return "offset süd"     
    else:
        return "kleineres"
 

class Umgebung(object):
     def __init__(self, bezeichung):
        self.bezeichung =bezeichung
        self.geschwindigkeiten = []

      def gebeBezeichnung(self):
        return self.bezeichung
        
      def setzeGeschwindigkeit(self, verb, wert)
         self.geschwindigkeiten.append (Geschwindigkeit(verb, wert))
         
      def gebeGeschwindigkeit(self,verb):
          return self.geschwindigkeiten[verb].getWert


class Geschwindigkeit(object) :
     def __init__(self, bezeichung, wert):
        self.bezeichung =bezeichung
        self.wert = wert

    def getWert(self):
        retrun self.wert


class Bewegung(object):
    def __init__(self, startPosition, startUmgebung):
          self.text = ""
          self.richtungstext =""
          self.hoehentext = ""
          self.position = startPosition
          self.umgebung = startUmgebung

    def druckeText(self):
         print(self.text)
    
    def druckePosition(self) :
        self.position.drucke

    def bewege(self,eingabe):
        if "gehe" in eingabe:
            self.gehe(eingabe)
        if "renne" in eingabe:
            self.renne(eingabe)

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

    def hohe(self, geschwindigkeit):
        self.position.ändereZ(geschwindigkeit)
        if geschwindigkeit > 0: 
            self.hoehentext = "hoch"
        else 
            self.hohenetext = "runter" 

    def richtungFläche(self, geschwindikgeit)
    	if "nord" in eingabe:
            self.nord(geschwindigkeit)
        elif "ost" in eingabe:
            self.ost(geschwindigkeit)
        elif "süd" in eingabe:
            self.süd(geschwindigkeit)
        elif "west" in eingabe  :
            self.west(geschwindigkeit)

            
    def gehe(self, eingabe)

        geschwindigkeit = self.umgebung.gebeGeschwindigkeit("gehe")
        richtungFläche(geschwindigkeit)
        self.text = "Du gehst nach " + self.richtungstext

     def renne(self, eingabe)

        geschwindigkeit = self.umgebung.gebeGeschwindigkeit("renne")
        richtungFläche(geschwindigkeit)
    	self.text = "Du rennst nach " + self.richtungstext


def richtungsbhängigkeit (eingabe, verb, position, geschwindigkeit, grenze):  
    if verb == "steigst" :   
        if "runter" in eingabe:
            verb = "steigst gemütlich die Treppe runter,"
            position.ändereZ(-1)
        else
            verb = "steigst gemütlich die Treppe hinauf,"
            position.ändereZ(1)

    if "nord" in eingabe:
        print("Du " + verb +" weiter nach Norden.")
        position.ändereY(geschwindigkeit)
    
    elif "ost" in eingabe:
        print("Du " + verb +" nach Osten")
        position.ändereX(geschwindigkeit)     
    elif "süd" in eingabe:
        print("Du " + verb +" nach Süden")
        position.ändereY(-geschwindigkeit)
     
    elif "west" in eingabe:
        position.ändereX(-geschwindigkeit)
        print("Du " + verb +" nach Westen.") 

    elif "hoch" in eingabe or "oben" in einabe or "höher" in eingabe or "himmel" in eingabe:
        if verb =="schwimmst" and position.gebeZ() == grenze:
            print("Du kannst hier nicht nach oben schwimmen!")
        elif  (verb == "gehst" or verb == "rennst"):
            print("Du kannst nicht zu Fuß nach oben!"
        else:
            print("Du " + verb +" nach oben.")
            position.ändereZ(geschwindigkeit())
            
    elif "runter" in eingabe or "unten" in eingabe or "tiefer" in eingabe:
        if verb =="schwimmst" and position.gebeZ() == grenze:
            print("Du kannst hier nicht nach unten schwimmen!")
        elif  verb == "gehst" or verb == "rennst" :
            print("Du kannst nicht zu Fuß nach unten!")
        else:
            print("Du " + verb +" nach unten.") 
            position.ändereZ(geschwindigkeit())