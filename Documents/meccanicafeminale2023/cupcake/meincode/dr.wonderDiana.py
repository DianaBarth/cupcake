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

def vergleichePositionen(userposition,vergleichsposition, offset):
    if (userposition.getX() == vergleichsposition.getX()  and userposition.getY() == vergleichsposition.getY() ):
        return "genau nord-west oben" ## ecke
    elif (userposition.getX() == vergleichsposition.getX() - offset and userposition.getY() == vergleichsposition.getY() - offset):
        return "offset nord-west oben" ## ecke
    elif (userposition.getX() == vergleichsposition.getX() and userposition.getY() == - vergleichsposition.getY()):
        return "genau süd-west" ## ecke
    elif (userposition.getX() == vergleichsposition.getX() - offset and userposition.getY() == - vergleichsposition.getY() + offset):
        return "offset süd-west" ## ecke
    elif (userposition.getX() == - vergleichsposition.getX() and userposition.getY() == - vergleichsposition.getY()):
        return "genau süd-ost" ## ecke
    elif (userposition.getX() == - vergleichsposition.getX() + offset and userposition.getY() == - (vergleichsposition.getY()) + offset):
        return "offset süd-ost" ## ecke
    elif userposition.getX() == vergleichsposition.getX():
        return "genau ost"
    elif userposition.getX() == vergleichsposition.getX() - offset:
        return "offset ost"
    elif userposition.getX() == - vergleichsposition.getX():
        return "genau west"
    elif userposition.getX() == - vergleichsposition.getX() + offset:
        return "offset west"
    elif userposition.getY() == vergleichsposition.getY():
        return "genau nord"
    elif userposition.getY() == vergleichsposition.getY() - offset:
        return "offset nord"
    elif userposition.getY() == - vergleichsposition.getY():
        return "genau süd"
    elif userposition.getY() == - vergleichsposition.getY() + offset:
        return "offset süd"     
    else:
        return "kleineres"
 
def Richtungsabhängigkeit (eingabe, verb, position, geschwindigkeit, grenze):   
    if "nord" in eingabe and verb != "steigst":
        print("du " + verb +" weiter nach Norden.")
        position.ändereY(geschwindigkeit)
    
    elif "ost" in eingabe  and verb != "steigst":
        print("du " + verb +" nach Osten")
        position.ändereX(geschwindigkeit)     
    elif "süd" in eingabe and verb != "steigst":
        print("du " + verb +" nach Süden")
        position.ändereY(-geschwindigkeit)
     
    elif "west" in eingabe and verb != "steigst":
        position.ändereX(-geschwindigkeit)
        print("du " + verb +" nach Westen.") 
    elif "hoch" in eingabe or "oben" in eingabe:
        if verb =="schwimmst" and position.getZ() ==grenze:
            print("du kannst hier nicht nach oben!")
        elif  (verb == "gehst" or verb == "rennst"):
            print("du kannst nicht nach oben gehen!")
        elif  (verb =="steigst"):    
            print("du steigst die Treppe nach oben.")        
            position.ändereZ(1)
               
            if "nord-west" in eingabe:
                position.ändereY(geschwindigkeit)
                position.ändereX(-geschwindigkeit)
            elif "nord-ost" in eingabe:
                position.ändereY(geschwindigkeit)
                position.ändereX(geschwindigkeit)                 
            elif "süd-west" in eingabe:
                position.ändereY(-geschwindigkeit)
                position.ändereX(-geschwindigkeit)                   
            elif "süd-ost" in eingabe:
                
                position.ändereY(-geschwindigkeit)
                position.ändereX(geschwindigkeit)

          

        else:
            print("du " + verb +" nach oben.")
            position.ändereZ(geschwindigkeit())
            
    elif "runter" in eingabe or "unten" in eingabe: 
        if verb =="schwimmst":
            print("du kannst hier nicht nach unten!")
        elif  verb == "gehst" or verb == "rennst" :
            print("du kannst nicht nach oben unten!")
        elif verb =="steigst":  
            
            print("du " + verb +" die Treppe nach unten.")  
            position.ändereZ(1)
                
            if "nord-west" in eingabe:
                position.ändereY(geschwindigkeit)
                position.ändereX(-geschwindigkeit)
            elif "nord-ost" in eingabe:
                position.ändereY(geschwindigkeit)
                position.ändereX(geschwindigkeit)                 
            elif "süd-west" in eingabe:
                position.ändereY(-geschwindigkeit)
                position.ändereX(-geschwindigkeit)                   
            elif "süd-ost" in eingabe:
                position.ändereY(-geschwindigkeit)
                position.ändereX(geschwindigkeit)  
        else:
            print("du " + verb +" nach unten.") 
            position.ändereZ(geschwindigkeit())
          
    ##else :   
       ##print("Eingabe konnte nicht verstanden werden. Bitte erneut eingeben")
     

