#lybraries

import os
import webbrowser
import time
import colorama
from colorama import Fore
import ctypes



#normal cls

def cls():
    os.system('cls' if os.name=='nt' else 'clear')



#console title

def terminaltitle():
    ctypes.windll.kernel32.SetConsoleTitleW("MENU | by 2Loop#6969")



#password screen

def rootmenu():
    cls()
    print("")
    print(Fore.LIGHTMAGENTA_EX + """     ██████╗  ██████╗  ██████╗ ████████╗    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
     ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝    ████╗ ████║██╔════╝████╗  ██║██║   ██║
     ██████╔╝██║   ██║██║   ██║   ██║       ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
     ██╔══██╗██║   ██║██║   ██║   ██║       ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
     ██║  ██║╚██████╔╝╚██████╔╝   ██║       ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝       ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝""")
    print("")
    print("")
    print("")
    while True:
        password = 'password'
        root = input("                                   [menu@root] > ")
        if root == password:
            menu()
            break
        else:
            rootmenu()



#menu title

def title():
    print("")
    print(Fore.LIGHTGREEN_EX+ """     ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
     ████╗ ████║██╔════╝████╗  ██║██║   ██║
     ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
     ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
     ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
     ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝""")



#menu input

def menu():
    cls()
    title()
    print(Fore.LIGHTGREEN_EX+ "")
    print("     -- Menu ------------------------------")
    print(Fore.LIGHTWHITE_EX + "")
    print("     [1] Option")
    print("     [2] Option")
    print("     [3] Option")
    print("     [4] Option")
    print("     [5] Option")
    print("     [6] Option")
    print("")
    print(Fore.LIGHTGREEN_EX+ "     --------------------------------------")
    print("")
    print(Fore.LIGHTWHITE_EX + "     [7] Quit")
    print(Fore.LIGHTGREEN_EX+ "")
    while True:
        menu = input("     [menu@input] > ")
        print("")
        try:
            menu = int(menu)
            break
        except (ValueError, TypeError, NameError):
            menu()
    if menu == 1:
        optiona()
    elif menu == 2:
        optionb()
    elif menu == 3:
        optionc()
    elif menu == 4:
        optiond()
    elif menu == 5:
        optione()
    elif menu == 6:
        optionf()
    elif menu == 7:
        quit()
    elif menu >= 8:
        menu()



#option1

def optiona():
    cls()
    print("")
    print(Fore.LIGHTCYAN_EX + """      ██████╗ ██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
     ██╔═══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
     ██║   ██║██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║
     ██║   ██║██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║
     ╚██████╔╝██║        ██║   ██║╚██████╔╝██║ ╚████║
      ╚═════╝ ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝""")
    print("")
    print("     -- Option --------------------------------------")
    print(Fore.LIGHTWHITE_EX + "")
    print("     Filler:")
    print("")
    print("     Lorem ipsum dolor sit amet,")
    print("     consectetuer adipiscing elit.")
    print("     Aenean commodo ligula eget dolor.")
    print("     Aenean massa.")
    print("     Donec quam felis, ultricies nec,")
    print("     pellentesque eu, pretium quis, sem.")
    print("     Nulla consequat massa quis enim.")
    print("")
    print("")
    print("     Others:")
    print("")
    print("     [1] Otion")
    print("     [2] Option")
    print("     [3] Option")
    print("")
    print(Fore.LIGHTCYAN_EX + "     ------------------------------------------------")
    print(Fore.LIGHTWHITE_EX + "     [4] Back")
    print(Fore.LIGHTCYAN_EX + "")
    while True:
        inputa = input("     [menu@input] > ")
        print("")
        try:
            inputa = int(inputa)
            break
        except (ValueError, TypeError, NameError):
            optiona()
    if inputa == 1:
            webbrowser.open("https://github.com/astros3x")
            optiona()
    elif inputa == 2:
            webbrowser.open("https://github.com/astros3x")
            optiona()
    elif inputa == 3:
            webbrowser.open("https://github.com/astros3x")
            optiona()
    elif inputa == 4:
            menu()
    elif inputa >= 5:
            optiona()



#option2

