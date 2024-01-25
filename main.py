import map
import animatronic
import rooms
import asciimodule
from playsound import playsound
from time import sleep
import keyboard
import msvcrt

Alive = True
Jagad = False
kodAnvand = False
letatKok = False
letatToalett = False
bought = False
escaped = False
cheats = False
val = None
karta = map.kartaKlass()
fredrik = animatronic.Fredrik()

asciimodule.huvt()
asciimodule.movment()
while True:
    if rooms.intro() == "option":
        if rooms.options() == "cheat":
            fredrik.activateCheat()
    if keyboard.is_pressed("1"):
        break

while True:
    while Alive:
        if escaped == False:
                
                if fredrik.returnLocation() == karta.returnPlats() and karta.jagad("") == False:
                    karta.jagad("same")
                    try:
                        playsound('./' + "alert.mp3")
                    except:
                        pass
                karta.printVal()
                
                msvcrt.getch()
                keyboard.read_key()
                if keyboard.is_pressed("a"):
                    val = "vänster"
                elif keyboard.is_pressed("d"):
                    val = "höger"
                elif keyboard.is_pressed("w"):
                    val = "fram"
                elif keyboard.is_pressed("s"):
                    val = "ner"
                elif keyboard.is_pressed("m"):
                    val = "karta"
                elif  keyboard.is_pressed("i"):
                    val = "väska"
                elif keyboard.is_pressed("space"):
                    val = "stanna"
                
                


                if val == "karta":
                    karta.printKarta()
                if val == "väska":
                    rooms.inventory()
                if val == "höger" or val ==  "vänster" or val ==  "fram" or  val == "kök" or val ==  "ner" or val == "stanna":
                    if karta.flytt(val) == "exit attempt":
                        if rooms.exit() == True:
                            print("Du lyckades fly!")
                            escaped = True
                        else:
                            print("Du har inte alla nycklar")
                    val = None
                    
                    if karta.jagad("") == True:
                        if karta.run() == 4:
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
            asciimodule.victory()
            print("Vill du spela igen?")
            retrywin = retrywin.lower()
            if retrywin == "ja":
                while True:
                    if rooms.intro() == "option":
                        if rooms.options() == "cheat":
                            fredrik.activateCheat()
                    if keyboard.is_pressed("1"):
                        break
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
        retry = input("LOSER YOU DIED!!! BIG L!!! Vill du spela igen?\n")
        retry = retry.lower()
        if retry == "ja":
            while True:
                if rooms.intro() == "option":
                    if rooms.options() == "cheat":
                        fredrik.activateCheat()
                if keyboard.is_pressed("1"):
                    break
            Alive = True
            karta = map.kartaKlass()
            fredrik = animatronic.Fredrik()
            Jagad = False
            kodAnvand = False
            letatKok = False
            letatToalett = False
    