#Tool: MyCat
#Version: 1.0.0.

import sys
import os
from time import sleep
from system import *

class Un(object):
  def Uni(self):
    while True:
      ask = input("\n\n\033[1;33m Do you want to kill this cat ?[\033[01;32mY/n\033[01;33m] >> \033[00m")
      if ask == "n" or ask == "N":
        break
      elif ask == "Y" or ask == "y":
        if system=="ubuntu":
          os.system("cd "+spath+" && sudo rm -rf MyCat")
          os.system("sudo rm -rf "+bpath+"meow")
          #The added files will removed here
         # os.system("cd "+spath+" && sudo rm -rf ")
        else:
          os.system("rm -rf "+bpath+"meow")
          os.system("cd "+spath+" && rm -rf MyCat")
          #The added files will be deleted here
          #os.system("cd "+spath+" && rm -rf ")
        exit()
      else:
        print("\n \033[01;31m\007Meowww:: Choices are Y or N :\033[01;32m \'"+ask+"\'")
        sleep(1)
#Loop
Un().Uni()