#rullande text
import sys
import time
import keyboard
import os
def print_slow(str):
    for letter in str:
        if keyboard.is_pressed("enter"):
            os.system("cls")
            return
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
# Funktioner som kallas när en specifik ascii art ska visas
def huvt():


    print(""" 
 ______               _        _  _           _____  _                       _        
|  ____|             | |      (_)| |         |  __ \(_)                     (_)       
| |__  _ __  ___   __| | _ __  _ | | __ ___  | |__) |_  ____ ____ ___  _ __  _   __ _ 
|  __|| '__|/ _ \ / _` || '__|| || |/ // __| |  ___/| ||_  /|_  // _ \| '__|| | / _` |
| |   | |  |  __/| (_| || |   | ||   < \__ \ | |    | | / /  / /|  __/| |   | || (_| |
|_|   |_|   \___| \__,_||_|   |_||_|\_\|___/ |_|    |_|/___|/___|\___||_|   |_| \__,_| """)
                                                                                                
    print_slow("\n Du befinner dig i Fredriks pizzaria och råkade fastna i pizzarian.\n Du hörde att det är dödliga robotar där och du ska försöka fly utan att dö.\n Ditt jobb är att leta runt pizzarian för ett sätt att fly.\n Om Fredrik hittar dig då ska du försöka gå till kontoret så fort som möjligt.\n Lycka till")
    print_slow("""\n Om du vill veta vart du befinner dig i kartan så skriv \033[91m"karta"\033[0m\n Om du vill veta vad du har på dig så kan du skriva \033[91m"väska"\033[0m\n""")
    
#huvt()







def FredrikSrkämm():
    print(''' 
⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⡛⠛⠛⠻⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
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

def menu():
    print('''
                                             _____            _                          
                                            /  ___|          | |                         
                                            \ `--. _ __   ___| | __ _                    
                                             `--. \ '_ \ / _ \ |/ _` |                   
                                            /\__/ / |_) |  __/ | (_| |                   
                                            \____/| .__/ \___|_|\__,_|                   
                                                    | |                                    
                                _____          _  _ |__ _ _       _                        
                               |_   _|        | |(_) (_) | |     (_)                       
                                 | | _ __  ___| |_ __ _| | |_ __  _ _ __   __ _  __ _ _ __ 
                                 | || '_ \/ __| __/ _` | | | '_ \| | '_ \ / _` |/ _` | '__|
                                _| || | | \__ \ || (_| | | | | | | | | | | (_| | (_| | |   
                                \___/_| |_|___/\__\__,_|_|_|_| |_|_|_| |_|\__, |\__,_|_|   
                                                                            __/ |           
                                                                        |___/             
    ''')



