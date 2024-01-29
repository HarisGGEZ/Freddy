from time import sleep
import keyboard

class kartaKlass():
    # Värden som klassen får när den skapas
    def __init__(self):
        self.o = ">-O"
        self.e = "   "
        self.w = "   "
        self.s = "   "
        self.k = "   "
        self.d = "   "
        self.b = "   "
        self.t = "   "
        self.old = None
        self.location = "kontoret"
        self.hunt = False
        self.steps = 0
        self.ner = None
        
    # Printar en bild av kartan
    def printMap(self):
        print(f'''                                                                                                                                                                                                                                                                                                                                                                                       
                                            ''...............................''                                              
                                            .,.                               .;.    .............                                   
                                            .,.                               .,.    ', \033[91mUtgång\033[0m  .,.                                  
                                            .,.                               .;.    ',         .,.                                  
                                            .:'                               ':.    ,,         .;.                                  
        .,'.........,.  .,..................','...............................','....'.          ...,'                         
        .,  \033[91mPrishörnan\033[0m                                                                            .,                         
        .,                                                                                         .,     .......             
        .,          ,;..;'                                                                         .,  .,,......;'            
        .,          ,'  ''                                                                         .,  .,.      .,            
        .,   {self.b}    ,'  ''                                                                         .:..,;.      .,            
        .,          ,'  ''                                                                                     .,            
        .,          ,'  ''                                                                                      .,   .........
        .,          ,'  ''                                                                         .:..,:.      ':..,c'......:
        .:..........;'  ''                              \033[91mMatsal\033[0m                                     .,  .,.      ':..,:.      ,
        ............   ''                                {self.d}                                       .,  .,.      ':'.;:.      ,
                        ..,,                                                                       .,  .,. {self.t}  ';..':,......:
            .,,.........:,                                                                         .,  .,.      .,   .........
            .,.         ''                                                                         .,  .,.      .,            
            .,.         .'                                                                         .,  .,.      .,            
            .,.         .'                                                                         .,  .,.      .,   .'......'
            .,.         .'                                                                         .,  .,.      ':'.;:.      ;
            .,.         .'                                                                         .,  .,.      ';..';.      ,
            .;,.........;,                                                                         .,  .,.      ':'.;:.      ,
            ...........;:...................      .............................       .........   ....;,  .,,......;,  .,,...;
                           .................      .............................       .......,:   :,..                   ..     
                                        .'          '.                     .'          '.   .;;   ;,.................'.         
                                        ,,          .;.                   .;.          ,,   ,,         \033[91mKöket\033[0m         ,,         
                        ............   ,'          .,.                   .,.          ',   ''                       ''         
                        ';.........';.  ,'          .,.                   .,.          ',   ''                       ',         
                        '' \033[91mFörråd\033[0m  .,.  ,'          .,.                   .,.          ,'   ''                        ',         
                        ',         .,.  ,'          .,.                   .,.          ',   ''        {self.k}           ',         
                        ',         .;;..;'          .,.                   .,.          ',   ''                       ',         
                        ',                          .,.                   .,.          ',   ''                       ''         
                        ''   {self.s}    ,,..;.          .,.                   .,.          ',   ''                       ''         
                        ''         .;;..;'          .,.                   .,.          ',   ,,                       ,,         
                        ''         .,.  ,'          .,.   .............   .,.          ',   .'.......................'.         
                        ''         .,.  ,'          .,.  ,;...........;,  .;.          ',                                       
                        ';.........';.  ,'          .,.  ,'  \033[91mKontor\033[0m   .,  .,.          ',                                       
                        ...........    ,'          .,.  ,'           ',  .,.          ',                                       
                                        ,'          .;,..:'           ':'.,;.          ',                                       
                                        ,'    {self.w}              {self.o}              {self.e}    ',                                       
                                        ,'          .,,.';.           .;'.,,.          ',                                       
                                        ,'          .;,..;'           ';..';.          ',                                       
                                        ,'          .;.  ,'           ',  .;.          ',                                       
                                        ,c,,,,,,,,,,::.  ;c,,,,,,,,,,,c;  .::,,,,,,,,,,c,                                       '''
        )
        
        
    # Förflyttelse beroende på nuvarande plats
    def move(self, move):
        
        if move == "vänster" and self.o == ">-O":
            self.o = "   "
            self.old = "kontor"
            self.e = "   "
            self.w = ">-O"
            
        elif move == "höger" and self.o == ">-O":
            self.o = "   "
            self.old = "kontor"
            self.e = ">-O"
        
        elif move == "vänster" and self.w == ">-O":
            self.old = "väst"
            self.s = ">-O"
            self.w = "   "
            
        elif move == "fram" and (self.e == ">-O" or self.w == ">-O"):
            if self.e == ">-O":
                self.old = "öst"
            if self.w == ">-O":
                self.old = "väst"
            self.d = ">-O"
            self.e = "   "
            self.w = "   "

        elif move == "vänster" and self.e == ">-O":
            self.old = "öst"
            self.o = ">-O"
            self.e = "   "
        
        elif move == "höger" and self.w == ">-O":
            self.old = "väst"
            self.o = ">-O"
            self.w = "   "

        elif move == "höger" and self.s == ">-O":
            self.old = "förråd"
            self.s = "   "
            self.w = ">-O"
            
        elif move == "vänster" and self.d == ">-O":
            self.old = "matsal"
            self.b = ">-O"
            self.d = "   "

        elif move == "höger" and self.d == ">-O":
            self.old = "matsal"
            self.t = ">-O"
            self.d = "   "

        elif move == "fram" and self.d == ">-O":
            return "exit attempt"

        elif move == "ner" and self.d == ">-O":
            sleep(0.3)
            print("(\033[91md\033[0m) Höger Hall, (\033[91ma\033[0m) Vänster Hall eller (\033[91ms\033[0m) Köket")
            keyboard.read_key()
            if keyboard.is_pressed("a"):
                    self.ner = "vänster"
            if keyboard.is_pressed("d"):
                    self.ner = "höger"
            if keyboard.is_pressed("s"):
                self.ner = "kök"

            if self.d == ">-O" and self.ner == "vänster":
                self.old = "matsal"
                self.w = ">-O"
                self.d = "   "
        
            if self.d == ">-O" and self.ner == "höger":
                self.old = "matsal"
                self.e = ">-O"
                self.d = "   "
        
            if self.d == ">-O" and self.ner == "kök" :
                self.old = "matsal"
                self.k = ">-O"
                self.d = "   "
        
        elif move == "höger hall" and self.d == ">-O":
            self.old = "matsal"
            self.w = ">-O"
            self.d = "   "

        elif move == "höger" and self.d == ">-O":
            self.old = "matsal"
            self.t = ">-O"
            self.d = "   "
        
        elif move == "höger" and self.b == ">-O":
            self.old = "prishörna"
            self.d = ">-O"
            self.b = "  "
        
        elif move == "vänster" and self.t == ">-O":
            self.old = "toaletter"
            self.d = ">-O"
            self.t = "  "
        
        elif move == "kök" and self.d == ">-O":
            self.old = "matsal"
            self.k = ">-O"
            self.d = "   "

        elif move == "fram":
            if self.old == "kök":
                self.old = "matsal"
                self.k = ">-O"
                self.d = "   "

            elif self.old == "matsal":
                if self.e == ">-O":
                    self.old = "öst"
                if self.w == ">-O":
                    self.old = "väst"
                if self.b == ">-O":
                    self.old = "prishörna"
                if self.t == ">-O":
                    self.old = "toaletter"
                if self.k == ">-O":
                    self.old = "kök"
                self.d = ">-O"
                self.e = "   "
                self.w = "   "
                self.b = "   "
                self.t = "   "
                self.k = "   "

            elif self.old == "förråd":
                self.old = "väst"
                self.s = ">-O"
                self.w = "   "
            
            elif self.old == "väst":
                if self.s == ">-O":
                    self.old = "förråd"
                if self.d == ">-O":
                    self.old = "matsal"
                if self.o == ">-O":
                    self.old = "Kontor"
                self.w = ">-O"
                self.s = "   "
                self.o = "   "
                self.d = "   "
        
            elif self.old == "öst":
                if self.d == ">-O":
                    self.old = "matsal"
                if self.o == ">-O":
                    self.old = "kontor"
                self.e = ">-O"
                self.d = "   "
                self.o = "   "

            elif self.old == "kontor":
                if self.e == ">-O":
                    self.old = "öst"
                if self.w == ">-O":
                    self.old = "väst"
                self.o = ">-O"
                self.e = "   "
                self.w = "   "

            elif self.old == "toaletter":
                self.old = "matsal"
                self.t = ">-O"
                self.d = "   "

            elif self.old == "prishörna":
                self.old = "matsal"
                self.b = ">-O"
                self.d = "   "
    
    # Visar vart man kan röra sig
    def printChoice(self):
        Plats = self.location.capitalize()
        print(f"\nDu befinner dig i {Plats}. \nDu kan gå:")
        sleep(0.5)
        if self.o == ">-O":
            print("(\033[91ma\033[0m) Vänster till Vänstra Hallen \n(\033[91md\033[0m) Höger till Högra Hallen")
        if self.w == ">-O":
            print("(\033[91ma\033[0m) Vänster till Förrådet \n(\033[91md\033[0m) Höger till Kontoret \n(\033[91mw\033[0m) Fram till Matsalen ")
        if self.e == ">-O":
            print("(\033[91ma\033[0m) Vänster till Kontoret \n(\033[91mw\033[0m) Fram till Matsalen")
        if self.s == ">-O":
            print("(\033[91md\033[0m) Höger till Vänstra Hallen")
        if self.d == ">-O":
            print("(\033[91ma\033[0m) Vänster till Prishörnan \n(\033[91md\033[0m) Höger till toaletterna. \n(\033[91ms\033[0m) Ner till Högra eller Vänstra hall eller Köket. \n(\033[91mw\033[0m) Fram till Utgången (Alla nycklar krävs)")
        if self.t == ">-O":
            print("(\033[91ma\033[0m) Vänster till Matsalen")
        if self.b == ">-O":
            print("(\033[91md\033[0m) Höger till Matsalen")
        if self.k == ">-O":
            print("(\033[91mw\033[0m) Tillbaka till Matsalen")
        print("\n")
    
    # Skickar tillbaka nuvarande position
    def returnLocation(self):
        if self.o == ">-O":
            self.location = "kontoret"
        if self.w == ">-O":
            self.location = "vänster hall"
        if self.e == ">-O":
            self.location = "höger hall"
        if self.s == ">-O":
            self.location = "förrådet"
        if self.d == ">-O":
           self.location = "matsalen"
        if self.t == ">-O":
          self.location = "toaletterna"
        if self.b == ">-O":
            self.location = "prishörnan"
        if self.k == ">-O":
            self.location = "köket"
        return self.location
    
    # Kollar ifall man blir jagad.
    def hunted(self, roomStatus):
        if roomStatus == "same":
            self.hunt = True
            print("\033[91mFredrik såg dig!! Skynda dig tillbaka till kontoret!\n\033[0m")
        if self.hunt == True:
            return True
        else:
            return False
    # Skickar tillbaka hur många steg man tagit medan man blir jagad.
    def run(self):
        if self.hunt == True and self.o != ">-O":
            self.steps = self.steps + 1
            print("\033[91mFredrik Jagar dig!\n\033[0m")
        if self.o == ">-O":
            self.steps = 0
            print("Du hann undan\n")
            self.hunt = False
        return self.steps






