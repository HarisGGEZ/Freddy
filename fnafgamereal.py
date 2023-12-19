import random
import time

office = False
westhall = False
easthall = False
supplycloset = False
diningroom = False
piratecove = False
backstage = False
showstage = False
kitchen = False
restrooms = False
escape = False

#temp values
nummerlapp = False
difficulty = 1
keys = 0
cheats = False
switch = "av"
valvkod = 0
valvtom = False
coins = 0
tkey = False


def inventory():
    print("Inventory:\n")
    if coins > 1:
        print(f"Mynt: {coins} st\n")
    if keys > 1:
        print(f"Nycklar: {keys} st\n")
    if valvkod == True:
        print(valvkod)

def intro():
    print("Välkommen till fredriks")
    print("1-Spela")
    print("2-Options")
    svar = input()
    if svar == "1":
        play()
    elif svar =="2":
        options()


def options():
    global cheats
    global switch
    print(f"1-Fusk {switch}")
    print(f"2-Svårhet [{difficulty}]")
    print("3-Tutorial")
    print("4-Backa")
    svar = input("")
    if svar == "1":
        hacks = input("Fusk? ja/nej \n")
        if hacks == "ja":
            cheats = True
            switch = "på"
            options()
        if hacks == "nej":
            cheats = False
            switch = "av"
            options()     
    elif svar == "2":
        diff()
    elif svar == "3":
        print("Tutorial")
        time.sleep(4)
        options()
    elif svar == "4":
        intro()
    options()

def diff():
    print("Välj en svårhet mellan 1-3 \n1=Enkel \n2=Svår \n3=Extrem")
    global difficulty
    difficulty = input()
    if difficulty == "1":
        difficulty = 1
    elif difficulty == "2":
        difficulty = 2
    elif difficulty == "3":
        difficulty = 3
    else:
        print("snälla skriv ett nummer mellan 1-3")
        diff()
    
def play():
    global coins
    global valvkod
    if difficulty == 1:
        valvkod = random.randint(1000, 9999)
    elif difficulty == 2:
        valvkod = random.randint(10000, 99999)
    elif difficulty == 3:
        valvkod = random.randint(100000, 999999)
    if cheats == True:
        coins = 999
    print("Du måste nu fly från pizzerian \n Du kommer få alternative på vilka rum du kan gå till \n Du måste hitta 3 nycklar för att komma ut, lycka till")
    office()

def office():
    office = True
    print("Du befinner dig i security rummet")
    print("Du kan gå \nvänster\nhöger")
    while True:
        direction = input("Vart vill du gå? \n")
        direction = direction.lower()
        if direction == "höger":
            easthall()
            break      
        elif direction == "vänster":
            westhall()
            break
        elif direction == "m":
            print(officem)
        elif direction == "inv":
            inventory()
        office = False

def westhall():
    westhall = True
    print("Du befinner dig vänster om kontoret")
    direction = input("Vart vill du gå? \nfram\ntillbaks\nförråd")
    direction = direction.lower()
    if direction == "fram":
        diningroom()
    elif direction == "tillbaks":
        ()
    elif direction == "förråd":
        supplycloset()
    easthall = False



def easthall():
    easthall = True
    print("\nDu befinner dig höger om kontoret")
    print("Du kan gå \nFram\nTillbaks")
    direction = input("Vart vill du gå? \n")
    direction = direction.lower()
    if direction == "fram":
        diningroom()
    elif direction == "tillbaks":
        ()
    easthall = False

def supplycloset():
    global valvtom
    supplycloset = True
    print("\nDu är i supplycloset")
    print("Du ser ett kassavalv")
    svar = input("\nVad vill du göra? \n lämna \n kassavalv\n")
    if svar == "lämna":
        westhall()
    elif svar == "kassavalv":
        while True:
            svar = input("Hmmmm, här behövs en kod. Gissa kod? ja/nej")
            if svar == "nej":
                (westhall)
                break
            elif svar == "ja" and valvtom == False:
                kodsvar = input("Kod:")
                if kodsvar == valvkod:
                    print("Grattis du hittade en nyckel")
                    keys = keys+1
                    valvtom = True
                    break
            elif svar == "ja" and valvtom == True:
                print("Valvet är tomt")
                break


def kitchen():
    global valvkod
    global nummerlapp
    global coins
    kitchen = True
    while True:
        svar = input("\nDu är i köket. Vad vill du göra? \ntillbaks/letarunt \n")
        if svar == "tillbaks":
            diningroom()
            break
        elif svar == "letarunt" and nummerlapp == True:
            print("Det finns inget här")
        elif svar == "letarunt":
            print(f"Du hittade 13 coins och en lapp med numret {valvkod}")
            coins = coins + 16
            print("+1 nummer lapp")
            nummerlapp = True
        
    
def diningroom():
    diningroom = True
    print("\nDu befinner dig nu i party rummet här finns många rum så tappa inte bort dig")
    direction = input("Vart vill du gå? \nköket \nbackstage \nexit \nToa")
    if direction == "exit":
        escape()
    elif direction == "köket":
        kitchen()
    elif direction == "prishörnet":
        prizecorner()
    elif direction == "toa":
        restrooms()
    
def restrooms():
    svar = input("Vad vill du göra? \n tillbaks")
    if svar == "tillbaks":
        diningroom()
    if tkey == False:
        print("You found a key +1 key")
        keys = keys + 1
        tkey == True
    elif tkey == True:
        print("There is nothing here")
    



def prizecorner():
    global coins
    print("Du befinner dig i prishörnan du ser en nyckel som kostar 50 coins")
    svar = input("Vad vill du göra? \n tillbaks \n nyckel")
    while True:
        if svar == "nyckel" and coins == 50:
            svar = input("Vill du köpa nyckeln ja/nej")
        else:
            print(f"Du har inte råd du har {coins}coins")
        if svar == "ja":
            keys = keys + 1
            coins = coins - 50
            break
        elif svar == "nej":
            break
        elif svar == "nyckel" and coins < 50:
            print("Du har inte tillräkligt med coins")
            break



def escape():
    escape = True
    if cheats == True or keys == 3:
        svar = input("Vill du fly? ja/nej")
        if svar == "ja":
            end()
        elif svar == "nej":
            diningroom()
    elif keys < 3:
        print(f"Du kan bara fly när du har fått 3 nycklar, Just nu har du {keys} nycklar.")
        diningroom()

def end():
    print("Grattis du lyckades fly!")
    time.sleep(10)
    intro()

def death():
    print("\nYou died\n")
    time.sleep(5)
    intro()


while True:
    intro()
    if office == True:
        currentmap = officem
