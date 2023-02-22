class Position(object):
    def __init__(self,x,y,z):
        self.X = x
        self.Y = y
        self.Z = z        
    def ändereX(self,inkrement):
        self.X = self.X + inkrement
        self.drucke()
    def ändereY(self,inkrement):
        self.Y = self.Y + inkrement
        self.drucke()
    def ändereZ(self,inkrement):
        self.Z = self.Z + inkrement
        self.drucke()
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    def getZ(self):
        return self.Z
    def drucke(self):
        print("neue Position:" + str(self.getX()) + "." + str(self.getY()) + "." + str(self.getZ()))

def vergleichePositionen(userposition,vergleichsposition):
    
    if (userposition.getX() == vergleichsposition.getX() and userposition.getY() == vergleichsposition.getY()):
        return "genau nord-west oben" ## ecke
    elif (userposition.getX() == -vergleichsposition.getX() and userposition.getY() == vergleichsposition.getY()):
        return "genau nord-ost" ## ecke        
    elif (userposition.getX() == vergleichsposition.getX() and userposition.getY() == - vergleichsposition.getY()):
        return "genau süd-west" ## ecke
    elif (userposition.getX() == -vergleichsposition.getX() and userposition.getY() == - vergleichsposition.getY()):
        return "genau süd-ost" ## ecke
    elif userposition.getX() == vergleichsposition.getX():
        return "genau ost"
    elif userposition.getX() == - vergleichsposition.getX():
        return "genau west"
    elif userposition.getY() == vergleichsposition.getY():
        return "genau nord"
    elif userposition.getY() == - vergleichsposition.getY():
      return "genau süd"     
    else:
        return "kleineres"
 
       

def Richtungsabhängigkeit (eingabe, verb, position, geschwindigkeit, grenze):   
    if "nord" in eingabe and verb != "steigst":
        position.ändereY(geschwindigkeit)
        print("du " + verb +" weiter nach Norden.")
    elif "ost" in eingabe  and verb != "steigst":
        position.ändereX(geschwindigkeit)
        print("du " + verb +" nach Osten")
    elif "süd" in eingabe and verb != "steigst":
        position.ändereY(-geschwindigkeit)
        print("du " + verb +" nach Süden")
    elif "west" in eingabe and verb != "steigst":
        position.ändereX(-geschwindigkeit)
        print("du " + verb +" nach Westen.") 
    elif "hoch" in eingabe or "oben" in eingabe:
        if verb =="schwimmst" and position.getZ() ==grenze:
            print("du kannst hier nicht nach oben!")
        elif  (verb == "gehst" or verb == "rennst"):
            print("du kannst nicht nach oben gehen!")
        elif  (verb =="steigst"):            
                position.ändereZ(1)
                position.ändereY(1) ##vereinfacht immer nach süden
                print("du " + verb +" die Treppe nach oben.")                 
        else:
            position.ändereZ(geschwindigkeit())
            print("du " + verb +" nach oben.")
    elif "runter" in eingabe or "unten" in eingabe: 
        if verb =="schwimmst":
            print("du kannst hier nicht nach unten!")
        elif  verb == "gehst" or verb == "rennst" :
            print("du kannst nicht nach oben unten!")
        elif verb =="steigst":           
                position.ändereZ(1)
                position.ändereY(1) ##vereinfacht immer nach süden
                print("du " + verb +" die Treppe nach unten.")                 
        else:
            position.ändereZ(geschwindigkeit())
            print("du " + verb +" nach unten.") 
    ##else :   
       ##print("Eingabe konnte nicht verstanden werden. Bitte erneut eingeben")
     

