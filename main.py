import json
import os
import string
from sysconfig import parse_config_h

import discord
from discord.app_commands import commands
from discord.ext.commands import bot

try:
    import sys
    import time
    import uuid
    import yaml
    import hashlib
    import httpx
    import faker
    import ctypes
    import random
    import secrets
    import pystyle
    import requests
    import keyboard
    import threading
    import tls_client
    import urllib.parse
    import concurrent.futures
    import pytz
    from keyauth import *


    from uuid import uuid4
    from faker import Faker
    from pystyle import Write, Colors, Colorate
    from colorama import Fore, Style, Back, init
    from threading import Lock
    from traceback import print_exc
    from concurrent.futures import ThreadPoolExecutor
except ModuleNotFoundError:
    os.system("cls")
    print(f"Module Not Found Error Occured!!! Installing Modules")
    os.system("py -m pip install keyboard")
    os.system("py -m pip install pyyaml")
    os.system("py -m pip install pystyle")
    os.system("py -m pip install colorama")
    os.system("py -m pip install threading")
    os.system("py -m pip install concurrent.futures")
    os.system("py -m pip install tls_client")
    os.system("py -m pip install ctypes")
    os.system("py -m pip install Faker")
    os.system("py -m pip install datetime")
    os.system("py -m pip install secrets")
    os.system("py -m pip install typing_extensions")
    os.system("py -m pip install traceback")
    os.system("py -m pip install capsolver")
    os.system("py -m pip install httpx")
    os.system("py -m pip install keyauth")

import sys
import time
import uuid
import yaml
import faker
import ctypes
import random
import secrets
import pystyle
import capsolver
import requests
import threading
import tls_client
import urllib.parse
import concurrent.futures



import warnings

# Ignore DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

from uuid import uuid4
from faker import Faker
from pystyle import Write, Colors, Colorate, Center
from colorama import Fore, Style, Back, init
from datetime import datetime
from threading import Lock
from traceback import print_exc
from concurrent.futures import ThreadPoolExecutor

try:
    with open("config.yml") as cfg_file:
        config_data = yaml.safe_load(cfg_file)
except FileNotFoundError:
    print("CONFIG_FILE_NOT_FOUND")
    time.sleep(10)
    os.system("cls")
    sys.exit(0)
os.system("cls")
try:
    License = config_data["License"]
    vcc_repeats = config_data["Vcc_Repeats"]
    auth_retries = config_data["Auth_Retries"]
    theme = config_data["Theme"]
    logging = config_data["Logging"]
    expressor = config_data["Expressor"]
    mask_resources = config_data["Mask_Resources"]
    show_time_stamp = config_data["Show_Time_Stamp"]
    proxyless = config_data["ProxyLess"]
    use_inbuilt_proxies = config_data["Use_Inbuilt_Proxies"]
    customize = config_data["Customize"]
    nick = config_data["Nick"]
    bio = config_data["Bio"]
    address = config_data["Address"]
    country = config_data["Country"]
    postal = config_data["Postal"]
    Sleep_After_X_Amount_Of_Redeems = config_data["Sleep_After_X_Amount_Of_Redeems"]
    state = config_data["State"]
    city = config_data["City"]
    name = config_data["Name"]
    capsolver_k = config_data["Capsolver"]
    use_solver = config_data["Use_Solver"]
    service = config_data["Service"]
    remove_vccs = config_data["Remove_Vccs"]
    resume_key = config_data["Resume_Key"]
    stop_key = config_data["Stop_Key"]
    stop_threads_after_redeeming = config_data["Stop_threads_After_Redeeming"]
    Stop_Threads_If_VccError = config_data["Stop_Threads_If_VccError"]
    Smart_Resources_Saver = config_data["Smart_Resources_Saver"]
    Sleep_After_Redeem = config_data["Sleep_After_Redeem"]
    Auth_Error_Limit = config_data["Auth_Error_Limit"]
    Log_Webhook = config_data["Log_Webhook"]
    Webhook_Url = config_data["Webhook_Url"]
    Message_Id = config_data["Message_Id"]
    Change_Token = config_data["Change_Token"]
    Password = config_data["Password"]
except Exception as e:
    print("BAD_CONFIG:{}".format(e))
    time.sleep(10)
    os.system("cls")
    sys.exit(0)


started_at = time.time()
lock = Lock()

# def getchecksum():
#     md5_hash = hashlib.md5()
#     file = open(''.join(sys.argv), "rb")
#     md5_hash.update(file.read())
#     digest = md5_hash.hexdigest()
#     return digest

# keyauthapp = api(
#     name = "ok", # Application Name
#     ownerid = "f0CyttuG1A", # Owner ID
#     secret = "53d6ab625ba3392c88d7711be37878b9e4484cab30bdd2e83c0c1f587f6e8fe9", # Application Secret
#     version = "1.0", # Application Version
#     hash_to_check = getchecksum()
# )


# os.system("cls")
# if keyauthapp.checkblacklist():
#     print(Fore.RED + "You are blacklisted from our system." + Fore.RESET)
#     quit()
    
# def validate():
#     if keyauthapp.license(config_data["License"]):
#         quit()
#     else:
#         print(Fore.GREEN + "Welcome to Lunar Redeemer" + Fore.RESET)
#         time.sleep(2)
        

# def answer():
#     try:
#         key = config_data["License"]

#     except KeyboardInterrupt:
#         os._exit(1)

# if "License" not in str(config_data):
#     answer()

# validate()


os.system("cls")
ascii_art = """
        ██████╗ ███████╗██████╗ ███████╗███████╗███╗   ███╗███████╗██████╗ 
        ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝████╗ ████║██╔════╝██╔══██╗
        ██████╔╝█████╗  ██║  ██║█████╗  █████╗  ██╔████╔██║█████╗  ██████╔╝
        ██╔══██╗██╔══╝  ██║  ██║██╔══╝  ██╔══╝  ██║╚██╔╝██║██╔══╝  ██╔══██╗
        ██║  ██║███████╗██████╔╝███████╗███████╗██║ ╚═╝ ██║███████╗██║  ██║
        ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝                                                                   
"""
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(ascii_art)))
print(f"{Fore.LIGHTCYAN_EX}Theme           = {theme}")
print(f"{Fore.LIGHTCYAN_EX}Customize-Token = {customize}")
print(f"{Fore.LIGHTCYAN_EX}Log-Webhook     = {Log_Webhook}")
print(f"{Fore.LIGHTCYAN_EX}Engine-Status   = Started")
print("")
Success, Fails, Auth_Errors, Proccessed = 0, 0, 0, 0




def send_message(message):
    if Log_Webhook:
        data = {"embeds": [message]}
        response = requests.post(Webhook_Url, json=data)

        if response.status_code == 200:
            message_id = response.json().get("id")
            return message_id
        else:
            return None
    else:
        return None


