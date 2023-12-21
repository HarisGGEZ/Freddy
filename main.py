import map
import animatronic
import fnafgamereal
from playsound import playsound
Jagad = False

karta = map.kartaKlass()
fredrik = animatronic.Fredrik()





while True:
    karta.printVal()
    val = input()
    val = val.lower()
    if val == "karta":
        karta.printKarta()
    if val == "väska":
        fnafgamereal.inventory()
    if val == "höger" or val ==  "vänster" or val ==  "tillbaka"  or val ==  "fram" or  val == "kök" or val ==  "ner" or val == "stanna":
        karta.flytt(val)
        if karta.jagad("") == True:
            if karta.run() == 5:
                playsound('/audio/freddy.mp3')
                print("dead")
                break
        fredrik.move()
    fredrik.printMove()
    if fredrik.returnLocation() == karta.returnPlats():
        karta.jagad("same")
    #if karta.jagad("") == True:
        #Jagad = True
    
    
  