# Tool: MyCat
# Version: 1.0.0.

import sys
import os
from time import sleep
from system import *

class update(object):
  def chk_upd(self):
    while True:
      askv = input("\n\033[1;33m Do you want to get updated Cat ?[\033[01;32mY/n\033[01;33m] >> \033[00m")
      if askv == "n" or askv == "N":
        break
      elif askv == "Y" or askv == "y":
        os.system("clear")
        print("\n\033[01;32mUpdating a Cat..............\033[01;36m")
        if os.path.exists(bpath+"git"):
          sleep(1.3)
          os.system("clear")
          print("Updating...")
        else:
          os.system(pac+" update")
          os.system(pac+" install git -y")
        if system=="ubuntu":
          os.system("cd "+home+" && sudo git clone https://github.com/MrNkolima/MyCat.git && cd MyCat && chmod +x install && sh install")
        else:
          os.system("cd "+home+" && git clone https://github.com/MrNkolima/MyCat.git && cd MyCat && chmod +x install && sh install")
        if os.path.exists(home+"MyCat"):
          os.system("cd "+home+"MyCat && sh install") 
          print("\033[01;32mThe cat is updated!, Test him!!\033[00m")
          break
        else:
        
          print("\n\n\033[01;37m    [+] \033[01;31mAn updated Cat be be installed!!\033[00m")
          print("\033[01;37m    [+] \033[01;31mYou are \033[01;33mOFFLINE \033[01;31m!!!\033[00m")
          print("\033[01;37m    [+] \033[01;31mPlease check your \033[01;33mnetwork \033[01;31mconnection !!!\033[00m")
          print("\n\n")
          sleep(4)
          break
      else:
        print("\n \033[01;31m\007Meowwwwwwww::: I can\'t understand:: \033[01;32m \'"+askv+"\'")
        sleep(1)

def upd():
  update().chk_upd()
upd()
