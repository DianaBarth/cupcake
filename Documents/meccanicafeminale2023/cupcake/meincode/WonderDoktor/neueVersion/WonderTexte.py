
class WonderText(object):
    def __init__(self):
          self.text = ""
    
    def setzeText(self,text):
        self.text = text

    def ergaenzeText(self,text):
         self.text = self.text + "\n" + text
       
    def druckeText(self):
         if self.text !="":
             print(self.text)
    
    def druckeAbschluss(self): 
        print("--------------------------------------")
        self.text =""

    def druckeEingabeNichtErkannt(self,eingabe):
        self.text = "Achtung, Eingabe '" + eingabe  +  "' nicht erkannt! Bitte versuche es erneut!"