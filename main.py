import map
import animatronic
import rooms
import asciimodule
from playsound import playsound
from time import sleep
Alive = True
Jagad = False
kodAnvand = False
letatKok = False
letatToalett = False
bought = False
escaped = False
cheats = False
karta = map.kartaKlass()
fredrik = animatronic.Fredrik()

asciimodule.huvt()
if rooms.intro() == "option":
   if rooms.options() == "cheat":
        fredrik.activateCheat()

while True:
    while Alive:
        if escaped == False:
            if fredrik.returnLocation() == karta.returnPlats() and karta.jagad("") == False:
                karta.jagad("same")
                playsound("alert.mp3")
            karta.printVal()
            val = input()
            val = val.lower()
            if val == "karta":
                karta.printKarta()
            if val == "väska":
                rooms.inventory()
            if val == "höger" or val ==  "vänster" or val ==  "tillbaka"  or val ==  "fram" or  val == "kök" or val ==  "ner" or val == "stanna" or val == "upp":
                if karta.flytt(val) == "exit attempt":
                    if rooms.exit() == True:
                        print("Du lyckades fly!")
                        escaped = True
                    else:
                        print("Du har inte alla nycklar")
                if karta.jagad("") == True:
                    if karta.run() == 4:
                        rooms.dead
                        Alive = False
                else:
                    fredrik.move()
                    fredrik.printMove()
            if karta.returnPlats() == "förrådet" and kodAnvand == False:
                if rooms.supplycloset() == "used":
                    kodAnvand = True
            if karta.returnPlats() == "köket" and letatKok == False:
                if rooms.kitchen() == "found":
                    letatKok = True
            if karta.returnPlats() == "toaletterna" and letatToalett == False:
                if rooms.restrooms() == "found":
                    letatToalett = True
            if karta.returnPlats() == "prishörnan" and bought == False:
                if rooms.prizecorner() == "köpt":
                    bought = True
            sleep(0.5) 
        if escaped == True:
            retrywin = input("Du vann!!! spela igen?\n")
            retrywin = retrywin.lower()
            if retrywin == "ja":
                Alive = True
                escaped = False
                karta = map.kartaKlass()
                fredrik = animatronic.Fredrik()
                Jagad = False
                kodAnvand = False
                letatKok = False
                letatToalett = False
    if Alive == False:
        rooms.dead()
        retry = input("Vill du spela igen?\n")
        retry = retry.lower()
        if retry == "ja":
            Alive = True
            karta = map.kartaKlass()
            fredrik = animatronic.Fredrik()
            Jagad = False
            kodAnvand = False
            letatKok = False
            letatToalett = False
