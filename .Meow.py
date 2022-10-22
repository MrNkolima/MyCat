#!/usr/bin/python3
# Tool: MyCat
# Version: 1.0.0.

import sys, os
from time import sleep
from base.system import *

class inst:
  def chk_sys(self):
    if "linux" in sys.platform or "linux2" in sys.platform:
      self.chk_inst()
    elif "darwin" in sys.platform:
      print("Meoww, MyCat is not available for mac rusers !!")
      sys.exit()
    elif "win" in sys.platform:
      print("Meoww, MyCat is not available for windows users !!")
      sys.exit()
    else:
      print("MyCat is not available for \'%s\' right now !!!" %sys.platform)
      sys.exit()

  def chk_inst(self):
    if os.path.exists(bpath+"meow") and os.path.exists(spath+"MyCat"):
    pass
    else:
      self.inst()

  def inst(self):
    if system=="ubuntu":
      noti()
      opt=raw_input("\033[01;33m Do you want to install MyCat? [\033[01;32mY/n\033[01;33m] >> \033[00m")
      if opt=="Y" or opt=="y":
        os.system("sh install")
      elif opt=="N" or opt=="n":
        sys.exit()
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+opt+"\'")
        sleep(1)
        self.inst()
    else:
      noti()
      opt=raw_input("\033[01;33m Do you want to install MyCat [\033[01;32mY/n\033[01;33m] >> \033[00m")
      if opt=="Y" or opt=="y":
        os.system("sh install")
      elif opt=="N" or opt=="n":
        sys.exit()
      else:
        print("\n \033[01;31m\007Command not found :\033[01;32m \'"+opt+"\'")
        sleep(1)
        self.inst()

def MyCat():
  try:
    inst().chk_sys()
  except KeyboardInterrupt:
    exit()
MyCat()
