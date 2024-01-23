import random
import time
import asciimodule
from playsound import playsound
import keyboard
import msvcrt

inventoryList = []
coinList = []
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
    while True:
        msvcrt.getch()
        if keyboard.is_pressed("1"):
            break
        if keyboard.is_pressed("2"):
            return "option"

# inuti inställningar
def options():
    while True:
        print(f"1. Fusk")
        #print(f"2-Svårhet [{difficulty}]")
        print("3. Tutorial")
        print("4. Backa\n")
        msvcrt.getch()
        if keyboard.is_pressed("1"):
            print("Vill göra så att Fredrik inte rör sig? Y/N \n")
            msvcrt.getch()
            if keyboard.is_pressed("y"):
                return "cheat"  
            if keyboard.is_pressed("n"):
                return "not cheat"
        #elif svar == "2":
            #diff()
        elif keyboard.is_pressed("3"):
            print("Tutorial")
            time.sleep(4)
            break
        elif keyboard.is_pressed("4"):
            break
        

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
            print("Hmmmm, här behövs en kod. \nVill du gissa koden? Y/N\n")
            if keyboard.is_pressed("y"):
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
        print("\nDu är i köket. Vill du leta runt? Y/N \n")
        if keyboard.is_pressed("y"):
            print(f"Du hittade 2 mynt och en lapp med numret {CodeReal}")
            inventoryAdd("Lapp med nummret " + CodeReal)
            coinList.append("coin")
            coinList.append("coin")
            return "found"
            
        
# likadant som ovanför fast här hittar du en till nyckel som läggs in i listan (inventory)
def restrooms():
    print("Du befinner dig på toaletten, vill du leta runt? Y/N")
    if keyboard.is_pressed("y"):
        print("Du hittade en nyckel och ett mynt")
        inventoryAdd("Nyckel 2")
        coinList.append("coin")
        return "found"
    
# i prishörnan kan du välja att köpa en nyckel, koden berättar om du kan köpa eller inte har råd, köper du en nyckel blir antalet nycklar 1 fler samt dina coins blir 3 färre
def prizecorner():
    print("Du befinner dig i prishörnan du ser en nyckel som kostar 5 mynt")
    while True:
        print("Vill du köpa nyckeln ja/nej\n")
        if keyboard.is_pressed("y") and len(coinList) == 5:
                inventoryAdd("Nyckel 3")
                while len(coinList) != 0:
                    coinList.remove("coin")
                return "köpt"

        else:
            print(f"Du har inte råd")
            break 
    
def dead():
    playsound("freddy.mp3")
    asciimodule.death()