def edit_message(message_id, new_embed):
    if Log_Webhook:
        edit_url = f"{Webhook_Url}/messages/{message_id}"
        data = {"embeds": [new_embed]}
        response = requests.patch(edit_url, json=data)

        if response.status_code == 200:
            return None
        else:
            return None
    else:
        return None


from datetime import datetime


class Logger:
    @staticmethod
    def update_console_title():
        elapsed = str(time.time() - started_at).split(".")[0]
        time_now = datetime.now().strftime("%H:%M:%S")
        ctypes.windll.kernel32.SetConsoleTitleW(
            f"Redeemer V2,Success:{Success},Fails:{Fails},Auth Errors:{Auth_Errors} ,Elapsed:{elapsed}Second(s),Time Right Now:{time_now}"
        )

    @staticmethod
    def remove_content(filename: str, delete_line: str) -> None:
        with open(filename, "r+") as io:
            content = io.readlines()
            io.seek(0)
            for line in content:
                if not (delete_line in line):
                    io.write(line)
            io.truncate()

    @staticmethod
    def TimeStamp() -> str:
        current_time = datetime.utcnow()
        ist_timezone = pytz.timezone(config_data["Timezone"])
        ist_time = pytz.utc.localize(current_time).astimezone(ist_timezone)
        formatted_time = ist_time.strftime("%H:%M:%S")
        return formatted_time

    @staticmethod
    def WriteToFile(name: str, content: str) -> None:
        with open(f"output/{name}", "a") as file:
            file.write(content + "\n")

    @staticmethod
    def Success(token: str, vcc: str, promo: str) -> None:
        with lock:
            if show_time_stamp:
                print(
                    Style.BRIGHT
                    + Fore.WHITE
                    + f'[{Fore.BLUE if theme == "blue" else Fore.CYAN}{Logger.TimeStamp()}{Fore.WHITE}] {Fore.WHITE}[{Fore.GREEN}{"SUCCESS" if expressor.lower() == "text" else "+"}{Fore.WHITE}] {Fore.BLUE if theme == "blue" else Fore.CYAN}- {Fore.WHITE}Redeemed Promo Successfully, Token ➔ {Fore.GREEN if theme.lower()=="blue" else Fore.GREEN}{token[:23]}{Fore.WHITE}, VCC ➔ {Fore.GREEN if theme.lower()=="blue" else Fore.GREEN}{vcc[:13]}{Fore.WHITE}, Promo ➔ {Fore.GREEN if theme.lower()=="blue" else Fore.GREEN}{promo[:10]}'
                )
            else:
                print(
                    Style.BRIGHT
                    + Fore.WHITE
                    + f'{Fore.WHITE}[{Fore.GREEN}{"SUCCESS" if expressor.lower() == "text" else "+"}{Fore.WHITE}] {Fore.BLUE if theme == "blue" else Fore.CYAN}- {Fore.WHITE}Redeemed Promo Successfully, Token ➔ {Fore.GREEN if theme=="blue" else Fore.GREEN}{token[:23]}{Fore.WHITE}, VCC ➔ {Fore.GREEN if theme.lower()=="blue" else Fore.GREEN}{vcc[:13]}{Fore.WHITE}, Promo ➔ {Fore.GREEN if theme.lower()=="blue" else Fore.GREEN}{promo[:10]}'
                )

    @staticmethod
    def Debug(content: str, token: str, vcc: str, promo: str) -> None:
        if logging.lower() == "all":
            with lock:
                if show_time_stamp:
                    print(
                        Style.BRIGHT
                        + Fore.WHITE
                        + f'[{Fore.BLUE if theme == "blue" else Fore.CYAN}{Logger.TimeStamp()}{Fore.WHITE}] {Fore.WHITE}[{Fore.MAGENTA}{"DEBUG" if expressor.lower() == "text" else "&"}{Fore.WHITE}] {Fore.BLUE if theme == "blue" else Fore.CYAN}  - {Fore.WHITE}{content}, Token ➔ {Fore.BLUE if theme.lower()=="blue" else Fore.GREEN}{token[:23]}{Fore.WHITE}, VCC ➔ {Fore.BLUE if theme.lower()=="blue" else Fore.GREEN}{vcc[:13]}{Fore.WHITE}, Promo ➔ {Fore.BLUE if theme.lower()=="blue" else Fore.GREEN}{promo[:10]}'
                    )
                else:
                    print(
                        Style.BRIGHT
                        + Fore.WHITE
                        + f'{Fore.WHITE}[{Fore.BLUE}{"DEBUG" if expressor.lower() == "text" else "&"}{Fore.WHITE}] {Fore.BLUE if theme == "blue" else Fore.CYAN}  - {Fore.WHITE}{content}, Token -> {Fore.BLUE if theme=="blue" else Fore.GREEN}{token[:23]}{Fore.WHITE}, VCC ➔ {Fore.BLUE if theme.lower()=="blue" else Fore.GREEN}{vcc[:13]}{Fore.WHITE}, Promo ➔ {Fore.BLUE if theme.lower()=="blue" else Fore.GREEN}{promo[:10]}'
                    )
        else:
            return None

    @staticmethod
    def Error(content: str, token: str, vcc: str, promo: str) -> None:
        with lock:
            if show_time_stamp:
                print(
                    Style.BRIGHT
                    + Fore.WHITE
                    + f'[{Fore.BLUE if theme == "blue" else Fore.CYAN}{Logger.TimeStamp()}{Fore.WHITE}] {Fore.WHITE}[{Fore.RED}{"ERROR" if expressor.lower() == "text" else "-"}{Fore.WHITE}] {Fore.YELLOW if theme == "blue" else Fore.YELLOW}  {Fore.CYAN}- {Fore.WHITE}{content}, Token ➔ {Fore.YELLOW if theme.lower()=="blue" else Fore.YELLOW}{token[:23]}{Fore.WHITE}, VCC ➔ {Fore.YELLOW if theme.lower()=="blue" else Fore.YELLOW}{vcc[:13]}{Fore.WHITE}, Promo ➔ {Fore.YELLOW if theme.lower()=="blue" else Fore.YELLOW}{promo[:10]}'
                )
            else:
                print(
                    Style.BRIGHT
                    + Fore.WHITE
                    + f'{Fore.WHITE}[{Fore.RED}{"ERROR" if expressor.lower() == "text" else "-"}{Fore.WHITE}] {Fore.BLUE if theme == "blue" else Fore.CYAN}  {Fore.CYAN}- {Fore.WHITE}{content}, Token ➔ {Fore.YELLOW if theme=="blue" else Fore.YELLOW}{token[:23]}{Fore.WHITE}, VCC ➔ {Fore.YELLOW if theme.lower()=="blue" else Fore.YELLOW}{vcc[:13]}{Fore.WHITE}, Promo ➔ {Fore.YELLOW if theme.lower()=="blue" else Fore.YELLOW}{promo[:10]}'
                )

    @staticmethod
    def Warn(content: str, token: str, vcc: str, promo: str) -> None:
        with lock:
            if show_time_stamp:
                print(
                    Style.BRIGHT
                    + Fore.WHITE
                    + f'[{Fore.BLUE if theme == "blue" else Fore.CYAN}{Logger.TimeStamp()}{Fore.WHITE}] {Fore.WHITE}[{Fore.YELLOW}{"WARN" if expressor.lower() == "text" else "!"}{Fore.WHITE}] {Fore.YELLOW if theme == "blue" else Fore.YELLOW}   {Fore.CYAN}- {Fore.WHITE}{content}, Token ➔ {Fore.YELLOW if theme.lower()=="blue" else Fore.YELLOW}{token[:23]}{Fore.WHITE}, VCC ➔ {Fore.YELLOW if theme.lower()=="blue" else Fore.YELLOW}{vcc[:13]}{Fore.WHITE}, Promo ➔ {Fore.YELLOW if theme.lower()=="blue" else Fore.YELLOW}{promo[:10]}'
                )
            else:
                print(
                    Style.BRIGHT
                    + Fore.WHITE
                    + f'{Fore.WHITE}[{Fore.YELLOW}{"WARN" if expressor.lower() == "text" else "!"}{Fore.WHITE}] {Fore.BLUE if theme == "blue" else Fore.CYAN}   {Fore.CYAN}- {Fore.WHITE}{content}, Token ➔ {Fore.YELLOW if theme=="blue" else Fore.YELLOW}{token[:23]}{Fore.WHITE}, VCC ➔ {Fore.YELLOW if theme.lower()=="blue" else Fore.YELLOW}{vcc[:13]}{Fore.WHITE}, Promo ➔ {Fore.YELLOW if theme.lower()=="blue" else Fore.YELLOW}{promo[:10]}'
                )


