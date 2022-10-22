# Tool: MyCat
# Version: 1.0.0.
#Artist & design: Isack Philiph

import sys
import os
from time import sleep
from system import *

def run():
  os.system("echo '\033[0;34mOperating System:: \033[00m' && uname -o ")
  os.system("echo '\033[0;34mMachine Hardware name:: \033[00m' && uname -m")
  os.system("echo '\033[0;34mHardware Platform:: \033[00m' && uname -i")
  os.system("echo '\033[0;34mProcessor:: \033[00m' && uname -p")
  os.system("echo '\033[0;34mNode-name:: \033[00m' && uname -n")
  print("")
  sys.exit()

run()