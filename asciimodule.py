#rullande text
import sys
import time
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
# Funktioner som kallas när en specifik ascii art ska visas
def huvt ():
    print(""" ______               _        _  _           _____  _                       _        
|  ____|             | |      (_)| |         |  __ \(_)                     (_)       
| |__  _ __  ___   __| | _ __  _ | | __ ___  | |__) |_  ____ ____ ___  _ __  _   __ _ 
|  __|| '__|/ _ \ / _` || '__|| || |/ // __| |  ___/| ||_  /|_  // _ \| '__|| | / _` |
| |   | |  |  __/| (_| || |   | ||   < \__ \ | |    | | / /  / /|  __/| |   | || (_| |
|_|   |_|   \___| \__,_||_|   |_||_|\_\|___/ |_|    |_|/___|/___|\___||_|   |_| \__,_| 
                                                                                                
                                                                                                """)
                                                                                                
    print_slow("\n Du befinner dig i Fredriks pizzaria och råkade fastna i pizzarian.\n Du hörde att det är dödliga robotar där och du ska försöka fly utan att dö.\n Ditt jobb är att leta runt pizzarian för ett sätt att fly.\n Om robotarna hittar dig då ska du försöka gå till kontoret så fort som möjligt.\n Lyckatill")
    print_slow("""\n Om du vill veta vart du befinner dig i kartan så skriv "karta" om du vill se kartan.\n Om du vill veta vad du har på dig så kan du skriva "väska" för att veta vad du har.\n""")
    
#huvt()







def FredrikSrkämm():
    print(''' ⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⡛⠛⠛⠻⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠿⠿⠿⡿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣏⠄⠀⠀⠀⢀⣤⣴⣦⣤⣤⣤⣀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠈⠀⠀⠀⠂⠈⠀⠀⠓⠀⠀⠤⣽⣿⣿⣿
⣿⠟⠁⠀⠀⠀⣴⠟⠉⠉⠉⠙⠛⠛⠿⣿⣦⡀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿
⠟⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⣄⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣷⣦⣤⣀⠀⠀⠀⠀⠻⣿
⠀⠄⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣧⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣠⣾⣿⣿⣿⠟⠛⠛⠻⠿⠿⣿⣿⣧⠀⠀⠀⠁⣾
⠂⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡆⠀⢸⣿⣿⣿⣿⣿⠛⢹⣿⣿⣿⡇⠀⠀⠀⣰⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠙⣿⠀⠀⠀⠄⢹
⢀⡀⠀⠀⠀⠙⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠏⠀⣸⣿⣿⣿⣿⠟⠁⠚⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠃⢸
⣏⠁⠀⠀⠀⠀⠈⠻⣦⣄⡀⠀⠀⠀⣀⣤⣾⣿⠟⠁⠀⢰⣿⣿⡿⠛⠁⠀⠀⠀⠙⣿⣿⣧⡀⠀⠀⢹⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⢠⣾
⣿⣇⠀⢂⠀⠀⠀⠀⠀⠉⠛⠛⠛⠿⠟⠛⠉⠀⠀⠀⣠⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡁⠀⠀⠀⠻⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⣀⠜⠀⠀⠀⠀⣼⣿
⣿⣮⣟⡌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⣴⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣷⠀⠀⠀⠀⠈⠛⠿⣿⣾⣿⡶⠖⠛⠉⠀⠀⠀⠀⠀⠀⣻⣿
⣿⣍⢻⣿⣤⠀⣀⠀⠀⠀⠀⠀⢀⠐⢁⣴⣾⣿⣾⣿⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⣅⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠐⢰⣿⣿
⣿⣿⠛⠟⢿⣇⣬⡀⠀⠠⣶⡀⢮⣼⣿⣿⣿⣿⣿⣿⣯⡀⠀⢀⣤⡀⢀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣷⣄⠀⠀⠀⢠⠒⠀⠀⠀⣀⠀⠀⠀⠀⠀⢀⣿⣿⣿
⣿⣿⣄⠀⠀⠡⠀⠄⠀⠀⠈⠁⠘⠛⠻⠿⣿⣿⣿⣿⣿⣿⠇⣸⣿⣿⣷⣽⣶⡒⠅⠀⢈⣼⣿⣿⣿⣿⣿⣿⣦⠀⢹⣶⣦⣤⠆⠀⠀⠀⠀⠤⢰⣿⣿⣿⣿
⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⡀⢀⠉⠉⠛⠉⠉⠙⠛⠿⠿⠿⠿⣿⣿⢆⠀⣾⣿⣿⣿⣿⣿⡿⣿⡋⠐⣿⠿⠋⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣀⡀⠀⠀⠀⠀⢄⠀⠀⠀⡃⢬⣗⠻⠇⣰⣶⣦⠀⣠⣄⣀⠀⣀⣉⡀⠐⠻⠿⠿⠟⠋⡀⠀⠠⠀⠀⠀⠀⠀⠀⠀⣠⣀⠀⠀⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠈⠃⠀⠴⠄⠈⠻⠷⠀⢿⣿⣿⠇⣿⣿⣿⢰⣿⣿⣿⡄⣾⣗⡀⠰⣀⠈⠀⠃⠀⠀⠀⠀⠀⣠⣾⣿⡵⠀⣰⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣇⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠋⠈⠻⠿⠿⠃⣿⣿⠇⠰⠂⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣷⠁⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠸⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⣻⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡠⠀⠀⠹⡇⢰⣾⣿⡆⢾⣿⣿⣆⢸⣿⣦⢸⣿⡆⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠉⠉⠉⠘⠿⡿⠏⠸⣿⡿⠘⡿⠛⠃⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡗⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⢀⣤⣴⣿⣿⠆⠀⣱⣉⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠘⣿⣿⣿⣿⣏⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ''')

def ChicaSkrämm():
    print('''  ''')

def death():
    print('''\033[91m
    
    ██████╗ ██╗   ██╗    ██████╗  ██████╗  ██████╗ 
    ██╔══██╗██║   ██║    ██╔══██╗██╔═══██╗██╔════╝ 
    ██║  ██║██║   ██║    ██║  ██║██║   ██║██║  ███╗
    ██║  ██║██║   ██║    ██║  ██║██║   ██║██║   ██║
    ██████╔╝╚██████╔╝    ██████╔╝╚██████╔╝╚██████╔╝
    ╚═════╝  ╚═════╝     ╚═════╝  ╚═════╝  ╚═════╝ 
                                               

    \033[0m''')

#death()