if not capsolver == "":
    capsolver.api_key = capsolver_k
else:
    pass

lock = Lock()
fkr = Faker()
genned = 0
AUDIO_FILE_PATH = "musics/s2.mp4"

import webbrowser
def play_audio_background(file_path):
    abs_file_path = os.path.abspath(file_path)
    webbrowser.open_new("file://" + abs_file_path)
def gettimestamp() -> str:
    return ''.join(datetime.now().strftime('%H:%M:%S'))
def Sprint(tag,message,color) -> None:
  with lock:
    print('\n'+Style.BRIGHT + f'{Fore.BLACK}[{gettimestamp()}] {color}[{tag}]  {Fore.WHITE}{message}{Style.RESET_ALL}\n')
def play_music():
  for i in range(10):
    if config_data["play_music"]:
        Sprint("MUSIC", f"PLAYING MUSIC [{Fore.BLUE}ANOTHER LOVE X SUMMERTIME SADNESS{Fore.WHITE}] IN 5 SECONDS", Fore.MAGENTA)
        time.sleep(5)

        # Call play_audio_background function with appropriate audio file path
        play_audio_background(AUDIO_FILE_PATH)
        time.sleep(280)
        
        Sprint("MUSIC", f"PLAYING MUSIC [{Fore.BLUE}ANOTHER LOVE X SET FIRE TO THE RAIN | SLOWED{Fore.WHITE}] IN 5 SECONDS", Fore.MAGENTA)
        time.sleep(5)
        play_audio_background("musics/s3.mp4")
        time.sleep(258)

        Sprint("MUSIC", f"PLAYING MUSIC [{Fore.BLUE}SOMEWHERE ONLY WE KNOW{Fore.WHITE}] IN 5 SECONDS", Fore.MAGENTA)
        time.sleep(5)
        play_audio_background("musics/s1.mp4")
        time.sleep(268)

    else:
        pass
def get_email(proxy):
    try:
        jsonr = requests.get("https://api.tempmail.lol/generate", proxies=proxy)
        return jsonr.json()["address"] + ";" + jsonr.json()["token"]
    except:
        print("TEMP_MAIL_SITE_DOWN TRY AGAIN LATER!")


def auth_email(proxy, token):
    try:
        jsonr2 = requests.get("https://api.tempmail.lol/auth/" + token, proxies=proxy)
        return jsonr2.json()
    except:
        print("TEMP_MAIL_SITE_DOWN TRY AGAIN LATER!")


with open("input/Proxies.txt", "r") as file:
    proxies = file.read().splitlines()
if not proxyless:
    proxies = {"https": "http://" + random.choice(proxies)}

else:
    proxies = None
Logger.update_console_title()
DEFAULT_X_SUPER_PROPERTIES = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExOC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE4LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjIzNjg1MCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"

