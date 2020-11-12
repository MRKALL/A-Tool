import os
os.system("clear")
print("--------------------------------------------------------------------------")
print("hello")
print("--------------------------------------------------------------------")
print("to A-Tool")
print("--------------------------------------------------------------")
print("---------------------------------------------------------")
print()
print()
print("1- update termux    2-upgrade termux""\n""3- nmap  4- hydra  5- python""\n""6- Tool-X  5- python2  6- python3""\n""7- tor  8- PLANETWORK-DDOS""\n""9- MRKING")
print("10- hammer  11-v7x tool 12- sqlmap")
n = input("inter numper : ")
if n == "1" :
    os.system("pkg update")
if n == "2" :
    os.system("pkg upgrade")
if n == "3" :
    os.system("pkg install nmap")
if n == "4" :
    os.system("pkg install hydra")
if n == "5" :
    os.system("pkg install python")
if n == "6" :
    os.system("pkg install git")
    os.system("git clone https://github.com/rajkumardusad/Tool-X")
    os.system("cd Tool-X")
    os.system("chmod +x install")
    os.system("sh install")
    os.system("Tool-X")
if n == "7" :
    os.system("pkg install tor")
if n == "8" :
    os.system("pkg install git")
    os.system("git clone https://github.com/Hydra7/Planetwork-DDOS")
if n == "9" :
    os.system("pkg install git")
    os.system("git clone https://github.com/king-hacking/MRKING")
    os.system("cd MRKING")
    os.system("sh install.sh")
    os.system("sh MRKING.sh")
if n == "10" :
    os.system("pkg install git")
    os.system("git clone https://github.com/cyweb/hammer")
if n == "11" :
    os.system("pkg install git")
    os.system("git clone https://github.com/Vairous7x/V7x-Tool")
if n == "12" :
    os.system("pkg install git")
    os.system("git clone https://github.com/sqlmapproject/sqlmap")
        
