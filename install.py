import requests
import os
os.system("pip3 install pyfiglet")
os.system("pip3 install tqdm")
url = 'https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt'
r = requests.get(url, allow_redirects=True)
open('rockyou.txt','wb').write(r.content)
print("Requirements are successfully installed.")
userinput = input("Do you wnat to run zip_hack.py.[y/n]: ")
if userinput == "y":
    os.system("python3 zip_hack.py")
