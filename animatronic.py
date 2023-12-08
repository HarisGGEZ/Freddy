from random import choice
Location = "Stage"
OldLocation = "Stage"




class bonnie():
    
    def __init__(self):
        self.location = "Stage"
        self.old = None
    
    def move(self):
        if self.location == "Stage":
            self.location = "Dining Area"
            self.old = "Stage"
        elif self.location == "Dining Area":
            self.location = choice([self.location, "Stage", "East Hall", "Backstage" ])
            self.old = "Dining Area"
        elif self.location ==  "Backstage":
            self.location = choice([self.location, "Dining Area"])
            self.old = "Backstage"
        elif self.location == "East Hall":
            self.location = choice([self.location, "Dining Area", "Supply Closet"])
            self.old = "East Hall"
        elif self.location == "Supply Closet":
            self.location = choice([self.location, "East Hall"])
            self.old = "Supply Closet"
        
        if self.old != self.location:
            print(f"Bonnie moved from {self.old} to {self.location}")
        else:
            print(f"Bonnie stays in {self.old}")
        
Bonnie = bonnie()




while True:
    
    test = input("")
    if test == "1":
        Bonnie.move()

