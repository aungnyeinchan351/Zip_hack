import zipfile
import os
import pyfiglet
from tqdm import tqdm
os.system("clear")
print(pyfiglet.figlet_format("Dust-Zip",font="slant"))
zip_file = input("Enter Zip File: ")
userinput = input("Do you wnat tlo use built-in-wordlist.[y/n]:")
if userinput == "y":
    wordlist = "rockyou.txt"
else:
    wordlist = input("Enter Wordlist: ")
zip_file = zipfile.ZipFile(zip_file)
nwords = len(list(open(wordlist,"rb")))
print("Number of passwords to test: ",nwords)
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=nwords, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit()
print("[!] Password not found, try other wordlist.")