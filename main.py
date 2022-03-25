import os
os.system("pip install amino.fix==2.2.7")
import aminofix
import re
from colorama import init, Fore, Back, Style
import pyfiglet
import time

#from keep_alive import keep_alive
#keep_alive()

print(Fore.RED + Style.BRIGHT)
print(pyfiglet.figlet_format("Transfert", font="standard"))

W=aminofix.Client("42FA1B03F7C14027E49A6230CA7E7E730482CDD157BC4B4CDD430870B1982A52EE913D003F5075C394")
emails = open("/sdcard/emails.txt", "r")
print(Fore.YELLOW + Style.BRIGHT)
link = W.get_from_code("http://aminoapps.com/p/5snf7h")
blog=link.objectId
comId=link.path[1:link.path.index('/')]

password = ("020862waza")
for line in emails:
 email = line.strip()

 try:
    W.login(email=email, password=password)
    SUB=aminofix.SubClient(comId,profile=W.profile)
 except aminofix.lib.util.exceptions. VerificationRequired as e:
               print(f"VerificationRequired for {email}")
               url = re.search("(?P<url>https?://[^\s'\"]+)", str(e)).group("url")                                                                             
 try:
       W.join_community(comId)
 except:
               print(comId,"no way")
               
               time.sleep(25)

 try:
  acc=W.get_wallet_info().totalCoins
  print(f"\n \033[0;36;40m Transferred {acc} coins from {email} ")
  if acc>500 and acc!=0:
   N=int(acc/500) 
   for _ in range(N):
    SUB.send_coins(500,blog)
    print("500 coins sent")
    print(f"Total coins till now : {W.get_wallet_info().totalCoins}") 
    print("_______________________")
 except:
    print(f"try again.{ W.get_wallet_info().totalCoins} ")

 try:
          totals=W.get_wallet_info().totalCoins      
          if totals!=0:
           print("......")
          if totals!=0 and totals<500 or totals==500:
                   SUB.send_coins(totals,blog)
                   print(f"Total coins till now : {W.get_wallet_info().totalCoins}") 
                   print("_______________________") 
 except:
    print(f"try again.{W.get_wallet_info().totalCoins}.")
