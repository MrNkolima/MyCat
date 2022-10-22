#!/usr/bin/python3
#Tool: MyCat
#Version: 1.0.0.
#Artist & design: Isack Philiph

import sys
import os
from time import sleep
from base.system import *

if os.getuid() == 0 or system=="termux":
  pass
else:
    print("\nerror: Please, Run This programm as Root!\n")
    sys.exit()
if len(sys.argv)>1:
  pass
else:
  print ("Meowwwww::: I can\'t understand!!")
  sleep(0.1)
  print ("Get Help ::: meow h OR, meow help OR, meow --help")
  sys.exit()

if sys.argv[1]=="rm" or sys.argv[1]=="kill":
  if len(sys.argv)==3:
    if sys.argv[2]=="cat" or sys.argv[2]=="meow" or sys.srgv[2]=="-T" or sys.argv[2]=="-t":
      if system=="ubuntu":
        os.system("sudo python3 base/killcat.py")
      else:
        os.system("python3 base/killcat.py")
    else:
      print ("Meowwwww::: I can\'t understand!!")
      
  else:
    print ("Meowwwww::: I can\'t understand!!")
    
elif sys.argv[1]=="install":
  if system=="ubuntu":
    os.system("python3 base/install.py")
  else:
    os.system("python3 base/install.py")

elif sys.argv[1]=="view" or sys.argv[1]=="v" or sys.argv[1]=="-v":
  if len(sys.argv)==3:
    if sys.argv[2]=="machine":
       os.system("python3 base/machineinfo.py")
       sys.exit()
    elif sys.argv[2]=="ip":
       os.system("echo '\033[0;34mIP address: \033[00m' && hostname -i")
       print("")
       sys.exit()
    elif sys.argv[2]=="storage":
       os.system("df -h")
       print("")
       sys.exit()
    elif sys.argv[2]=="list":
       os.system("ls | xargs wc")
       print("")
       sys.exit()
    elif sys.argv[2]=="cpu":
       os.system("cat /proc/cpuinfo")
       print("")
       sys.exit()
    elif sys.argv[2]=="usage":
       os.system("echo '\033[0;34mThis directory takes about::\033[00m' && du -sh")
       print("")
       sys.exit()
    else:
     os.system("echo '\033[0;34m   Meowww::\033[00m\v Try meow --help for more information'")
     print("")
     print("")
     sys.exit()
  else:
    os.system("echo '          \033[01;31m  Meowww: use like this\t meow view [argument] \tsee meow --help\033[00m'") 
    print("")
    print("")
    sys.exit()

elif sys.argv[1]=="update":
  if system=="ubuntu":
    os.system("python3 base/buynewcat.py")
  else:
    os.system("python3 base/buynewcat.py")

elif sys.argv[1]=="version" or sys.argv[1]=="-version":
  if system=="ubuntu":
    os.system("echo 1.0.0.")
    print("")
  else:
    os.system("echo '\033[0;34mMyCat Version::\033[00m \n1.0.0.'")
    print("")


elif sys.argv[1]=="--help" or sys.argv[1]=="-help" or sys.argv[1]=="help" or sys.argv[1]=="h":
  print("")
  print("            MyCat v1.0.0.")
  print ("Usage: \033[0;34mmeow [command]... [arguments]...\033[00m")
  print("")
  print("   \033[0;34mmeow install\033[00m       | Get to install tools (11 tools available now)")
  print("   \033[0;34mmeow version\033[00m       | To check my cat version")
  print("\n          view or v or -v \n")
  print("   \033[0;34mmeow v machine\033[00m   | See the computer informations(Everything!!)")
  print("   \033[0;34mmeow -v storage\033[00m  |  See the system storage information")
  print("   \033[0;34mmeow view cpu\033[00m    |  Show system CPU information")
  print ("")
  print("   \033[0;34mmeow update\033[00m      |  Update MyCat")
  print("   \033[0;34mmeow kill cat\033[00m    |  Uninstall MyCat")
  print("   \033[0;34mmeow help\033[00m        |  Display this help and exit")
  print (" \n")
  print("     Developer: \033[0;34mIsack Philiph\033[00m")
  print ("")

else:
  print ("\033[0;31m   Meowwwww\033[00m::: I can\'t understand!!")
  print("")
  sys.exit()