def optionb():
    cls()
    print("")
    print(Fore.LIGHTYELLOW_EX + """      ██████╗ ██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
     ██╔═══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
     ██║   ██║██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║
     ██║   ██║██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║
     ╚██████╔╝██║        ██║   ██║╚██████╔╝██║ ╚████║
      ╚═════╝ ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝""")
    print("")
    print("     -- Option --------------------------------------")
    print(Fore.LIGHTWHITE_EX + "")
    print("     Filler:")
    print("")
    print("     Lorem ipsum dolor sit amet,")
    print("     consectetuer adipiscing elit.")
    print("     Aenean commodo ligula eget dolor.")
    print("     Aenean massa.")
    print("     Donec quam felis, ultricies nec,")
    print("     pellentesque eu, pretium quis, sem.")
    print("     Nulla consequat massa quis enim.")
    print("")
    print("")
    print("     Others:")
    print("")
    print("     [1] Otion")
    print("     [2] Option")
    print("     [3] Option")
    print("")
    print(Fore.LIGHTYELLOW_EX + "     ------------------------------------------------")
    print(Fore.LIGHTWHITE_EX + "     [4] Back")
    print(Fore.LIGHTYELLOW_EX + "")
    while True:
        inputb = input("     [menu@input] > ")
        print("")
        try:
            inputb  = int(inputb)
            break
        except (ValueError, TypeError, NameError):
            optionb()
    if inputb  == 1:
            webbrowser.open("https://github.com/astros3x")
            optionb()
    elif inputb  == 2:
            webbrowser.open("https://github.com/astros3x")
            optionb()
    elif inputb  == 3:
            webbrowser.open("https://github.com/astros3x")
            optionb()
    elif inputb  == 4:
            menu()
    elif inputb  >= 5:
            optionb()


#option3

def optionc():
    cls()
    print("")
    print(Fore.LIGHTBLUE_EX + """      ██████╗ ██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
     ██╔═══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
     ██║   ██║██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║
     ██║   ██║██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║
     ╚██████╔╝██║        ██║   ██║╚██████╔╝██║ ╚████║
      ╚═════╝ ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝""")
    print("")
    print("     -- Option --------------------------------------")
    print(Fore.LIGHTWHITE_EX + "")
    print("     Filler:")
    print("")
    print("     Lorem ipsum dolor sit amet,")
    print("     consectetuer adipiscing elit.")
    print("     Aenean commodo ligula eget dolor.")
    print("     Aenean massa.")
    print("     Donec quam felis, ultricies nec,")
    print("     pellentesque eu, pretium quis, sem.")
    print("     Nulla consequat massa quis enim.")
    print("")
    print("")
    print("     Others:")
    print("")
    print("     [1] Otion")
    print("     [2] Option")
    print("     [3] Option")
    print("")
    print(Fore.LIGHTBLUE_EX + "     ------------------------------------------------")
    print(Fore.LIGHTWHITE_EX + "     [4] Back")
    print(Fore.LIGHTBLUE_EX + "")
    while True:
        inputc = input("     [menu@input] > ")
        print("")
        try:
            inputc  = int(inputc)
            break
        except (ValueError, TypeError, NameError):
            optionc()
    if inputc  == 1:
            webbrowser.open("https://github.com/astros3x")
            optionc()
    elif inputc  == 2:
            webbrowser.open("https://github.com/astros3x")
            optionc()
    elif inputc  == 3:
            webbrowser.open("https://github.com/astros3x")
            optionc()
    elif inputc  == 4:
            menu()
    elif inputc  >= 5:
            optionc()



#option4

def optiond():
    cls()
    print("")
    print(Fore.LIGHTRED_EX + """      ██████╗ ██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
     ██╔═══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
     ██║   ██║██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║
     ██║   ██║██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║
     ╚██████╔╝██║        ██║   ██║╚██████╔╝██║ ╚████║
      ╚═════╝ ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝""")
    print("")
    print("     -- Option --------------------------------------")
    print(Fore.LIGHTWHITE_EX + "")
    print("     Filler:")
    print("")
    print("     Lorem ipsum dolor sit amet,")
    print("     consectetuer adipiscing elit.")
    print("     Aenean commodo ligula eget dolor.")
    print("     Aenean massa.")
    print("     Donec quam felis, ultricies nec,")
    print("     pellentesque eu, pretium quis, sem.")
    print("     Nulla consequat massa quis enim.")
    print("")
    print("")
    print("     Others:")
    print("")
    print("     [1] Otion")
    print("     [2] Option")
    print("     [3] Option")
    print("")
    print(Fore.LIGHTRED_EX + "     ------------------------------------------------")
    print(Fore.LIGHTWHITE_EX + "     [4] Back")
    print(Fore.LIGHTRED_EX + "")
    while True:
        inputd = input("     [menu@input] > ")
        print("")
        try:
            inputd  = int(inputd)
            break
        except (ValueError, TypeError, NameError):
            optiond()
    if inputd  == 1:
            webbrowser.open("https://github.com/astros3x")
            optiond()
    elif inputd  == 2:
            webbrowser.open("https://github.com/astros3x")
            optiond()
    elif inputd  == 3:
            webbrowser.open("https://github.com/astros3x")
            optiond()
    elif inputd  == 4:
            menu()
    elif inputd  >= 5:
            optiond()



