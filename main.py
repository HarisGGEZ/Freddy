import map
import animatronic
import rooms
import asciimodule
from playsound import playsound
from time import sleep
import keyboard

#defined temp choiceues
alive = True
hunt  = False
codeUsed = False
kitchenSearched = False
toiletSearched = False
bought = False
escaped = False
choice = None
karta = map.kartaKlass()
fredrik = animatronic.Fredrik()

# Start menyn
asciimodule.huvt()
sleep(0.3)
asciimodule.movment()
sleep(0.3)
while True:
    if rooms.intro() == "option":
        if rooms.options() == "cheat":
            fredrik.activateCheat()
    if keyboard.is_pressed("1"):
        break

#Hela spel loopen,
while True:
    while alive:
        if escaped == False:
                
                if fredrik.returnLocation() == karta.returnLocation() and karta.hunted("") == False:
                    karta.hunted("same")
                    try:
                        playsound("alert.mp3")
                    except:
                        pass
                karta.printChoice()
        
                keyboard.read_key()
                if keyboard.is_pressed("a"):
                    choice = "vänster"
                elif keyboard.is_pressed("d"):
                    choice = "höger"
                elif keyboard.is_pressed("w"):
                    choice = "fram"
                elif keyboard.is_pressed("s"):
                    choice = "ner"
                elif keyboard.is_pressed("m"):
                    choice = "karta"
                elif  keyboard.is_pressed("i"):
                    choice = "väska"
                elif keyboard.is_pressed("space"):
                    choice = "stanna"
                
                if choice == "karta":
                    karta.printMap()
                if choice == "väska":
                    rooms.inventory()
                if choice == "höger" or choice ==  "vänster" or choice ==  "fram" or  choice == "kök" or choice ==  "ner" or choice == "stanna":
                    if karta.move(choice) == "exit attempt":
                        if rooms.exit() == True:
                            print("Du lyckades fly!")
                            escaped = True
                        else:
                            print("Du har inte alla nycklar")
                    choice = None
                    if karta.hunted("") == True:
                        if karta.run() == 4:
                            alive = False
                    else:
                        fredrik.move()
                        fredrik.printMove()
                if karta.returnLocation() == "förrådet" and codeUsed== False:
                    if rooms.supplycloset() == "used":
                        codeUsed= True
                if karta.returnLocation() == "köket" and kitchenSearched == False:
                    if rooms.kitchen() == "found":
                        kitchenSearched = True
                if karta.returnLocation() == "toaletterna" and toiletSearched == False:
                    if rooms.restrooms() == "found":
                        toiletSearched = True
                if karta.returnLocation() == "prishörnan" and bought == False:
                    if rooms.prizecorner() == "köpt":
                        bought = True
                sleep(0.5) 
        
        if escaped == True:
            karta = map.kartaKlass()
            fredrik = animatronic.Fredrik()
            asciimodule.victory()
            print("Vill du spela igen? Y/N")
            keyboard.read_key()
            if keyboard.is_pressed("n"):
                break
            elif keyboard.is_pressed("y"):
                while True:
                    if rooms.intro() == "option":
                        if rooms.options() == "cheat":
                            fredrik.activateCheat()
                    if keyboard.is_pressed("1"):
                        break
                alive = True
                escaped = False
                hunt = False
                codeUsed= False
                kitchenSearched = False
                toiletSearched = False
                rooms.itemsReset()
    
    if alive == False:
        rooms.dead()
        karta = map.kartaKlass()
        fredrik = animatronic.Fredrik()
        print("Vill du spela igen? Y/N")
        keyboard.read_key()
        if keyboard.is_pressed("n"):
            break
        elif keyboard.is_pressed("y"):
            while True:
                if rooms.intro() == "option":
                    if rooms.options() == "cheat":
                        fredrik.activateCheat()
                if keyboard.is_pressed("1"):
                    break
            alive = True
            hunt = False
            codeUsed = False
            kitchenSearched = False
            toiletSearched = False
            rooms.itemsReset()