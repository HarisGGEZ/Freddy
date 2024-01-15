from time import sleep


class kartaKlass():
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
        
    def printKarta(self):
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
                        ';.........';.  ,'          .,.  ,'  \033[91mKontor\033[0m          .,  .,.          ',                                       
                        ...........    ,'          .,.  ,'           ',  .,.          ',                                       
                                        ,'          .;,..:'           ':'.,;.          ',                                       
                                        ,'    {self.w}              {self.o}              {self.e}    ',                                       
                                        ,'          .,,.';.           .;'.,,.          ',                                       
                                        ,'          .;,..;'           ';..';.          ',                                       
                                        ,'          .;.  ,'           ',  .;.          ',                                       
                                        ,c,,,,,,,,,,::.  ;c,,,,,,,,,,,c;  .::,,,,,,,,,,c,                                       '''
        )
        
        
    def flytt(self, flytt):
        
        if flytt == "vänster" and self.o == ">-O":
            self.o = "   "
            self.old = "kontor"
            self.e = "   "
            self.w = ">-O"
            
        elif flytt == "höger" and self.o == ">-O":
            self.o = "   "
            self.old = "kontor"
            self.e = ">-O"
        
        elif flytt == "vänster" and self.w == ">-O":
            self.old = "väst"
            self.s = ">-O"
            self.w = "   "
            
        elif flytt == "fram" and (self.e == ">-O" or self.w == ">-O"):
            if self.e == ">-O":
                self.old = "öst"
            if self.w == ">-O":
                self.old = "väst"
            self.d = ">-O"
            self.e = "   "
            self.w = "   "

        elif flytt == "vänster" and self.e == ">-O":
            self.old = "öst"
            self.o = ">-O"
            self.e = "   "
        
        elif flytt == "höger" and self.w == ">-O":
            self.old = "väst"
            self.o = ">-O"
            self.w = "   "

        elif flytt == "höger" and self.s == ">-O":
            self.old = "förråd"
            self.s = "   "
            self.w = ">-O"
            
        elif flytt == "vänster" and self.d == ">-O":
            self.old = "matsal"
            self.b = ">-O"
            self.d = "   "

        elif flytt == "höger" and self.d == ">-O":
            self.old = "matsal"
            self.t = ">-O"
            self.d = "   "

        elif flytt == "upp" and self.d == ">-O":
            return "exit attempt"

        elif flytt == "ner":
            print("Höger, Vänster eller Kök?")
            ner = input()

            if self.d == ">-O" and ner == "vänster":
                self.old = "matsal"
                self.w = ">-O"
                self.d = "   "
        
            if self.d == ">-O" and ner == "höger":
                self.old = "matsal"
                self.e = ">-O"
                self.d = "   "
        
            if self.d == ">-O" and ner == "kök" :
                self.old = "matsal"
                self.k = ">-O"
                self.d = "   "
        
        elif flytt == "höger hall" and self.d == ">-O":
            self.old = "matsal"
            self.w = ">-O"
            self.d = "   "

        elif flytt == "höger" and self.d == ">-O":
            self.old = "matsal"
            self.t = ">-O"
            self.d = "   "
        
        elif flytt == "höger" and self.b == ">-O":
            self.old = "prishörna"
            self.d = ">-O"
            self.b = "  "
        
        elif flytt == "vänster" and self.t == ">-O":
            self.old = "toaletter"
            self.d = ">-O"
            self.t = "  "
        
        elif flytt == "kök" and self.d == ">-O":
            self.old = "matsal"
            self.k = ">-O"
            self.d = "   "

        elif flytt == "tillbaka":
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

    
    def printVal(self):
        Plats = self.location.capitalize()
        print(f"\nDu befinner dig i {Plats}. \nDu kan gå:")
        sleep(0.5)
        if self.o == ">-O":
            print("Vänster till Vänstra Hallen \nHöger till Högra Hallen")
        if self.w == ">-O":
            print("Vänster till Förrådet \nHöger till Kontoret \nFram till Matsalen ")
        if self.e == ">-O":
            print("Vänster till Kontoret \nFram till Matsalen")
        if self.s == ">-O":
            print("Höger till Vänstra Hallen")
        if self.d == ">-O":
            print("Vänster till Prishörnan \nHöger till toaletterna. \nNer till Högra eller Vänstra hall eller Köket. \nUpp till Utgången (Alla nycklar krävs)")
        if self.t == ">-O":
            print("Vänster till Matsalen")
        if self.b == ">-O":
            print("Höger till Matsalen")
        if self.k == ">-O":
            print("Tillbaka till Matsalen")
        #if self.l == ">-O":
            #print(" \nTillbaka till Matsalen")
        print("\n")
    
    def returnPlats(self):
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
        #if self.l == ">-O":
            #self.location = "utgång"
        return self.location
    
    def jagad(self, room):
        if room == "same":
            self.hunt = True
            print("Fredrik såg dig!! Skynda dig tillbaka till kontoret!\n")
        if self.hunt == True:
            return True
        else:
            return False

    def run(self):
        if self.hunt == True and self.o != ">-O":
            self.steps = self.steps + 1
            print("Fredrik Jagar dig!\n")
        if self.o == ">-O":
            self.steps = 0
            print("Du hann undan\n")
            self.hunt = False
        return self.steps