#option5

def optione():
    cls()
    print("")
    print(Fore.LIGHTMAGENTA_EX + """      ██████╗ ██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
     ██╔═══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
     ██║   ██║██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║
     ██║   ██║██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║
     ╚██████╔╝██║        ██║   ██║╚██████╔╝██║ ╚████║
      ╚═════╝ ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝""")
    print("")
    print("     -- Option --------------------------------------")
    print(Fore.LIGHTWHITE_EX + "")
    print("     Filler:")
    print("")
    print("     Lorem ipsum dolor sit amet,")
    print("     consectetuer adipiscing elit.")
    print("     Aenean commodo ligula eget dolor.")
    print("     Aenean massa.")
    print("     Donec quam felis, ultricies nec,")
    print("     pellentesque eu, pretium quis, sem.")
    print("     Nulla consequat massa quis enim.")
    print("")
    print("")
    print("     Others:")
    print("")
    print("     [1] Otion")
    print("     [2] Option")
    print("     [3] Option")
    print("")
    print(Fore.LIGHTMAGENTA_EX + "     ------------------------------------------------")
    print(Fore.LIGHTWHITE_EX + "     [4] Back")
    print(Fore.LIGHTMAGENTA_EX + "")
    while True:
        inpute = input("     [menu@input] > ")
        print("")
        try:
            inpute  = int(inpute)
            break
        except (ValueError, TypeError, NameError):
            optione()
    if inpute == 1:
            webbrowser.open("https://github.com/astros3x")
            optione()
    elif inpute == 2:
            webbrowser.open("https://github.com/astros3x")
            optione()
    elif inpute == 3:
            webbrowser.open("https://github.com/astros3x")
            optione()
    elif inpute == 4:
            menu()
    elif inpute >= 5:
            optione()



#option6

def optionf():
    cls()
    print("")
    print(Fore.LIGHTGREEN_EX + """      ██████╗ ██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
     ██╔═══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
     ██║   ██║██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║
     ██║   ██║██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║
     ╚██████╔╝██║        ██║   ██║╚██████╔╝██║ ╚████║
      ╚═════╝ ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝""")
    print("")
    print("     -- Option --------------------------------------")
    print(Fore.LIGHTWHITE_EX + "")
    print("     Filler:")
    print("")
    print("     Lorem ipsum dolor sit amet,")
    print("     consectetuer adipiscing elit.")
    print("     Aenean commodo ligula eget dolor.")
    print("     Aenean massa.")
    print("     Donec quam felis, ultricies nec,")
    print("     pellentesque eu, pretium quis, sem.")
    print("     Nulla consequat massa quis enim.")
    print("")
    print("")
    print("     Others:")
    print("")
    print("     [1] Otion")
    print("     [2] Option")
    print("     [3] Option")
    print("")
    print(Fore.LIGHTGREEN_EX + "     ------------------------------------------------")
    print(Fore.LIGHTWHITE_EX + "     [4] Back")
    print(Fore.LIGHTGREEN_EX + "")
    while True:
        inputf = input("     [menu@input] > ")
        print("")
        try:
            inputf  = int(inputf)
            break
        except (ValueError, TypeError, NameError):
            optionf()
    if inputf  == 1:
            webbrowser.open("https://github.com/astros3x")
            optionf()
    elif inputf  == 2:
            webbrowser.open("https://github.com/astros3x")
            optionf()
    elif inputf  == 3:
            webbrowser.open("https://github.com/astros3x")
            optionf()
    elif inputf  == 4:
            menu()
    elif inputf  >= 5:
            optionf()



#start

terminaltitle()
rootmenu()