class Worker:
    def __init__(self, promo: str, vcc: str, token: str, proxy: str | None):
        try:
            self.session = tls_client.Session(client_identifier="chrome_118")
            self.full_promo = promo
            self.full_vcc = vcc
            self.full_token = token
            if proxyless == False and not proxy == None:
                self.session.proxies = {
                    "http": "http://" + proxy,
                    "https": "https://" + proxy,
                }
            else:
                self.session.proxies = None
            self.xprop = DEFAULT_X_SUPER_PROPERTIES
            self.ua = DEFAULT_USER_AGENT
            if "@" in token:
                self.token = token.split(":")[2]
            elif not "@" and not ":" in token:
                self.token = token
            else:
                self.token = token
            if ":" in vcc:
                self.ccn = vcc.split(":")[0]
                self.exp_day = vcc.split(":")[1][:2]
                self.exp_year = vcc.split(":")[1][2:]
                self.cvc = vcc.split(":")[2]
            elif "|" in vcc:
                self.ccn, self.exp_day, self.exp_year, self.cvc = vcc.split("|")
            else:
                Logger.Error("Wrong Vcc Format", "N/A", "N/A", vcc)
                return
            if "-" in promo:
                self.type = "Alienware"
            else:
                self.type = "Xbox GamePass"
            self.RETRIES = 0
        except Exception as e:
            print(e)

    def Obtain_Cookies(self) -> dict:
        cookies = {}
        try:
            response = self.session.get("https://discord.com")
            for cookie in response.cookies:
                if cookie.name.startswith("__") and cookie.name.endswith("uid"):
                    cookies[cookie.name] = cookie.value
            return cookies
        except Exception as e:
            return {}

    def Format_Promotion(self) -> str | None:
        global Fails
        try:
            if self.type == "Alienware" or "Xbox GamePass":
                if "https://discord.com/billing/promotions/" in self.full_promo:
                    code = self.full_promo.split(
                        "https://discord.com/billing/promotions/"
                    )[1]
                else:
                    code = self.full_promo.split("https://promos.discord.gg/")[1]
                return code
        except Exception as e:
            Logger.Error(
                f"Failed To Get Promo Code : {e}",
                self.token,
                self.full_vcc,
                self.full_promo,
            )
            Fails += 1
            Logger.WriteToFile("bad_promo.txt", self.full_token)
            return None

    def RemoveCard(self, payment_id: str):
        try:
            try:
                self.headers = {
                    "authority": "discord.com",
                    "accept": "*/*",
                    "accept-language": "en-US,en;q=0.9",
                    "authorization": self.token,
                    "referer": "https://discord.com/channels/@me",
                    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": self.ua,
                    "x-debug-options": "bugReporterEnabled",
                    "x-discord-locale": "en-US",
                    "x-discord-timezone": "Europe/Budapest",
                    "x-super-properties": self.xprop,
                }
                response = self.session.get(
                    "https://discord.com/api/v9/users/@me/billing/subscriptions",
                    headers=self.headers,
                    cookies=self.Obtain_Cookies(),
                )
                if '"id"' in response.text:
                    self.subscription = response.json()[0]["id"]
                else:
                    Logger.Error(
                        f"Failed To Get Subscription Id : {response.json()}",
                        self.token,
                        self.full_vcc,
                        self.full_promo,
                    )
                    return False
            except Exception as e:
                Logger.Error(
                    f"Failed To Get Subscription Id : {e}",
                    self.token,
                    self.full_vcc,
                    self.full_promo,
                )
                print_exc()
                return False
            self.headers = {
                "authority": "discord.com",
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9",
                "authorization": self.token,
                "content-type": "application/json",
                "origin": "https://discord.com",
                "referer": "https://discord.com/channels/@me",
                "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": self.ua,
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-discord-timezone": "Europe/Budapest",
                "x-super-properties": self.xprop,
            }
            self.json = {
                "payment_source_token": None,
                "gateway_checkout_context": None,
                "items": [],
            }
            self.params = {
                "location_stack": [
                    "user settings",
                    "subscription header",
                    "premium subscription cancellation modal",
                ],
            }
            response = self.session.patch(
                f"https://discord.com/api/v9/users/@me/billing/subscriptions/{self.subscription}",
                headers=self.headers,
                json=self.json,
                params=self.params,
                cookies=self.Obtain_Cookies(),
            )
            if response.status_code in (200, 204):
                pass
            else:
                Logger.Error(
                    f"Failed To Cancle Subscription : {response.status_code}",
                    self.token,
                    self.full_vcc,
                    self.full_promo,
                )
                return False
            response = self.session.delete(
                f"https://discord.com/api/v9/users/@me/billing/payment-sources/{payment_id}",
                headers=self.headers,
                cookies=self.Obtain_Cookies(),
            )
            if response.status_code in (200, 204):
                Logger.Debug("Removed Card", self.token, self.full_vcc, self.full_promo)
                return False
            else:
                Logger.Error(
                    f"Failed To Remove Card : {response.status_code}",
                    self.token,
                    self.full_vcc,
                    self.full_promo,
                )
                return False
        except Exception as e:
            Logger.Error(
                f"Unhandled Exception During Remove Card Function : {e}",
                self.token,
                self.full_vcc,
                self.full_promo,
            )
            return False

    def RedeemPromo(self, payment_source: str) -> bool:
        global Fails
        global Auth_Errors
        global Success
        try:
            self.Formatted_Code = self.Format_Promotion()
            if not self.Formatted_Code == None:
                self.headers = {
                    "accept": "*/*",
                    "accept-language": "en-US,en;q=0.9",
                    "content-type": "text/plain;charset=UTF-8",
                    "origin": "https://m.stripe.network",
                    "referer": "https://m.stripe.network/",
                    "sec-ch-ua": '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "cross-site",
                    "user-agent": self.ua,
                }
                response = self.session.post(
                    "https://m.stripe.com/6",
                    headers=self.headers,
                    data="JTdCJTIybXVpZCUyMiUzQSUyMjI5ZGZiM2FjLTUwZGUtNDYwYi05YzYxLWI5M2U5YmRiMzgzOTM2MzUxYSUyMiUyQyUyMnNpZCUyMiUzQSUyMjQwNzM0ZWEwLTU5M2EtNGI3MS1hZjFkLTJmZjdmMmRkZWY4MjA1NGNlZCUyMiUyQyUyMnVybCUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGR1M3aHFua1pCUnBQXzdXbjktQ0dGaHpxNGtyMlgzSkM0QTNrNkJEQnZwRS5nMnU5LWhxWnZHSXFZSmNQbFBmd0pBZi12M1JneUtfeDFOcHB6QWxBMTJNJTJGQlFkTnl6cExVNG5NNllLenpuYVAxWENEMVcwREoxejNUcG50ejJacElxcyUyRjBzTHkxUFBJSTJobTNPREhpTFp1S2M2UmR5Y0xFMVZybXJ5bnRzWFh0N28lMkZlVW1nMjg3dHRDOFE0elc3Rm9OcUtCRHVSMnRpUklyaEZrTkRiZFpVSy1zJTIyJTJDJTIyc291cmNlJTIyJTNBJTIybW91c2UtdGltaW5ncy0xMCUyMiUyQyUyMmRhdGElMjIlM0ElNUIxMTAlMkM5JTJDMCUyQzglMkMxNiUyQzUlMkMxMCUyQzglMkM5JTJDNyU1RCU3RA==",
                )
                if not response.status_code in (200, 204):
                    stripe_cookies = None
                else:
                    self.muid = response.json()["muid"]
                    self.guid = response.json()["guid"]
                    self.sid = response.json()["sid"]
                    stripe_cookies = {
                        "__stripe_mid": self.muid,
                        "__stripe_sid": self.sid,
                    }
                    stripe_cookies_2 = {"__stripe_mid": self.muid}
                self.cookie = self.Obtain_Cookies()
                self.cookie_with_stripe = self.cookie.update(stripe_cookies)

                self.headers = {
                    "authority": "discord.com",
                    "accept": "*/*",
                    "accept-language": "en-US,en;q=0.9",
                    "authorization": self.token,
                    "content-type": "application/json",
                    "origin": "https://discord.com",
                    "referer": f"https://discord.com/billing/promotions/{self.Formatted_Code}",
                    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": self.ua,
                    "x-debug-options": "bugReporterEnabled",
                    "x-discord-locale": "en-US",
                    "x-discord-timezone": "Europe/Budapest",
                    "x-super-properties": self.xprop,
                }
                self.json = {
                    "channel_id": None,
                    "payment_source_id": payment_source,
                    "gateway_checkout_context": None,
                }
                response = self.session.post(
                    f"https://discord.com/api/v9/entitlements/gift-codes/{self.Formatted_Code}/redeem",
                    headers=self.headers,
                    json=self.json,
                    cookies=self.cookie_with_stripe,
                )
                if '"id"' in response.text:
                    Logger.Success(self.token, self.full_vcc, self.full_promo)
                    Success += 1
                    if remove_vccs == True:
                        self.RemoveCard(payment_source)
                    else:
                        pass
                    Logger.WriteToFile("Success.txt", self.full_token)
                    return True
                else:
                    if "Authentication" in response.text:
                        self.headers = {
                            "accept": "*/*",
                            "accept-language": "en-US,en;q=0.9",
                            "authorization": self.token,
                            "referer": "https://discord.com/billing/promotions/"
                            + self.Formatted_Code,
                            "sec-ch-ua": '"Microsoft Edge";     v="123", "Not:A-Brand"; v="8", "Chromium"; v="123"',
                            "sec-ch-ua-mobile": "?0",
                            "sec-ch-ua-platform": '"Windows"',
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": self.ua,
                            "x-debug-options": "bugReporterEnabled",
                            "x-discord-locale": "en-US",
                            "x-discord-timezone": "Asia/Katmandu",
                            "x-super-properties": self.xprop,
                        }
                        try:
                            nz = self.Obtain_Cookies()
                            b_3_response = self.session.get(
                                f'https://discord.com/api/v9/users/@me/billing/stripe/payment-intents/payments/{response.json()["payment_id"]}',
                                headers=self.headers,
                                cookies=nz.update(stripe_cookies_2),
                            )
                            full_secret = str(
                                b_3_response.json()[
                                    "stripe_payment_intent_client_secret"
                                ]
                            )
                            secret = str(
                                b_3_response.json()[
                                    "stripe_payment_intent_client_secret"
                                ]
                            ).split("_secret_")[0]
                            self.headers = {
                                "accept": "application/json",
                                "accept-language": "en-US,en;q=0.9",
                                "content-type": "application/x-www-form-urlencoded",
                                "origin": "https://js.stripe.com",
                                "referer": "https://js.stripe.com/",
                                "sec-ch-ua": '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                                "sec-ch-ua-mobile": "?0",
                                "sec-ch-ua-platform": '"Windows"',
                                "sec-fetch-dest": "empty",
                                "sec-fetch-mode": "cors",
                                "sec-fetch-site": "same-site",
                                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
                            }
                            self.data = {
                                "expected_payment_method_type": "card",
                                "use_stripe_sdk": "true",
                                "key": "pk_live_CUQtlpQUF0vufWpnpUmQvcdi",
                                "client_secret": full_secret,
                            }

                            three_ds_resp = self.session.post(
                                f"https://api.stripe.com/v1/payment_intents/{secret}/confirm",
                                headers=self.headers,
                                params=self.data,
                            )
                            three_ds_source = three_ds_resp.json()["next_action"][
                                "use_stripe_sdk"
                            ]["three_d_secure_2_source"]
                            three_ds_2_resp = self.session.post(
                                "https://api.stripe.com/v1/3ds2/authenticate",
                                headers=self.headers,
                                data=f"source={three_ds_source}&browser=%7B%22fingerprintAttempted%22%3Afalse%2C%22fingerprintData%22%3Anull%2C%22challengeWindowSize%22%3Anull%2C%22threeDSCompInd%22%3A%22Y%22%2C%22browserJavaEnabled%22%3Afalse%2C%22browserJavascriptEnabled%22%3Atrue%2C%22browserLanguage%22%3A%22en-US%22%2C%22browserColorDepth%22%3A%2224%22%2C%22browserScreenHeight%22%3A%221080%22%2C%22browserScreenWidth%22%3A%221920%22%2C%22browserTZ%22%3A%22-345%22%2C%22browserUserAgent%22%3A%22Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F123.0.0.0+Safari%2F537.36+Edg%2F123.0.0.0%22%7D&one_click_authn_device_support[hosted]=false&one_click_authn_device_support[same_origin_frame]=false&one_click_authn_device_support[spc_eligible]=false&one_click_authn_device_support[webauthn_eligible]=false&one_click_authn_device_support[publickey_credentials_get_allowed]=true&key=pk_live_CUQtlpQUF0vufWpnpUmQvcdi",
                            )
                        except Exception as e:
                            if self.RETRIES < auth_retries:
                                time.sleep(20)
                                self.RedeemPromo(payment_source)
                                self.RETRIES += 1
                            else:
                                Logger.Warn(
                                    f"Auth Error Passed Limit",
                                    self.token,
                                    self.full_vcc,
                                    self.full_promo,
                                )
                                Logger.WriteToFile("bad_vcc.txt", self.full_vcc)
                                return False
                    if "Authentication" in response.text and self.RETRIES < vcc_repeats:
                        self.RedeemPromo(payment_source)
                        self.RETRIES += 1
                        return False
                    Logger.Error(
                        f"Failed To Redeem Promo : {response.json()}",
                        self.token,
                        self.full_vcc,
                        self.full_promo,
                    )
                    Fails += 1
                    Logger.WriteToFile("bad_vcc.txt", self.full_vcc)
                    return False
            else:
                return False
        except Exception as e:
            Logger.Error(
                f"Unknown Exception Occured : {e}",
                self.token,
                self.full_vcc,
                self.full_promo,
            )
            Logger.WriteToFile("bad_vcc.txt", self.full_vcc)
            return False

    def AddCard(self) -> bool:
        global Fails
        try:
            Logger.Debug("Using ", self.token, self.full_vcc, self.full_promo)
            self.headers = {
                "authority": "api.stripe.com",
                "accept": "application/json",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://js.stripe.com",
                "referer": "https://js.stripe.com/",
                "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
                "user-agent": self.ua,
            }
            self.data = f"card[number]={self.ccn}&card[cvc]={self.cvc}&card[exp_month]={self.exp_day}&card[exp_year]={self.exp_year}&guid={uuid.uuid4()}&muid={uuid.uuid4()}&sid={uuid.uuid4()}&payment_user_agent=stripe.js%2F28b7ba8f85%3B+stripe-js-v3%2F28b7ba8f85%3B+split-card-element&referrer=https%3A%2F%2Fdiscord.com&time_on_page=415638&key=pk_live_CUQtlpQUF0vufWpnpUmQvcdi&pasted_fields=number%2Ccvc"
            response = self.session.post(
                "https://api.stripe.com/v1/tokens", headers=self.headers, data=self.data
            )
            if '"id"' in response.text:
                self.cardtoken = response.json()["id"]
            else:
                Logger.Error(
                    f'Failed To Tokenize Card : {response.json()["error"]["code"]}',
                    self.token,
                    self.full_vcc,
                    self.full_promo,
                )
                Logger.WriteToFile("bad_vcc.txt", self.full_vcc)
                Fails += 1
                return False
            self.headers = {
                "authority": "discord.com",
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9",
                "authorization": self.token,
                "origin": "https://discord.com",
                "referer": "https://discord.com/channels/@me",
                "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": self.ua,
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-discord-timezone": "Europe/Budapest",
                "x-super-properties": self.xprop,
            }
            response = self.session.post(
                "https://discord.com/api/v9/users/@me/billing/stripe/setup-intents",
                headers=self.headers,
                cookies=self.Obtain_Cookies(),
            )
            if '"client_secret"' in response.text:
                self.csTok = response.json()["client_secret"]
                self.Stok = str(self.csTok).split("_secret_")[0]
            else:
                Logger.Error(
                    f"Failed To Setup Stripe Intents : {response.json()}",
                    self.token,
                    self.full_vcc,
                    self.full_promo,
                )
                Fails += 1
                Logger.WriteToFile("bad_token.txt", self.full_token)
                return False
            self.json = {
                "billing_address": {
                    "name": name,
                    "line_1": address,
                    "line_2": "",
                    "city": city,
                    "state": state,
                    "postal_code": postal,
                    "country": country,
                    "email": "",
                },
            }
            response = self.session.post(
                "https://discord.com/api/v9/users/@me/billing/payment-sources/validate-billing-address",
                headers=self.headers,
                json=self.json,
                cookies=self.Obtain_Cookies(),
            )
            if '"token"' in response.text:
                self.billing_token = response.json()["token"]
            else:
                Logger.Error(
                    f"Failed To Retrieve Billing Token : {response.json()}",
                    self.token,
                    self.full_vcc,
                    self.full_promo,
                )
                Fails += 1
                Logger.WriteToFile("bad_vcc.txt", self.full_promo)
                return False
            self.headers = {
                "authority": "api.stripe.com",
                "accept": "application/json",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://js.stripe.com",
                "referer": "https://js.stripe.com/",
                "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
                "user-agent": self.ua,
            }
            self.data = f"payment_method_data[type]=card&payment_method_data[card][token]={self.cardtoken}&payment_method_data[billing_details][address][line1]={address}&payment_method_data[billing_details][address][line2]=&payment_method_data[billing_details][address][city]={city}&payment_method_data[billing_details][address][state]={state}&payment_method_data[billing_details][address][postal_code]={postal}&payment_method_data[billing_details][address][country]={country}&payment_method_data[billing_details][name]={name}&payment_method_data[guid]={uuid.uuid4()}&payment_method_data[muid]={uuid.uuid4()}&payment_method_data[sid]={uuid.uuid4()}&payment_method_data[payment_user_agent]=stripe.js%2F28b7ba8f85%3B+stripe-js-v3%2F28b7ba8f85&payment_method_data[referrer]=https%3A%2F%2Fdiscord.com&payment_method_data[time_on_page]=707159&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_CUQtlpQUF0vufWpnpUmQvcdi&client_secret={self.csTok}"
            response = self.session.post(
                f"https://api.stripe.com/v1/setup_intents/{self.Stok}/confirm",
                headers=self.headers,
                data=self.data,
            )
            try:
                if '"id"' in response.text:
                    self.CardSCMAIN = response.json()["id"]
                    self.pmTok = response.json()["payment_method"]
                else:
                    Logger.Error(
                        f"Failed To Retrieve Payment Method : {response.json()}",
                        self.token,
                        self.full_vcc,
                        self.full_promo,
                    )
                    Fails += 1
                    Logger.WriteToFile("bad_vcc.txt", self.full_vcc)
                    return False
            except:
                Logger.Error(
                    f"Failed To Retrieve Payment Method : {response.json()}",
                    self.token,
                    self.full_vcc,
                    self.full_promo,
                )
                Fails += 1
                Logger.WriteToFile("bad_vcc.txt", self.full_vcc)
                return False
            self.headers = {
                "authority": "discord.com",
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9",
                "authorization": self.token,
                "content-type": "application/json",
                "origin": "https://discord.com",
                "referer": "https://discord.com/channels/@me",
                "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": self.ua,
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-discord-timezone": "Europe/Budapest",
                "x-super-properties": self.xprop,
            }
            self.json = {
                "payment_gateway": 1,
                "token": self.pmTok,
                "billing_address": {
                    "name": name,
                    "line_1": address,
                    "line_2": None,
                    "city": city,
                    "state": state,
                    "postal_code": postal,
                    "country": country,
                    "email": "",
                },
                "billing_address_token": self.billing_token,
            }
            response = self.session.post(
                "https://discord.com/api/v9/users/@me/billing/payment-sources",
                headers=self.headers,
                json=self.json,
                cookies=self.Obtain_Cookies(),
            )
            if '"id"' in response.text:
                Logger.Debug(
                    "Added Card Successfully",
                    self.token,
                    self.full_vcc,
                    self.full_promo,
                )
                payment_source_id = response.json()["id"]
                self.RedeemPromo(payment_source=payment_source_id)
            else:
                Logger.Error(
                    f"Failed To Add Card : {response.json()}",
                    self.token,
                    self.full_vcc,
                    self.full_promo,
                )
                Fails += 1
                Logger.WriteToFile("bad_vcc.txt", self.full_vcc)
                return False
        except Exception as e:
            Logger.Error(
                f"Unhandled Exception During Add Card Function : {e}",
                self.token,
                self.full_vcc,
                self.full_promo,
            )
            Fails += 1
            print_exc()
            return False


