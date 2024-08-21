import os
import requests
from colorama import init, Fore, Back, Style
from helper import usdtoiqd
import instaloader


init()

def convert_currency():
    amount = input(Style.BRIGHT+Fore.LIGHTYELLOW_EX+"[BOT] "+Fore.LIGHTWHITE_EX+"Amount of USD to iqd : ")
    rateIq = usdtoiqd()

    ratefinal = int(amount) * rateIq
    print(Style.BRIGHT+Fore.LIGHTYELLOW_EX+"[BOT] "+Fore.LIGHTWHITE_EX+"The Amount is IQD "+str(ratefinal))

    
def search_web():
    query = input(Style.BRIGHT+Fore.LIGHTYELLOW_EX+"[BOT] "+Fore.LIGHTWHITE_EX+"What do you want search for : "+Style.RESET_ALL)
    
    url = "https://www.google.com/search?q="+query
    command = "start "+url
    os.system(command)

def install_web():
    url = input(Style.BRIGHT+Fore.LIGHTYELLOW_EX+"[BOT]"+Fore.LIGHTWHITE_EX+" Webiste Link to download source code : "+Style.RESET_ALL)
    response = requests.get(url)
    if response.status_code == 200:
        nameFile = input(Style.BRIGHT+Fore.LIGHTYELLOW_EX+"[BOT] "+Fore.LIGHTWHITE_EX+"File name to save the source code : "+Style.RESET_ALL)
        open(nameFile+".html", "w+", encoding="utf-8").write(response.text)

def hello():
    print(Style.BRIGHT+Fore.LIGHTYELLOW_EX+"[BOT]"+Fore.LIGHTWHITE_EX+" Hello, What can i help you with ?"+Style.RESET_ALL)

def igProfile():

    ig = instaloader.Instaloader()
    username = input(Style.BRIGHT+Fore.LIGHTYELLOW_EX+"[BOT] "+Fore.LIGHTWHITE_EX+"Instagram username : "+Style.RESET_ALL)
    profile = instaloader.Profile.from_username(ig.context, username)

    info_account = Style.BRIGHT+Fore.LIGHTWHITE_EX+'''
+++++++++++++++++++++++
+ '''+Fore.LIGHTCYAN_EX+''' Username : '''+Fore.LIGHTYELLOW_EX+profile.username+Fore.LIGHTWHITE_EX+'''
+ '''+Fore.LIGHTCYAN_EX+''' Followers : '''+Fore.LIGHTYELLOW_EX+str(profile.followers)+Fore.LIGHTWHITE_EX+'''
+ '''+Fore.LIGHTCYAN_EX+''' Following : '''+Fore.LIGHTYELLOW_EX+str(profile.followees)+Fore.LIGHTWHITE_EX+'''
+ '''+Fore.LIGHTCYAN_EX+''' Posts : '''+Fore.LIGHTYELLOW_EX+str(profile.mediacount)+Fore.LIGHTWHITE_EX+'''
+ '''+Fore.LIGHTCYAN_EX+''' Bio : '''+Fore.LIGHTYELLOW_EX+profile.biography+Fore.LIGHTWHITE_EX+'''
+++++++++++++++++++++++
    '''+Style.RESET_ALL
    print(info_account)
    option = input(Style.BRIGHT+Fore.LIGHTYELLOW_EX+"[BOT] "+Fore.LIGHTWHITE_EX+"Save Profile Picture ? y/n ")
    if option.lower() == "y":
        instaloader.Instaloader().download_profile(username,profile_pic_only=True)
        print(Style.BRIGHT+Fore.LIGHTYELLOW_EX+"[BOT] "+Fore.LIGHTGREEN_EX+"Profile Downloaded Success "+Style.RESET_ALL)

def exitSys():
    exit()

def error_():
    print(Style.BRIGHT+Fore.LIGHTYELLOW_EX+"[BOT] "+Fore.LIGHTRED_EX+" I cant handle this command"+Style.RESET_ALL)