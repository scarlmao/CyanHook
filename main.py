import requests
import random
import time
import json
import os
from pystyle import Colors, Colorate
import threading



menu_text = r"""     
                                     

                                         
                                         _____                   _   _             _    
                                        /  __ \                 | | | |           | |   
                                        | /  \/_   _  __ _ _ __ | |_| | ___   ___ | | __
                                        | |   | | | |/ _` | '_ \|  _  |/ _ \ / _ \| |/ /
                                        | \__/\ |_| | (_| | | | | | | | (_) | (_) |   < 
                                         \____/\__, |\__,_|_| |_\_| |_/\___/ \___/|_|\_\
                                                __/ |                                   
                                               |___/                                    
                                        
                                     ╔══════════════════════════════════════════════════════╗
                                     ║                                                      ║
                                     ║      [1] Spam      [2] Info      [3] Delete          ║
                                     ║                                                      ║
                                     ╚══════════════════════════════════════════════════════╝ 
                        
"""

menu_text2 = r"""     
                                     

                                         
                                         _____                   _   _             _    
                                        /  __ \                 | | | |           | |   
                                        | /  \/_   _  __ _ _ __ | |_| | ___   ___ | | __
                                        | |   | | | |/ _` | '_ \|  _  |/ _ \ / _ \| |/ /
                                        | \__/\ |_| | (_| | | | | | | | (_) | (_) |   < 
                                         \____/\__, |\__,_|_| |_\_| |_/\___/ \___/|_|\_\
                                                __/ |                                   
                                               |___/                                    
                                        
                                     ╔══════════════════════════════════════════════════════╗
                                     ║                                                      ║
                                     ║               Enter Your Webhook Url                 ║
                                     ║                                                      ║
                                     ╚══════════════════════════════════════════════════════╝ 
                        
"""
def main():
 os.system('cls')
 print(Colorate.Horizontal(Colors.cyan_to_blue, menu_text,1))
 option = input(Colorate.Horizontal(Colors.blue_to_white, '                                     [@] > ', 1))

 def spam(webhook,username,avatar,msg):
    while True:
     r = requests.post(webhook, json={"username": username, "avatar_url": avatar, "content": msg})
     current_time = time.strftime("%H.%M.%S")
     print(Colorate.Horizontal(Colors.green_to_white, f"                                     [@] > [{current_time}] | SUCCES",1))


 if option == "1":
    os.system('cls')
    print(Colorate.Horizontal(Colors.cyan_to_blue, menu_text2,1))
    webhook = input(Colorate.Horizontal(Colors.blue_to_white, '                                     [@] > ', 1))
    os.system('cls')
    username = input(Colorate.Horizontal(Colors.blue_to_white, '                                     [@] Username > ', 1))
    os.system('cls')
    avatar = input(Colorate.Horizontal(Colors.blue_to_white, '                                     [@] Avatar Url > ', 1))
    os.system('cls')
    msg = input(Colorate.Horizontal(Colors.blue_to_white, '                                     [@] Msg To Spam > ', 1))
    os.system('cls')
    threads = input(Colorate.Horizontal(Colors.blue_to_white, '                                     [@] Amt Of Threads > ', 1))
    for thread in threads:
     threading.Thread(target=spam, args=(webhook, username, avatar, msg)).start()


 if option == "2":
    os.system('cls')
    print(Colorate.Horizontal(Colors.cyan_to_blue, menu_text2,1))
    webhook = input(Colorate.Horizontal(Colors.blue_to_white, '                                     [@] > ', 1))
    r = requests.get(webhook)
    print(r.json())
    pause = input("")
    main()

 if option == "3":
   os.system('cls')
   print(Colorate.Horizontal(Colors.cyan_to_blue, menu_text2,1))
   webhook = input(Colorate.Horizontal(Colors.blue_to_white, '                                     [@] > ', 1))
   r = requests.delete(webhook)
   current_time = time.strftime("%H.%M.%S")
   print(Colorate.Horizontal(Colors.red_to_white, f"                                     [@] > [{current_time}] | DELETED",1))
   pause = input("")
   main()
   

main()