def Obtain_Cookies() -> dict:
    cookies = {}
    session = tls_client.Session(
        client_identifier="chrome_112", random_tls_extension_order=True
    )
    try:
        response = session.get("https://discord.com")
        for cookie in response.cookies:
            if cookie.name.startswith("__") and cookie.name.endswith("uid"):
                cookies[cookie.name] = cookie.value
        return cookies
    except Exception as e:
        return {}


def nameChanger(token: str, dName: str):
    __sessionx = tls_client.Session(
        client_identifier="chrome_112", random_tls_extension_order=True
    )
    if "@" in token:
        token = token.split(":")[2]
    else:
        token = token
    ua = DEFAULT_USER_AGENT
    xprop = DEFAULT_X_SUPER_PROPERTIES
    headers = {
        "authority": "discord.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": token,
        "content-type": "application/json",
        "origin": "https://discord.com",
        "referer": "https://discord.com/channels/@me",
        "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": ua,
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
        "x-discord-timezone": "Europe/Budapest",
        "x-super-properties": xprop,
    }
    json_data = {
        "global_name": str(dName),
    }

    try:
        response = __sessionx.patch(
            "https://discord.com/api/v9/users/@me",
            headers=headers,
            json=json_data,
            cookies=Obtain_Cookies(),
        )

    except Exception as e:
        return

    if response.status_code == 200:
        Logger.Debug("Customized Token", token, "N/A", "N/A")

    else:
        Logger.Warn("Failed To Customize Token", "N/A", "N/A", "N/A")


