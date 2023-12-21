import map
import animatronic
import fnafgamereal
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
    if val == "höger" or val ==  "vänster" or val ==  "tillbaka"  or val ==  "fram" or  val == "kök" or val ==  "ner":
        karta.flytt(val)
        if Jagad == True:
            if karta.run() == 5:
                print("dead")
                break
        fredrik.move()
    fredrik.printMove()
    if fredrik.returnLocation() == karta.returnPlats():
        karta.jagad("same")
    if karta.jagad("") == True:
        Jagad = True
    
    
  