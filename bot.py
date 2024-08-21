from funct import *
from data import *
import os
from helper import clear, logo
from data import update_js, load_js
from colorama import init, Fore, Back, Style

init()



DATA = load_js()

def main():
    clear()
    logo()

    while True:
        command = input(Fore.LIGHTWHITE_EX+Style.BRIGHT+"=> "+Style.RESET_ALL) 
        try:
            command_temp = DATA[command]
            if command_temp in globals():
                functionRun = globals()[command_temp]
                if callable(functionRun):
                    functionRun()
        except Exception as e:
            print(Fore.LIGHTWHITE_EX+Style.BRIGHT+"[BOT] : "+Fore.LIGHTRED_EX+str(e)+Style.RESET_ALL)
            error_()


if __name__ == "__main__":
    main()