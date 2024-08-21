import os
from colorama import init, Fore, Back, Style
import requests
import json

init()
# Bot version
VERSION = "1.0.0"

# Clear Screen (terminal)
def clear():
    os.system("cls")

# logo
def logo():
    logo_ = Style.BRIGHT+Fore.LIGHTCYAN_EX+'''

.____________        __   
|__\______   \ _____/  |_ 
|  ||    |  _//  _ \   __\\
|  ||    |   (  <_> )  |  
|__||______  /\____/|__|  
           \/          

iBot '''+Fore.LIGHTGREEN_EX+VERSION+Fore.LIGHTWHITE_EX+'''
==========================
Welcome To iBot
    '''+Style.RESET_ALL
    print(logo_)

# USD to IQD
def usdtoiqd():
    response = requests.get('https://open.er-api.com/v6/latest/USD')
    try:
        rateIQD = response.json()["rates"]["IQD"]
    except:
        rateIQD = "0000"
    return int(rateIQD)