def hauptprogramm():
    startPosition = Position(0,0,0)
    grenzPositionStartWasser = Position(12,12,-1)
    grenzPositionWasserWald = Position(40,40,0)
    grenzPositionWaldTreppe = Position (50,50,10)

    intro_text = "================= Dr. WonderDiana ====================="
    print(intro_text)

    beginning_text = "Du bist Dr. Wonder-Diana. zu Beginn kannst du nur in alle Himmelsrichtungen (Nord,Ost,Süd,West) gehen oder rennen. du musst erst weitere Fähigkeiten erlernen, bevor du diese anwenden kannst. bitte gebe ´GEHE´und die Richtung ein, um zu gehen und ´RENNE´ und die Richtung um zu rennen." 
    print(beginning_text)

    position = Position(0,0,0)
    umgebung = "start"
    kannfliegen = False

    while True:
           
        PositionsVergleichStartZuWasser = vergleichePositionen(position, grenzPositionStartWasser)
        PositionsVergleichWasserZuWald = vergleichePositionen(position, grenzPositionWasserWald)
        PositionsVergleichWaldZuTreppe = vergleichePositionen(position, grenzPositionWaldTreppe)

       ## print(PositionsVergleichStartZuWasser)
       ## print(PositionsVergleichWasserZuWald)
        if (umgebung == "start" and "genau" in PositionsVergleichStartZuWasser) or (umgebung =="wald" and "genau" in PositionsVergleichWasserZuWald):
            if umgebung =="start":
                PositionsVergleich = PositionsVergleichStartZuWasser
            elif umgebung =="wald":
                PositionsVergleich = PositionsVergleichWasserZuWald
            
            print("du stehst vor einem großen See. wenn du willst, kannst du jetzt ins wasser springen und danach schwimmen.")
            usereingabe = (input("> ").casefold()) ##casefold: in Kleinbuchstaben, ß in ss, umlaute bleiben
            if "springe" in usereingabe:                             
                position.ändereZ((-1))
                print("Du springst voller Elan ins Wasser")
                Richtungsabhängigkeit(PositionsVergleich,"schwimmst", position,4,startPosition.getZ())
                umgebung = "wasser" 
            elif "fliege" in usereingabe:
                if kannfliegen == True:
                    Richtungsabhängigkeit(usereingabe,"fliegst",position, 8,0)
                else:
                    print("du kannst nicht fiegen!")
            elif "gehe" in usereingabe and umgebung =="start":
                if "nord" in PositionsVergleich and "nord" in usereingabe   :
                    print("du kannst nicht nach Norden, da hier der See ist")
                elif "ost" in PositionsVergleich and "ost" in usereingabe:
                    print("du kannst nicht nach Osten, da hier der See ist")
                elif "süd" in PositionsVergleich and "süd" in usereingabe:
                    print("du kannst nicht nach Süden, da hier der See ist")
                elif "west" in PositionsVergleich and "west" in usereingabe:
                    print("du kannst nicht nach Westen, da hier der See ist")
                else:  Richtungsabhängigkeit(usereingabe,"gehst", position,2,startPosition.getZ())
            elif "gehe" in usereingabe and umgebung =="wald": ## achtung, richtungen müssen geswitcht werden, da vergleicher von start aus schaut
                if "süd" in PositionsVergleich and "nord" in usereingabe   :
                    print("du kannst nicht nach Norden, da hier der See ist")
                elif "west" in PositionsVergleich and "ost" in usereingabe:
                    print("du kannst nicht nach Osten, da hier der See ist")
                elif "nord" in PositionsVergleich and "süd" in usereingabe:
                    print("du kannst nicht nach Süden, da hier der See ist")
                elif "ost" in PositionsVergleich and "west" in usereingabe:
                    print("du kannst nicht nach Westen, da hier der See ist")
                else:  Richtungsabhängigkeit(usereingabe,"gehst", position,2,startPosition.getZ())
            elif "renne" in usereingabe:
                print("so nah am see solltest du nicht rennen!")
            elif "schwimme" in usereingabe:
                print("Du kannst NUR im Wasser schwimmen!") 
            else: 
                print("Eingabe  nicht erkannt. Du springst ins Wasser.")
                position.ändereZ((-1))              
                Richtungsabhängigkeit(PositionsVergleich,"schwimmst", position,4,startPosition.getZ())
                umgebung = "wasser" 

            position.drucke()

        elif umgebung =="wasser" and ("genau" in PositionsVergleichStartZuWasser or "genau" in PositionsVergleichWasserZuWald):
            
            if "genau" in PositionsVergleichStartZuWasser:
                print("Du stößt an das Start-Ufer und kannst hier hochspringen")
                ziel = "start"
                hoehe = startPosition.getZ()               
                PositionsVergleich = PositionsVergleichStartZuWasser
            elif  "genau" in PositionsVergleichWasserZuWald:
                print("Du stößt an das Ufer zum Wald und kannst hier hochspringen")
                ziel ="wald"
                hoehe = grenzPositionWasserWald.getZ()
                PositionsVergleich = PositionsVergleichWasserZuWald

            usereingabe = (input("> ").casefold()) ##casefold: in Kleinbuchstaben, ß in ss, umlaute bleiben
                      
            if "springe" in usereingabe:
                print("du springst voller Kraft aus dem See" ) 
                umgebung = ziel           
                position.ändereZ((1))
                Richtungsabhängigkeit(PositionsVergleich,"gehst", position,2,hoehe)   
            elif "fliege" in usereingabe:
                if kannfliegen == True:
                    Richtungsabhängigkeit(usereingabe,"fliegst",position, 8,0)
                else:
                    print("du kannst nicht fiegen!")
                    
            elif "schwimme" in usereingabe and ziel =="wald" :
                if "nord" in PositionsVergleich and "nord" in usereingabe:
                    print("du kannst nicht nach Norden, da hier das Ufer ist")
                elif "ost" in PositionsVergleich and "ost" in usereingabe:
                    print("du kannst nicht nach Osten, da hier das Ufere ist")
                elif "süd" in PositionsVergleich and "süd" in usereingabe:
                    print("du kannst nicht nach Süden, da hier das Ufer ist")
                elif "west" in PositionsVergleich and "west" in usereingabe:
                    print("du kannst nicht nach Westen, da hier das Ufer ist")
                else:  Richtungsabhängigkeit(usereingabe,"schwimmst", position,4,grenzPositionStartWasser.getZ())

            elif "schwimme" in usereingabe and ziel=="start" :## achtung, richtungen müssen geswitcht werden, da vergleicher von start aus schaut
                if "süd" in PositionsVergleich and "nord" in usereingabe   :
                    print("du kannst nicht nach Norden, da hier das Ufer ist")
                elif "west" in PositionsVergleich and "ost" in usereingabe:
                    print("du kannst nicht nach Osten, da hier das Ufere ist")
                elif "nord" in PositionsVergleich and "süd" in usereingabe:
                    print("du kannst nicht nach Süden, da hier das Ufer ist")
                elif "ost" in PositionsVergleich and "west" in usereingabe:
                    print("du kannst nicht nach Westen, da hier das Ufer ist")
                else:  Richtungsabhängigkeit(usereingabe,"schwimmst", position,4,grenzPositionStartWasser.getZ())
            elif "gehe" in usereingabe:
                print("du kannst im Wasser nicht gehen")
            elif "renne" in usereingabe:
                print("du kannst im Wasser nicht rennen")
            else:
                "eingabe nicht erkannt! du springst aus dem Wasser"
                umgebung = "start"            
                position.ändereZ((1))
                Richtungsabhängigkeit(usereingabe,"gehst", position,2,grenzPositionStartWasser.getZ())   

        elif umgebung == "wald" and "genau" in PositionsVergleichWaldZuTreppe:
            print("du stehst genau vor der Treppe zur Uni. Du kammst diese nun hochstreigen (und sobald du auch nur einen Schritt oben bist wieder runtersteigen)")
            usereingabe = input("> ").casefold()
            if "steige hoch" in usereingabe:
                Richtungsabhängigkeit(usereingabe,"steigst", position,1,grenzPositionWaldTreppe.getZ()) 
                umgebung = "treppe"
            elif "süd" in usereingabe:
                print("Achtung, hier ist die Treppe, du kannst hier nicht weiter nach Süden!") 
            else:
                Richtungsabhängigkeit(usereingabe,"gehst", position,"1",grenzPositionWasserWald.getZ())

        elif umgebung == "treppe" and "genau" in PositionsVergleichWaldZuTreppe :
            print("du stehst wieder unten an der der Treppe zur Uni. Du kammst diese nun hochstreigen (und sobald du auch nur einen Schritt oben bist wieder runtersteigen)")
            usereingabe = input("> ").casefold()     
            if "süd" in usereingabe:
                print("Achtung, hier ist die Treppe, du kannst hier nicht weiter nach Süden!") 
            else:
                Richtungsabhängigkeit(usereingabe,"gehst", position,"1",grenzPositionWasserWald.getZ()) 
                umgebung = "wald" 

        else:
            usereingabe = input("> ").casefold()
          
            if "gehe" in usereingabe:
                if umgebung == "start":
                    Richtungsabhängigkeit(usereingabe,"gehst", position,2,startPosition.getZ())
                elif umgebung =="wald":
                    Richtungsabhängigkeit(usereingabe,"gehst", position,1,grenzPositionWasserWald.getZ())
                elif umgebung =="wasser":
                    print("Du kannst im Wasser nicht gehen!")
            elif "renne" in usereingabe:
                if umgebung == "start":
                    Richtungsabhängigkeit(usereingabe,"rennst", position,4,startPosition.getZ())
                elif umgebung =="wald" :
                    Richtungsabhängigkeit(usereingabe,"rennst", position,2,grenzPositionWasserWald.getZ())
                elif umgebung =="wasser":
                    print("Du kannst im Wasser nicht rennen!") 
                else:
                    print("fehler")
            elif "schwimme" in usereingabe:
                if umgebung =="wasser":
                    Richtungsabhängigkeit(usereingabe,"schwimmst",position,4,grenzPositionStartWasser.getZ)
                else:
                    print("Du kannst NUR im Wasser schwimmen!")   
            
            elif "steige" in usereingabe:
                if umgebung =="treppe":
                     Richtungsabhängigkeit(usereingabe,"steigst",position, 4,0)
             
            elif "fliege" in usereingabe:
                if kannfliegen == True:
                    Richtungsabhängigkeit(usereingabe,"fliegst",position, 4,0)
                else :
                    print("du kannst nicht fiegen!")

            else:
                print("Befehl nicht erkannt")
    
hauptprogramm()