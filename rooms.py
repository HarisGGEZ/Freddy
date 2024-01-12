import random
import time
import asciimodule
from playsound import playsound

inventoryList = []
coinList = ["coin", "coin", "coin", "coin", "coin"]

#temp values
cheat_text = False
difficulty = 1
cheats = False
switch = "av"
coins = 0


def inventory():
    print("I din väska:\n")
    inventoryList.sort()
    print(*inventoryList, sep="\n")
    print(f"Du har {len(coinList)} mynt")

def exit():
    if "Nyckel 1" in inventoryList and "Nyckel 2" in inventoryList and "Nyckel 3" in inventoryList:
        return True

def intro():
    asciimodule.huvt()
    #asciimodule.menu()
    svar = input("1. Spela \n2. Inställningar")
    if svar == "1" or "spela":
        return True
    elif svar =="2" or "options":
        print("options")


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
                        print("Grattis du hittade en nyckel och två mynt")
                        inventoryAdd("Nyckel 1")
                        coinList.append("coin")
                        coinList.append("coin")
                        return "used"       
                elif kodsvar != CodeReal:
                    print(CodeReal)
                    print("Fel kod")
            


def kitchen():
        svar = input("\nDu är i köket. Vad vill du göra? letarunt \n")
        if svar == "letarunt":
            print(f"Du hittade 2 coins och en lapp med numret {CodeReal}")
            inventoryAdd("Lapp med nummret " + CodeReal)
            coinList.append("coin")
            coinList.append("coin")
            return "found"
            
        
    
def restrooms():
    svar = input("Du befinner dig på toaletten, vill du leta runt?")
    if svar == "ja":
        print("Du hittade en nyckel och ett mynt")
        inventoryAdd("Nyckel 2")
        coinList.append("coin")
        return "found"
    

def prizecorner():
    print("Du befinner dig i prishörnan du ser en nyckel som kostar 5 coins")
    svar = input("Vad vill du göra? \n tillbaks \n nyckel")
    while True:
        if svar == "nyckel" and len(coinList) == 5:
            svar = input("Vill du köpa nyckeln ja/nej")
        else:
            print(f"Du har inte råd")
            break 
        if svar == "ja":
            inventoryAdd("Nyckel 3")
            for coin in coinList:
                coinList.remove(coin)

            
            return "köpt"
            
        elif svar == "nej":
            break
    
def dead():
    playsound(freddy.mp3)
    asciimodule.fredrikjump()
    asciimodule.death()