import random


def process_token(vcc, promo, token):
    instance = Worker(promo, vcc, token, None)
    instance.AddCard()


with open("input/Promotion_Links.txt", "r") as f:
    promos = f.read().splitlines()

with open("input/Tokens.txt", "r") as f:
    tokens = f.read().splitlines()

with open("input/VCCS.txt", "r") as f:
    vccs = f.read().splitlines()

with open("input/Proxies.txt", "r") as f:
    proxies = f.read().splitlines()

proxy = random.choice(proxies) if not proxyless else None

token_finished = False
vcc_finished = False
from itertools import cycle

used_p = []
used_t = []
used_v = []
vcc_count = {}  # Dictionary to keep track of VCC usage count

if Sleep_After_X_Amount_Of_Redeems > 0:
    Sleep_After_X_Amount_Of_Redeems = Sleep_After_X_Amount_Of_Redeems
else:
    Sleep_After_X_Amount_Of_Redeems = len(tokens) + 1
    Sleep_After_X_Amount_Of_Redeems_Delay = config_data[
        "Sleep_After_X_Amount_Of_Redeems_Delay"
    ]
Stop_threads_After_Redeeming = config_data["Stop_threads_After_Redeeming"]

if Stop_threads_After_Redeeming > 0:
    Stop_threads_After_Redeeming = Stop_threads_After_Redeeming
