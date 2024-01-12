import random
import time
import asciimodule
from playsound import playsound

inventoryList = []

#temp values
cheat_text = False
difficulty = 1
cheats = False
switch = "av"
coins = 0


def inventory():
    print("I din väska:\n")
    if coins > 1:
        print(f"\033[91Mynt: {coins} st [0m\033\n")
    inventoryList.sort()
    print(*inventoryList, sep="\n")

def exit():
    if "Nyckel 1" in inventoryList and "Nyckel 2" in inventoryList:
        return True

def intro():
    asciimodule.huvt()
    asciimodule.menu()
    svar = input()
    if svar == "1" or "spela":
        play()
    elif svar =="2" or "options":
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
    
def inventoryAdd(object):
    inventoryList.append(object)

    

def codeUsed():
    CodeReal = "used"
    return CodeReal


CodeReal = str(random.randint(1000, 9999))


def supplycloset():
            print("\nDu är i förrådet")
            print("Du ser ett kassavalv")
            svar = input("Hmmmm, här behövs en kod. \nVill du gissa koden? ja/nej\n")
            if svar == "ja":
                print(CodeReal)
                kodsvar = input("Kod: ")
                if kodsvar == CodeReal:
                        print("Grattis du hittade en nyckel")
                        inventoryAdd("Nyckel 1")
                        return "used"       
                elif kodsvar != CodeReal:
                    print(CodeReal)
                    print("Fel kod")
            


def kitchen():
        svar = input("\nDu är i köket. Vad vill du göra? letarunt \n")
        if svar == "letarunt":
            print(f"Du hittade 13 coins och en lapp med numret {CodeReal}")
            inventoryAdd("Lapp med nummret " + CodeReal)
            return "found"
            
        
    
def restrooms():
    svar = input("Du befinner dig på toaletten, vill du leta runt?")
    if svar == "ja":
        print("Du hittade en nyckel")
        inventoryAdd("Nyckel 2")
        return "found"
    

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
    
def dead():
    playsound(freddy.mp3)
    asciimodule.fredrikjump()
    asciimodule.death()

