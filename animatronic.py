from random import choice



class Bonnie():
    
    def __init__(self):
        self.location = "scen"
        self.old = None
    
    def move(self):
        if self.location == "scen":
            self.location = "matsal"
            self.old = "scen"
        elif self.location == "matsal":
            self.location = choice([self.location, "scen", "höger hall", "prishörna" ])
            self.old = "matsal"
        elif self.location ==  "prishörna":
            self.location = choice([self.location, "matsal"])
            self.old = "prishörna"
        elif self.location == "höger hall":
            self.location = choice([self.location, "matsal", "förråd"])
            self.old = "höger hall"
        elif self.location == "förråd":
            self.location = choice([self.location, "höger hall"])
            self.old = "förråd"
        
        
    def printMove(self):
        if self.old != self.location:
            print(f"Bonnie flyttade sig från {self.old} till {self.location}")
        else:
            print(f"Bonnie stannar i {self.old}")
        
class Fredrik():

    def __init__(self):
        self.location = "scen"
        self.old = None

    def move(self):
        if self.location == "scen":
            self.location = "matsal"
            self.old = "scen"
        elif self.location == "matsal":
            self.location = choice([self.location, "scen", "höger hall", "prishörna", "vänster hall", "toaletter", "kök"])
            self.old = "matsal"
        elif self.location == "vänster hall":
             self.location = choice([self.location, "matsal"])
             self.old = "vänster hall"
        elif self.location == "toaletter":
            self.location = choice([self.location, "matsal"])
            self.old = "toaletter"
        elif self.location == "kök":
            self.location = choice([self.location, "matsal"])
            self.old = "kök"
        elif self.location ==  "prishörna":
            self.location = choice([self.location, "matsal"])
            self.old = "prishörna"
        elif self.location == "höger hall":
            self.location = choice([self.location, "matsal", "förråd"])
            self.old = "höger hall"
        elif self.location == "förråd":
            self.location = choice([self.location, "höger hall"])
            self.old = "förråd" 
    
    def returnLocation(self):
        return self.location
    
    def printMove(self):
        if self.old != self.location:
            print(f"\nFredrik flyttade sig från {self.old} till {self.location}\n")
        else:
            print(f"\nFredrik stannar i {self.old}\n")