else:
    Stop_threads_After_Redeeming = len(tokens) + 1


pause_event = threading.Event()
server_inv = config_data["Guild_Invite"]


def get_fingerprint():
    try:
        fingerprint = httpx.get(f"https://discord.com/api/v10/experiments")
        return fingerprint.json()["fingerprint"]
    except Exception as e:
        return get_fingerprint()


class Booster:
    def __init__(self, token: str):
        self.full = token
        self.times = 0
        if "https://discord.gg/" in server_inv:
            self.invite = server_inv.replace("https://discord.gg/", "")

        elif "discord.gg" in server_inv and not "https" in server_inv:
            self.invite = server_inv.replace("discord.gg/", "")
        elif not "https://discord" in server_inv and ".gg" in server_inv:
            self.invite = server_inv.replace(".gg/", "")

        elif not "https://discord" and ".gg/" in server_inv:
            self.invite = server_inv

        if "@" in token:
            self.token = token.split(":")[2]
        else:
            self.token = token

        self.session = tls_client.Session(
            client_identifier="chrome_109", random_tls_extension_order=True
        )
        self.session2 = tls_client.Session(
            client_identifier="chrome_109", random_tls_extension_order=True
        )
        if not use_inbuilt_proxies:
            self.session.proxies = None
            self.session2.proxies = None
        else:
            self.session.proxies = None
            self.session2.proxies = None

    def obt_cookies(self):
        cookies = {}
        try:
            response = self.session.get("https://discord.com")
            for cookie in response.cookies:
                if cookie.name.startswith("__") and cookie.name.endswith("uid"):
                    cookies[cookie.name] = cookie.value
            return cookies
        except Exception as e:
            Logger.Warn(f"Failed To Obtain Cookies", "N/A", "N/A", "N/A")
            return {}

    def joiner(self):
        self.headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "authorization": self.token,
            "content-type": "application/json",
            "origin": "https://discord.com",
            "referer": "https://discord.com/channels/@me",
            "sec-ch-ua": '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6bnVsbCwibG9jYXRpb25fY2hhbm5lbF9pZCI6IjEyMDk4MjYwMDAzNTIwNTk0MDMiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjEsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiIxMjIzNjE2NDEyMDQwNTYwNjcwIn0=",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-discord-timezone": "Europe/Budapest",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMy4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjMuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjMuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vZGlzY29yZC5jb20vP2Rpc2NvcmR0b2tlbj1NVEEzTURReU56RXhNVGM1TVRJNE5ESTROQS5HYWNhYnIuVE9NZUVzbHdiczJ2OFRlck4wOTM3SzVvS0ZFMFZyZW5fdWF6Q1kiLCJyZWZlcnJpbmdfZG9tYWluIjoiZGlzY29yZC5jb20iLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjgwMjMxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        }
        try:
            response = self.session.post(
                f"https://discord.com/api/v9/invites/{self.invite}",
                headers=self.headers,
                json={
                    "session_id": "".join(
                        random.choice(string.ascii_lowercase)
                        + random.choice(string.digits)
                        for _ in range(16)
                    )
                },
                cookies=self.obt_cookies(),
            )
        except Exception as e:
            Logger.Warn(f"Proxy/Network Error : {e}", "N/A", "N/A", "N/A")
            return False

        if response.status_code in (200, 204):
            Logger.Debug(f"Joined Server.", "N/A", "N/A", "N/A")
            self.guild = response.json()["guild"]["id"]
            return True
        elif response.status_code == 401:
            Logger.Debug(f"Invalid Token :/", "N/A", "N/A", "N/A")
            with open("output/invalid_tokens.txt", "a") as f:
                f.write(self.full + "\n")
            return False
        elif "Unknown Invite" in response.json():
            Logger.Warn(f"Failed To Join Server.", "N/A", "N/A", "N/A")
            return False
        else:
            if "captcha" in response.text:
                Logger.Warn(f"Failed To Join Server : Captcha.", "N/A", "N/A", "N/A")
                return False
            else:
                Logger.Warn(f"Failed To Join Server.", "N/A", "N/A", "N/A")
                return False

    def put_boost(self) -> bool:
        try:
            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "authorization": self.token,
                "content-type": "application/json",
                "origin": "https://discord.com",
                "referer": "https://discord.com",
                "sec-ch-ua": f'"Google Chrome";v="108", "Chromium";v="108", "Not=A?Brand";v="8"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
                "x-context-properties": "eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjY3OTg3NTk0NjU5NzA1NjY4MyIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiIxMDM1ODkyMzI4ODg5NTk0MDM2IiwibG9jYXRpb25fY2hhbm5lbF90eXBlIjowfQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMy4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjMuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjMuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vZGlzY29yZC5jb20vP2Rpc2NvcmR0b2tlbj1NVEEzTURReU56RXhNVGM1TVRJNE5ESTROQS5HYWNhYnIuVE9NZUVzbHdiczJ2OFRlck4wOTM3SzVvS0ZFMFZyZW5fdWF6Q1kiLCJyZWZlcnJpbmdfZG9tYWluIjoiZGlzY29yZC5jb20iLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjgwMjMxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
                "fingerprint": get_fingerprint(),
            }

            boost_dat = self.session.get(
                f"https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots",
                headers=headers,
                cookies=self.obt_cookies(),
            )
            if boost_dat.status_code == 200:
                boost_data = boost_dat.json()
                for boost in boost_data:
                    boost_id = boost["id"]
                    payload = {"user_premium_guild_subscription_slot_ids": [boost_id]}
                    boosted = self.session.put(
                        f"https://discord.com/api/v9/guilds/{self.guild}/premium/subscriptions",
                        json=payload,
                        headers=headers,
                    )
                    if boosted.status_code == 201:
                        self.times += 1
                        Logger.Debug(
                            f"Boosted Server -> {self.invite}.", "N/A", "N/A", "N/A"
                        )
                    elif (
                        "Must wait for premium server subscription cooldown to expire"
                        in boosted.text
                    ):
                        Logger.Warn(
                            f"Excp In Boosting -> Insufficient Boosts Left.",
                            "N/A",
                            "N/A",
                            "N/A",
                        )
                    else:
                        Logger.error(
                            "serve.py",
                            f"Failed to boost, reason: {Fore.YELLOW}{boosted.json()}",
                        )
            else:
                Logger.Warn(
                    "Failed To Boost Server : Boost Data Fail", "N/A", "N/A", "N/A"
                )
        except Exception as e:
            Logger.Warn(f"Excp In Boosting -> {e}.", "N/A", "N/A", "N/A")


