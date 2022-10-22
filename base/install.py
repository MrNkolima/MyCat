# Tool: MyCat
# Version: 1.0.0.
#Designer & Artist: Isack Philiph

import sys
import os
from time import sleep
from system import *

class installm:
  def store():
    while True:
      if system=="ubuntu":
         os.system("Meowww::: For Ubuntu users, This Feature will come soon!!")
      else:
         #The tools
         os.system("clear")
         sleep(0.3)
         os.system("echo '          MYCAT Version: 1.0.0.'")
         os.system("echo '\n\n\n  \033[1;31mIt is recommended to read info first!! \n       Type:: \033[01;33m>>>info [Tool number]\033[00m\n\n \033[01;34m    1->Lazymux \n     2->Zphisher \n     3->MBomb \n     4->Infoga Collect Mail Info \n     5->BlackEye \n     6->Sqlisscan \n     7->Autopixie wps \n     8->Seeker \n     9->Whatsapp with QRL Hacking \n     10->T-Phish\n     11->200+ Tools \033[00m'")
         try:
           choice=input("\n\n\033[01;33m          >>>")
           os.system("echo '\033[00m'")
           if choice=="1":
             os.system("apt install git && apt install python2 && git clone https://github.com/Gameye98/Lazymux && cd Lazymux && chmod +X * && python2 lazymux.py")
             sys.exit()
           elif choice=="2":
             os.system("apt install git && git clone git://github.com/htr-tech/zphisher.git && cd zphisher && bash zphisher.sh")
             sys.exit()
           elif choice=="3":
             os.system("pkg install python2 -y && pkg install git -y && git clone https://github.com/palahsu/MBomb && cd MBomb && python2 MBomb.py")
             sys.exit()
           elif choice=="4":
             os.system("apt install python2 && git clone https://github.com/m4ll0k/Infoga && cd Infoga && chmod +x * && pip2 install requests && python2 infoga.py -t gmail.com -s all")
             sys.exit()
           elif choice=="5":
             os.system("apt install curl && git clone https://github.com/thelinuxchoice/blackeye && cd blackeye && chmod +x * && bash blackeye.sh")
             sys.exit()
           elif choice=="6":
             os.system("apt install curl && git clone https://github.com/thelinuxchoice/sqliscan && cd sqliscan && chmod +x * && ./sqliscan.sh")
             sys.exit()
           elif choice=="7":
             os.system("apt install python2 && apt install python && pip2 install requests && git clone https://github.com/nxxxu/AutoPixieWps && cd AutoPixieWps && chmod +x * && python2 autopixie.py")
             sys.exit()
           elif choice=="8":
             os.system("pkg install git curl php python && git clone https://github.com/thewhiteh4t/seeker && cd seeker && bash install.sh &&pkg install open ssl && pkg install openssh && pkg install python2 && python3 seeker.py -t manual")
             sys.exit()
           elif choice=="9":
             os.system("pkg install wget && gem install lolcat && pkg install php && pkg install toilet && git clone https://github.com/sparkz-technology/Target.git && cd Target && chmod +x Target.sh && bash Target.sh")
             sys.exit()
           elif choice=="10":
             os.system("termux-setup-storage && pkg install git && apt install php && git clone https://github.com/Stephin-Franklin/T-Phish && unzip T-Phish.zip && cd T-Phish && chmod 777 start.sh && ./start.sh && ./phish.sh")
             sys.exit()
           elif choice=="11":
             os.system("apt install php && apt install curl && apt install ruby && apt install figlet && apt install python2 && gem install lolcat && git clone https://github.com/TUANB4DUT/TOOLSINSTALLERv3 && cd TOOLSINSTALLERv3 && chmod +x TUANB4DUT.sh && sh TUANB4DUT.sh")
             sys.exit()
           elif choice=="info 1":
              print("Lazymux is python based tool in this tool and collection of tools for termux users.\nYou guys can install some tools by typing number in easiest way")
              sys.exit()
           elif choice=="info 2":
              print("A beginners friendly, Automated ph!$hing tool with 30+ templates.")
              sys.exit()
           elif choice=="info 3":
              print("MBomb means Mail-Bomb and it s works for Sending Unlimited Mail. You can send unlimited message Gmail to Gmail.")
              sys.exit()
           elif choice=="info 4":
              print("Infoga is a tool gathering email accounts informations (ip,hostname,country,...) from different public source (search engines, pgp key servers and shodan) and check if emails was leaked using h@¢ked-emails API.  \n Is a really simple tool, but very effective for the early stages of a penetration test or just to know the visibility of your company in the Internet.")
              sys.exit()
           elif choice=="info 5":
              print("The most complete Ph!$h!ng Tool, with 32 templates +1 customizable\nNow select your option it will generate an url for P!$h!ng..")
              sys.exit()
           elif choice=="info 6":
              print("Now enter your dorks it will start collecting all vulnerable sites related to your dork and also these sites saved in saved.txt file.")
              sys.exit()
           elif choice=="info 7":
              print("Now select any option it will guide you..")
              sys.exit()
           elif choice=="info 8":
              print("By the use of following commands we can creat a strong V!®us in Termux.")
              sys.exit()
           elif choice=="info 9":
              print("By the using of following commands we can find our lose device location.")
              sys.exit()
           elif choice=="info 10":
              print("T-Phish is a great tool for Ph!$hing attack for mobile devices. It is a modified tool to provide better experience to user.TPHISH provide Ph!$hing links of Faceb00k, inst@gram, What$App, Paytm, Netflix and like all major Social media platform. It uses PHP and NGROK server to generate link.\nTurn ON your Mobile Hotspot here.Now send the Generated link to your target.")
              sys.exit()
           elif choice=="info 11":
              print("With the following commands we can install 200+ tools in Termux.")
              sys.exit()

           elif choice=="exit":
             sys.exit()
           else:
             os.system("echo '\033[01;31mMeoww: incorrect choice\033[00m'")
             sleep(1.2)
         except KeyboardInterrupt:
           print("    \033[0;31m Meowww:: Exiting...\n\n \033[00m")
           sleep(1.5) 
           sys.exit()

                     
#Looping
def run():
  installm.store()
run()