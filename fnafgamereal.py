import random
import time

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
nummerlapp = False
difficulty = 1
keys = 0
cheats = False
switch = "av"
valvkod = 0

officem = '''                                                                                                                                                                                                                                                                                                                                                                                       
                                            ''...............................''                                              
                                           .,.                               .;.    ..  ..                                   
                                           .,.                               .,.    ',  .,.                                  
                                           .,.                               .;.    ',  .,.                                  
                                           .:'                               ':.    ,,  .;.                                  
       .,'.........,.  .,..................','...............................','....'.   .'.......,'                         
       .,          ,:..;'                                                                         .,                         
       .,          ..  ..                                                                         .,     .......             
       .,          ,;..;'                                                                         .,  .,,......;'            
       .,          ,'  ''                                                                         .,  .,.      .,            
       .,          ,'  ''                                                                         .:..,;.      .,            
       .,          ,'  ''                                                                         .;'.',.      .,            
       .,          ,'  ''                                                                         .;'.,,.      .,   .........
       .,          ,'  ''                                                                         .:..,:.      ':..,c'......:
       .:..........;'  ''                                                                         .,  .,.      ':..,:.      ,
        ............   ''                                                                         .,  .,.      ':'.;:.      ,
                     ..,,                                                                         .,  .,.      ';..':,......:
           .,,.........:,                                                                         .,  .,.      .,   .........
           .,.         ''                                                                         .,  .,.      .,            
           .,.         .'                                                                         .,  .,.      .,            
           .,.         .'                                                                         .,  .,.      .,   .'......'
           .,.         .'                                                                         .,  .,.      ':'.;:.      ;
           .,.         .'                                                                         .,  .,.      ';..';.      ,
           .;,.........;,                                                                         .,  .,.      ':'.;:.      ,
            ...........;:.........................................................................;,  .,,......;,  .,,......;
                        .................;;..':.............................;;..,;........,:...:,..                   ..     
                                     .'..;,..';'.'.                     .'..;,..,;..'.   .;;...;,.................'.         
                                     ,,          .;.                   .;.          ,,   ,,                       ,,         
                      ............   ,'          .,.                   .,.          ',   ''                       ''         
                     ';.........';.  ,'          .,.                   .,.          ',   ''                       ',         
                     ''         .,.  ,'          .,.                   .,.          ',   ''                       ',         
                     ',         .,.  ,'          .,.                   .,.          ',   ''                       ',         
                     ',         .;;..;'          .,.                   .,.          ',   ''                       ',         
                     ',          ',..,.          .,.                   .,.          ',   ''                       ''         
                     ''          ,,..;.          .,.                   .,.          ',   ''                       ''         
                     ''         .;;..;'          .,.                   .,.          ',   ,,                       ,,         
                     ''         .,.  ,'          .,.   .............   .,.          ',   .'.......................'.         
                     ''         .,.  ,'          .,.  ,;...........;,  .;.          ',                                       
                     ';.........';.  ,'          .,.  ,'           .,  .,.          ',                                       
                      ...........    ,'          .,.  ,'           ',  .,.          ',                                       
                                     ,'          .;,..:'           ':'.,;.          ',                                       
                                     ,'           ''..,. Du är här .,..''.          ',                                       
                                     ,'          .,,.';.           .;'.,,.          ',                                       
                                     ,'          .;,..;'           ';..';.          ',                                       
                                     ,'          .;.  ,'           ',  .;.          ',                                       
                                     ,c,,,,,,,,,,::.  ;c,,,,,,,,,,,c;  .::,,,,,,,,,,c,                                       '''




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
    global cheats
    global switch
    print(f"1-Fusk {switch}")
    print(f"2-Svårhet [{difficulty}]")
    print("3-Tutorial")
    print("4-Backa")
    svar = input("")
    if svar == "1":
        hacks = input("Fusk? ja/nej \n")
        if hacks == "ja":
            cheats = True
            switch = "på"
            options()
        if hacks == "nej":
            cheats = False
            switch = "av"
            options()     
    elif svar == "2":
        diff()
    elif svar == "3":
        print("Tutorial")
    elif svar == "4":
        intro()
    options()



def diff():
    print("Välj en svårhet mellan 1-3 \n 1=Enkel 2=Svår 3=Extrem")
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
    global valvkod
    if difficulty == 1:
        valvkod = random.randint(1111, 9999)
    elif difficulty == 2:
        valvkod = random.randint(10000, 99999)
    elif difficulty == 3:
        valvkod = random.randint(100000, 999999)
    print("Du måste nu fly från pizzerian \n Du kommer få alternative på vilka rum du kan gå till \n Du måste hitta 3 nycklar för att komma ut, lycka till")
    office()

def office():
    office = True
    print("Du befinner dig i security rummet")
    print("Du kan gå vänster/höger")
    direction = input("Vart vill du gå? \n")
    if direction == "höger":
        easthall()      
    elif direction == "vänster":
        westhall()
    elif direction == "m":
        print(officem)
    office = False

def westhall():
    westhall = True
    print("Du befinner dig höger om kontoret")
    direction = input("Vart vill du gå? \n")
    if direction == "fram":
        diningroom()
    elif direction == "tillbaks":
        ()
    easthall = False



def easthall():
    easthall = True
    print("Du befinner dig höger om kontoret")
    print("Du kan gå fram/tillbaks")
    direction = input("Vart vill du gå? \n")
    if direction == "fram":
        diningroom()
    elif direction == "tillbaks":
        ()
    easthall = False

def supplycloset():
    supplycloset = True
    print("Du är i supplycloset")
    print("Du ser ett kassavalv")
    svar = input("Vad vill du göra? \n lämna \n kassavalv")
    if svar == "lämna":
        westhall()
    elif svar == "kassavalv":
        svar = input("Hmmmm, här behövs en kod. Gissa kod? ja/nej")
        if svar == "nej":
            (westhall)
        elif svar == "ja":
            kodsvar = input("Kod:")


def kitchen():
    global valvkod
    global nummerlapp
    kitchen = True
    svar = input("Du är i köket. Vad vill du göra? \ntillbaks/letarunt \n")
    if svar == "tillbaks":
        diningroom()
    elif svar == "letarunt":
        print(f"Du hittade en lapp med numret {valvkod}")
        print("+1 nummer lapp")
        nummerlapp = True
        
    

def diningroom():
    diningroom = True
    print("Du befinner dig nu i party rummet här finns många rum så tappa inte bort dig")
    direction = input("Vart vill du gå? \nköket \nbackstage \nexit \n")
    if direction == "exit":
        escape()
    if direction == "köket":
        kitchen()



def prizecorner():
    ()
def escape():
    escape = True
    if keys == 3:
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
    print("You died")


while True:
    intro()
    if office == True:
        currentmap = officem