def hauptprogramm():
    startPosition = Position(0,0,0)
    grenzPositionStartWasser = Position(12,12,-1)
    grenzPositionWasserWald = Position(40,40,0)
    grenzPositionWaldTreppe = Position (50,50,10)

    intro_text = "================= Dr. WonderDiana ====================="
    print(intro_text)

    beginning_text = "Du bist Dr. Wonder-Diana. zu Beginn kannst du nur in alle Himmelsrichtungen (Nord,Ost,Süd,West) gehen oder rennen. du musst erst weitere Fähigkeiten erlernen, bevor du diese anwenden kannst. bitte gebe ´GEHE´ und die Richtung ein, um zu gehen und ´RENNE´  und die Richtung ein um zu rennen." 
    print(beginning_text)

    position = Position(0,0,0)
    umgebung = "start"
    kannfliegen = False

    offset =0
    while True:
           
        PositionsVergleichStartZuWasser = vergleichePositionen(position, grenzPositionStartWasser, offset)
        PositionsVergleichWasserZuWald = vergleichePositionen(position, grenzPositionWasserWald, offset)
        PositionsVergleichWaldZuTreppe = vergleichePositionen(position, grenzPositionWaldTreppe, offset)

        print("debuginfo " + str(PositionsVergleichStartZuWasser) + "---"  + str(offset))
        print("debuginfo " + str(PositionsVergleichWasserZuWald)  + "---"  + str(offset))

        if ((umgebung == "start" and "genau" in PositionsVergleichStartZuWasser) or (umgebung =="wald" and "genau" in PositionsVergleichWasserZuWald) or
            (umgebung == "start" and "offset" in PositionsVergleichStartZuWasser) or (umgebung =="wald" and "offset" in PositionsVergleichWasserZuWald)):

            if umgebung =="start":
                PositionsVergleich = PositionsVergleichStartZuWasser
                geschwindigkeit = 2
                hoehe = startPosition.getZ()
            elif umgebung =="wald":
                PositionsVergleich = PositionsVergleichWasserZuWald
                geschwindigkeit = 1
                hoehe = grenzPositionWasserWald.getZ()

            if "genau" in PositionsVergleich:
                print("du stehst vor einem großen See. wenn du willst, kannst du jetzt ins wasser springen und danach schwimmen.")
            else :
                print("Du siehst in der Nähe einen großen See.")                
                Richtungsabhängigkeit(letzeUsereingabe,"gehst", position,geschwindigkeit,hoehe)
                print("wenn du willst, kannst du jetzt ins wasser springen und danach schwimmen.")

            usereingabe = (input("> ").casefold()) ##casefold: in Kleinbuchstaben, ß in ss, umlaute bleiben
            if "springe" in usereingabe:                             
                position.ändereZ((-1))
                print("Du springst voller Elan ins Wasser")
                Richtungsabhängigkeit(PositionsVergleich,"schwimmst", position,4,startPosition.getZ())
                umgebung = "wasser" 
                offset = 0
            elif "fliege" in usereingabe:
                if kannfliegen == True:
                    Richtungsabhängigkeit(usereingabe,"fliegst",position, 8,0)
                    offset=0
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

                offset = 0
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

                offset = 0
            elif "renne" in usereingabe:
                print("so nah am see solltest du nicht rennen!")
            elif "schwimme" in usereingabe:
                print("Du kannst NUR im Wasser schwimmen!") 
            else: 
                print("Eingabe  nicht erkannt. Du springst ins Wasser.")
                position.ändereZ((-1))              
                Richtungsabhängigkeit(PositionsVergleich,"schwimmst", position,4,startPosition.getZ())
                umgebung = "wasser"
                offset =0

            position.drucke()

        elif umgebung =="wasser" and ("genau" in PositionsVergleichStartZuWasser or "genau" in PositionsVergleichWasserZuWald or
        "offset" in PositionsVergleichStartZuWasser or "offset" in PositionsVergleichWasserZuWald):
            ##offset dürfte egtl hier nicht vorkommen, da im wasser konstante gescvhwindigkeit
            offset = 0
            if "genau" in PositionsVergleichStartZuWasser or "offset" in PositionsVergleichStartZuWasser:
                print("Du stößt an das Start-Ufer und kannst hier hochspringen")
                ziel = "start"
                hoehe = startPosition.getZ()               
                PositionsVergleich = PositionsVergleichStartZuWasser
            elif  "genau" in PositionsVergleichWasserZuWald or "offset" in PositionsVergleichWasserZuWald:
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
            offset =0       

            if position.getX() <=0 and position.getY() <=0:    
                if "steige hoch" in usereingabe:
                    Richtungsabhängigkeit(usereingabe + " nord-west","steigst",position, 1,grenzPositionWaldTreppe.getZ)
                    umgebung = "treppe"            
                elif "nord" in usereingabe or "west" in usereingabe:
                    print("du kannst nicht in diese Richtung, das hier die Treppe ist")
            elif position.getX() >=0 and position.getY() <=0:    
                if "steige hoch" in usereingabe:
                    Richtungsabhängigkeit(usereingabe + " nord-ost","steigst",position, 1,grenzPositionWaldTreppe.getZ)
                    umgebung = "treppe" 
                elif "nord" in usereingabe or "ost" in usereingabe:
                    print("du kannst nicht in diese Richtung, das hier die Treppe ist")
            elif position.getX() <=0 and position.getY() >=0:    
                if "steige hoch" in usereingabe:
                    Richtungsabhängigkeit(usereingabe + " süd-west","steigst",position, 1,grenzPositionWaldTreppe.getZ)
                    umgebung = "treppe"            
                elif "süd" in usereingabe or "west" in usereingabe:
                    print("du kannst nicht in diese Richtung, das hier die Treppe ist")    
            elif position.getX() >=0 and position.getY() >=0:    
                if "steige hoch" in usereingabe:
                    Richtungsabhängigkeit(usereingabe + " süd-ost","steigst",position, 1,grenzPositionWaldTreppe.getZ)
                    umgebung = "treppe"            
                elif "süd" in usereingabe or "ost" in usereingabe:
                    print("du kannst nicht in diese Richtung, das hier die Treppe ist")
            
        elif umgebung == "treppe" and "genau" in PositionsVergleichWaldZuTreppe :
            
            print("du stehst wieder unten an der der Treppe zur Uni. Du kammst diese nun hochstreigen (und sobald du auch nur einen Schritt oben bist wieder runtersteigen)")
            usereingabe = input("> ").casefold()     
            if "süd" in usereingabe:
                print("Achtung, hier ist die Treppe, du kannst hier nicht weiter nach Süden!") 
            else:
                Richtungsabhängigkeit(usereingabe,"gehst", position,"1",grenzPositionWasserWald.getZ()) 
                umgebung = "wald" 
                offset=0
        else:
            usereingabe = input("> ").casefold()
          
            if "gehe" in usereingabe:
                if umgebung == "start":
                    Richtungsabhängigkeit(usereingabe,"gehst", position,2,startPosition.getZ())
                    offset =0
                elif umgebung =="wald":
                    Richtungsabhängigkeit(usereingabe,"gehst", position,1,grenzPositionWasserWald.getZ())
                    offset =0
                elif umgebung =="wasser":
                    print("Du kannst im Wasser nicht gehen!")
            elif "renne" in usereingabe:
                if umgebung == "start":
                    offset = 2
                    Richtungsabhängigkeit(usereingabe,"rennst", position,4,startPosition.getZ())
                   
                elif umgebung =="wald" :
                    offset = 1
                    Richtungsabhängigkeit(usereingabe,"rennst", position,2,grenzPositionWasserWald.getZ())
                elif umgebung =="wasser":
                    print("Du kannst im Wasser nicht rennen!") 
                else:
                    print("fehler")
            elif "schwimme" in usereingabe:
                if umgebung =="wasser":
                    offset = 0
                    Richtungsabhängigkeit(usereingabe,"schwimmst",position,4,grenzPositionStartWasser.getZ)
                else:
                    print("Du kannst NUR im Wasser schwimmen!")   
            
            elif "steige" in usereingabe:
                offset = 0
                if umgebung =="treppe":
                    if "hoch" in usereingabe:
                        grenze = grenzPositionWaldTreppe.getZ()
                    elif "runter" in usereingabe:
                        grenze = grenzPositionWasserWald.getZ()

                    if position.getX() <=0 and position.getY() <=0:    
                        Richtungsabhängigkeit(usereingabe + " nord-west","steigst",position, 1,grenze)
                    elif position.getX() >=0 and position.getY() <=0:    
                        Richtungsabhängigkeit(usereingabe + " nord-ost","steigst",position, 1,grenze)
                    elif position.getX() <=0 and position.getY() >=0:    
                        Richtungsabhängigkeit(usereingabe + " süd-west","steigst",position, 1,grenze)
                    elif position.getX() >=0 and position.getY() >=0:    
                        Richtungsabhängigkeit(usereingabe + " süd-ost","steigst",position, 1,grenze)

            elif "fliege" in usereingabe:
                if kannfliegen == True:
                    Richtungsabhängigkeit(usereingabe,"fliegst",position, 4,0)
                else :
                    print("du kannst nicht fiegen!")

            else:
                print("Befehl nicht erkannt")
    
            letzeUsereingabe = usereingabe
            
hauptprogramm()