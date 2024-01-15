import random
import time
import asciimodule
from playsound import playsound

inventoryList = []
coinList = ["coin", "coin", "coin", "coin", "coin"]
CodeReal = str(random.randint(1000, 9999))

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

# menyn till spelet
def intro():
    asciimodule.menu()
    svar = input("\n")
    if svar == "1":
        return True
    elif svar == "2":
        return "option"

# inuti inställningar
def options():
    print(f"1-Fusk")
    print(f"2-Svårhet [{difficulty}]")
    print("3-Tutorial")
    print("4-Backa")
    svar = input("")
    if svar == "1":
        hacks = input("Fusk? ja/nej \n")
        if hacks == "ja":
          return "cheat"  
        if hacks == "nej":
            return "not cheat"

    elif svar == "2":
        diff()
    elif svar == "3":
        print("Tutorial")
        time.sleep(4)
        options()
    elif svar == "4":
        intro()
    options()

#väljer svårhetsgrad 
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

# lägger till objekt i listan
def inventoryAdd(object):
    inventoryList.append(object)

    

def codeUsed():
    CodeReal = "used"
    return CodeReal



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
            

# går man in i köket får man alternativet att leta runt, väljs det får man 13 cois samt koden till kassavalvet
def kitchen():
        svar = input("\nDu är i köket. Vad vill du göra? letarunt \n")
        if svar == "letarunt":
            print(f"Du hittade 2 coins och en lapp med numret {CodeReal}")
            inventoryAdd("Lapp med nummret " + CodeReal)
            coinList.append("coin")
            coinList.append("coin")
            return "found"
            
        
# likadant som ovanför fast här hittar du en till nyckel som läggs in i listan (inventory)
def restrooms():
    svar = input("Du befinner dig på toaletten, vill du leta runt?")
    if svar == "ja":
        print("Du hittade en nyckel och ett mynt")
        inventoryAdd("Nyckel 2")
        coinList.append("coin")
        return "found"
    
# i prishörnan kan du välja att köpa en nyckel, koden berättar om du kan köpa eller inte har råd, köper du en nyckel blir antalet nycklar 1 fler samt dina coins blir 3 färre
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
            while len(coinList) != 0:
                coinList.remove("coin")

            
            return "köpt"
            
        elif svar == "nej":
            break
    
def dead():
    playsound("freddy.mp3")
    asciimodule.fredrikjump()
    asciimodule.death()

