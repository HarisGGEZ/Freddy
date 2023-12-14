
class map():
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
        
    def printMap(self):
        print(f'''                                                                                                                                                                                                                                                                                                                                                                                       
                                            ''...............................''                                              
                                            .,.                               .;.    ..  ..                                   
                                            .,.                               .,.    ',  .,.                                  
                                            .,.                               .;.    ',  .,.                                  
                                            .:'                               ':.    ,,  .;.                                  
        .,'.........,.  .,..................','...............................','....'.   .'.......,'                         
        .,          ,:..;'                                                                         .,                         
        .,                                                                                         .,     .......             
        .,          ,;..;'                                                                         .,  .,,......;'            
        .,          ,'  ''                                                                         .,  .,.      .,            
        .,   {self.b}    ,'  ''                                                                         .:..,;.      .,            
        .,          ,'  ''                                                                                     .,            
        .,          ,'  ''                                                                                      .,   .........
        .,          ,'  ''                                                                         .:..,:.      ':..,c'......:
        .:..........;'  ''                                                                         .,  .,.      ':..,:.      ,
            ............   ''                                {self.d}                                   .,  .,.      ':'.;:.      ,
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
                                        ,,          .;.                   .;.          ,,   ,,                       ,,         
                        ............   ,'          .,.                   .,.          ',   ''                       ''         
                        ';.........';.  ,'          .,.                   .,.          ',   ''                       ',         
                        ''         .,.  ,'          .,.                   .,.          ',   ''                       ',         
                        ',         .,.  ,'          .,.                   .,.          ',   ''        {self.k}           ',         
                        ',         .;;..;'          .,.                   .,.          ',   ''                       ',         
                        ',                          .,.                   .,.          ',   ''                       ''         
                        ''   {self.s}    ,,..;.          .,.                   .,.          ',   ''                       ''         
                        ''         .;;..;'          .,.                   .,.          ',   ,,                       ,,         
                        ''         .,.  ,'          .,.   .............   .,.          ',   .'.......................'.         
                        ''         .,.  ,'          .,.  ,;...........;,  .;.          ',                                       
                        ';.........';.  ,'          .,.  ,'           .,  .,.          ',                                       
                        ...........    ,'          .,.  ,'           ',  .,.          ',                                       
                                        ,'          .;,..:'           ':'.,;.          ',                                       
                                        ,'    {self.w}              {self.o}              {self.e}    ',                                       
                                        ,'          .,,.';.           .;'.,,.          ',                                       
                                        ,'          .;,..;'           ';..';.          ',                                       
                                        ,'          .;.  ,'           ',  .;.          ',                                       
                                        ,c,,,,,,,,,,::.  ;c,,,,,,,,,,,c;  .::,,,,,,,,,,c,                                       '''
        )
        
    def Move(self, move):
        
        if move == "left" and self.o == ">-O":
            self.o = "   "
            self.old = "Office"
            self.e = "   "
            self.w = ">-O"
            
        elif move == "right" and self.o == ">-O":
            self.o = "   "
            self.old = "Office"
            self.e = ">-O"
        
        elif move == "left" and self.w == ">-O":
            self.old = "West"
            self.s = ">-O"
            self.w = "   "
            
        elif move == "up" and (self.e == ">-O" or self.w == ">-O"):
            if self.e == ">-O":
                self.old = "East"
            if self.w == ">-O":
                self.old = "West"
            self.d = ">-O"
            self.e = "   "
            self.w = "   "

        elif move == "left" and self.e == ">-O":
            self.old = "East"
            self.o = ">-O"
            self.e = "   "
        elif move == "right" and self.w == ">-O":
            self.old = "West"
            self.o = ">-O"
            self.w = "   "

        elif move == "right" and self.s == ">-O":
            self.old = "Supply"
            self.s = "   "
            self.w = ">-O"
            
        elif move == "left" and self.d == ">-O":
            self.old = "Dining"
            self.b = ">-O"
            self.d = "   "

        elif move == "right" and self.d == ">-O":
            self.old = "Dining"
            self.t = ">-O"
            self.d = "   "

        elif move == "east" and self.d == ">-O":
            self.old = "Dining"
            self.e = ">-O"
            self.d = "   "

        elif move == "west" and self.d == ">-O":
            self.old = "Dining"
            self.w = ">-O"
            self.d = "   "

        elif move == "right" and self.d == ">-O":
            self.old = "Dining"
            self.t = ">-O"
            self.d = "   "

        elif move == "kitchen" and self.d == ">-O":
            self.old = "Dining"
            self.k = ">-O"
            self.d = "   "

        elif move == "back":
            if self.old == "Kitchen":
                self.old = "Dining"
                self.k = ">-O"
                self.d = "   "

            elif self.old == "Dining":
                if self.e == ">-O":
                    self.old = "East"
                if self.w == ">-O":
                    self.old = "West"
                if self.b == ">-O":
                    self.old = "Backstage"
                if self.t == ">-O":
                    self.old = "Toilets"
                if self.k == ">-O":
                    self.old = "Kitchen"
                self.d = ">-O"
                self.e = "   "
                self.w = "   "
                self.b = "   "
                self.t = "   "
                self.k = "   "

            elif self.old == "Supply":
                self.old = "West"
                self.s = ">-O"
                self.w = "   "
            
            elif self.old == "West":
                if self.s == ">-O":
                    self.old = "Supply"
                if self.d == ">-O":
                    self.old = "Dining"
                if self.o == ">-O":
                    self.old = "Office"
                self.w = ">-O"
                self.s = "   "
                self.o = "   "
                self.d = "   "
        
            elif self.old == "East":
                if self.d == ">-O":
                    self.old = "Dining"
                if self.o == ">-O":
                    self.old = "Office"
                self.e = ">-O"
                self.d = "   "
                self.o = "   "

            elif self.old == "Office":
                if self.e == ">-O":
                    self.old = "East"
                if self.w == ">-O":
                    self.old = "West"
                self.o = ">-O"
                self.e = "   "
                self.w = "   "

            elif self.old == "Toilets":
                self.old = "Dining"
                self.t = ">-O"
                self.d = "   "

            elif self.old == "Backstage":
                self.old = "Dining"
                self.b = ">-O"
                self.d = "   "


Map = map()
while True:
    
    Map.printMap()
    move = input()
    Map.Move(move)