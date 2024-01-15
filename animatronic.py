from random import choice

class Fredrik():

    def __init__(self):
        self.location = "scen"
        self.old = None
        self.cheat = False
        

    def move(self):
        if self.cheat == False:
            if self.location == "scen":
                self.location = "matsalen"
                self.old = "scen"
            elif self.location == "matsalen":
                self.location = choice([self.location, "scen", "vänster hall", "prishörnan", "höger hall", "toaletterna", "köket"])
                self.old = "matsalen"
            elif self.location == "höger hall":
                self.location = choice([self.location, "matsalen"])
                self.old = "höger hall"
            elif self.location == "toaletterna":
                self.location = choice([self.location, "matsalen"])
                self.old = "toaletterna"
            elif self.location == "köket":
                self.location = choice([self.location, "matsalen"])
                self.old = "köket"
            elif self.location ==  "prishörnan":
                self.location = choice([self.location, "matsalen"])
                self.old = "prishörnan"
            elif self.location == "vänster hall":
                self.location = choice([self.location, "matsalen", "förrådet"])
                self.old = "vänster hall"
            elif self.location == "förrådet":
                self.location = choice([self.location, "vänster hall"])
            self.old = "förrådet" 
        else:
            self.location = "scen"
            self.old = "scen"
    def returnLocation(self):
        return self.location
    
    def printMove(self):
        if self.old != self.location:
            print(f"\nFredrik flyttade sig från {self.old} till {self.location}\n")
        else:
            print(f"\nFredrik stannar i {self.old}\n")

    def activateCheat(self):
        self.cheat = True