Use_Boost_Tool = config_data["Use_Boost_Tool"]


def process_token(vcc, promo, token):
    instance = Worker(promo, vcc, token, None)
    instance.AddCard()
    if customize:
        nameChanger(nick, token)
    else:
        pass
    if Use_Boost_Tool:
        instance = Booster(token)
        joinerBool = instance.joiner()
        if joinerBool:
            instance.put_boost()
        else:
            pass
    else:
        pass
    Logger.remove_content("input/Promotion_Links.txt", promo)
    Logger.remove_content("input/Tokens.txt", token)


def pause_threads():
    pause_event.set()
    Sprint("PAUSED","THREADS PAUSED PRESS '#' IN YOUR KEYBOARD TO RESUME",Fore.YELLOW)


def resume_threads():
    pause_event.clear()
    Sprint("RESUMED","THREADS RESUMED",Fore.YELLOW)


def keypress_listener():
    while True:
        if keyboard.is_pressed("$"):
            pause_threads()
            while keyboard.is_pressed("$"):  # Wait until key is released
                time.sleep(0.1)
        elif keyboard.is_pressed("#"):
            resume_threads()
            while keyboard.is_pressed("#"):  # Wait until key is released
                time.sleep(0.1)


def update_console_title_continuously():
    while True:
        Logger.update_console_title()
        time.sleep(1)


if __name__ == "__main__":
    Sleep_After_X_Amount_Of_Redeems_Delay = config_data[
        "Sleep_After_X_Amount_Of_Redeems_Delay"
    ]
    threads = 1
    try:
        print(
            f"{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}{Logger.TimeStamp()}{Fore.WHITE}] [{Fore.BLUE}TOOL{Fore.WHITE}] {Fore.MAGENTA}>>> {Fore.WHITE}Hey, Please Enter {Fore.BLUE}Thread Amount {Fore.WHITE}To Run."
        )
        threads = int(
            input(
                f"{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}{Logger.TimeStamp()}{Fore.WHITE}] [{Fore.YELLOW}USER{Fore.WHITE}] {Style.BRIGHT}{Fore.YELLOW}>>> {Fore.WHITE}"
            )
        )
    except ValueError:
        print(
            f"{Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}{Logger.TimeStamp()}{Fore.WHITE}] [{Fore.BLUE}TOOL{Fore.WHITE}] {Fore.MAGENTA}>>> {Fore.WHITE}Hey, The Thread Provided Is Not Valid The Tool Is Now Running In Default 1 Thread."
        )
        threads = 1
    print("")
    if Log_Webhook:
        new_embed = {
            "title": "Lunar Redeemer Started",
            "description": "**Will Send A Detailed Info After Completing**",
            "color": 800080,
        }

        send_message(new_embed)
    # Start a listener thread for keypress events
    listener_thread = threading.Thread(target=keypress_listener, daemon=True)
    listener_thread.start()

    # Start a thread to update console title continuously
    title_update_thread = threading.Thread(
        target=update_console_title_continuously, daemon=True
    )
    title_update_thread.start()
    if config_data["play_music"]:
      music_thread = threading.Thread(target=play_music)

    # Start the music thread
      music_thread.start()
    with ThreadPoolExecutor(max_workers=threads) as execute:
        try:
            vcc_batch = cycle(vccs)
            token_batch = cycle(tokens)
            promo_batch = cycle(promos)
        except:
            Logger.Error(
                "Insufficient Materials, Please Put Sufficient Materials In The Files",
                "N/A",
                "N/A",
                "N/A",
            )
            time.sleep(40)
            sys.exit(0)
        vcc_finished = False
        proccessedTok = 0
        while not vcc_finished:
            try:
              vcc = next(vcc_batch)
            except:
               Sprint('MATERIALS',"INSUFFICIENT MATERIALS",Fore.YELLOW)
               time.sleep(1000)
            for _ in range(vcc_repeats):
                if pause_event.is_set():
                    Sprint("PAUSED","THREADS PAUSED PRESS '#' IN YOUR KEYBOARD TO RESUME",Fore.YELLOW)
                    time.sleep(5)
                    continue

                if proccessedTok >= Sleep_After_X_Amount_Of_Redeems:
                    Logger.Debug(
                        "Sleeping After Redemption | As Mentioned In Config For Sleep After X Amount Of Redeems",
                        "N/A",
                        "N/A",
                        "N/A",
                    )
                    time.sleep(Sleep_After_X_Amount_Of_Redeems_Delay)
                    Sleep_After_X_Amount_Of_Redeems = 0
                try:

                    token = next(token_batch)
                    promo = next(promo_batch)
                except:
                    Logger.Error(
                        "Insufficient Materials, Please Put Sufficient Materials In The Files",
                        "N/A",
                        "N/A",
                        "N/A",
                    )
                    time.sleep(40)
                    sys.exit(0)
                process_token(vcc, promo, token)
                proccessedTok += 1
                Logger.Debug("Sleeping After Redemption", "N/A", "N/A", "N/A")
                time.sleep(Sleep_After_Redeem)
                if vcc == vccs[-1]:
                    vcc_finished = True
                if token == tokens[-1] and vcc_finished:
                    Sprint("MATERIALS","MATERIALS FINISHED PRESS ENTER TO EXIT",Fore.YELLOW)
                    if Log_Webhook:
                       new_embed = {
        "title": "Lunar Redeemer | Threads Completed",
        "description": "",
        "color": 800080,
        "fields": [
            {"name": "Success", "value": "```" + str(Success) + "```", "inline": False},
            {"name": "Fails", "value": "```" + str(Fails) + "```", "inline": True},
            {
                "name": "Auth Errors",
                "value": "```" + str(Auth_Errors) + "```",
                "inline": False,
            },
            {
                "name": "Proccessed",
                "value": "```" + str(Success + Fails) + "```",
                "inline": True,
            },
        ],
    }
                       send_message(new_embed)
                    input(Style.BRIGHT + Fore.MAGENTA + '~~')
                    sys.exit(0)
Sprint("MATERIALS","MATERIALS FINISHED PRESS ENTER TO EXIT",Fore.YELLOW)
input(Style.BRIGHT + Fore.MAGENTA + '~~')
sys.exit(0)
