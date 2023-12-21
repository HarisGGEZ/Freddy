import random
import time
import asciimodule

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
cheat_text = False
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
    print("I din väska:\n")
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
    global fusk
    global difficulty
    print(f"1-Fusk {switch}")
    print(f"2-Svårhet [{difficulty}]")
    print("3-Tutorial")
    print("4-Backa")
    svar = input("")
    if svar == "1":
        hacks = input("Fusk? ja/nej \n")
        if hacks == "ja":
            cheats = True
            fusk = "på"
            options()
        if hacks == "nej":
            cheats = False
            fusk = "av"
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
    global cheat_text
    if difficulty == 1:
        valvkod = random.randint(1000, 9999)
    elif difficulty == 2:
        valvkod = random.randint(10000, 99999)
    elif difficulty == 3:
        valvkod = random.randint(100000, 999999)
    if cheats == True:
        cheat_text == True
        coins = 999
    print("lycka till")
    office()

def supplycloset():
    global valvtom
    supplycloset = True
    print("\nDu är i supplycloset")
    print("Du ser ett kassavalv")
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
    global coins
    global nummerlapp
    kitchen = True
    while True:
        svar = input("\nDu är i köket. Vad vill du göra? letarunt \n")
        if svar == "letarunt" and nummerlapp == True:
            print("Det finns inget här")
        elif svar == "letarunt":
            print(f"Du hittade 13 coins och en lapp med numret {valvkod}")
            coins = coins + 1
            print("+1 nummer lapp")
            nummerlapp = True
        
    
def restrooms():
    svar = input("Du befinner dig på toaletten")
    if tkey == False:
        print("Du hittade en nyckel +1 nyckel")
        keys = keys + 1
        tkey == True
    svar1 = input("Vill du leta vidare? ja/nej")
    if svar == "ja" and tcoin == False:
        print("Du letade runt i toaletten och hittade")


        

    elif tkey == True:
        print("Det finns inget här")
        time.sleep(1)
    

def prizecorner():
    print("Du befinner dig i prishörnan du ser en nyckel som kostar 50 coins")
    svar = input("Vad vill du göra? \n tillbaks \n nyckel")
    while True:
        if svar == "nyckel" and coins == 3:
            svar = input("Vill du köpa nyckeln ja/nej")
        else:
            print(f"Du har inte råd du har {coins}coins")
        if svar == "ja":
            keys = keys + 1
            coins = coins - 3
            break
        elif svar == "nej":
            break
        elif svar == "nyckel" and coins < 3:
            print("Du har inte tillräkligt med coins")
            break

def diningroom():
    indining = indining + 1
    if indining < 1:
        print("Du hittade ett mynt! +1 mynt")
        coins = coins + 1
    if indining > 2:
        end



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

