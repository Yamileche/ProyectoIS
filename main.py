#!/usr/bin/python3
import click
from Encrypt import *
from random import choice
from Entero import *
import sys
import os
from sympy.ntheory import factorint


global path, Bpath, exit
exit = False
@click.group()
def main():
    """Encrypting program"""
def getDefaultPath():
    global path, Bpath, exit
    Bpath = False
    if exit: sys.exit()
    while True:
        path = input("Enter default path: ")
        path = path.strip()
        if os.path.isdir(path) or path == "":
            if path != "": Bpath = True
            break
        else:
            print("Path does not exist, try again")
def getTextFromFile() -> str:
    global path, Bpath, exit
    exit = False
    text = ""
    if exit: sys.exit()
    while True:
        try:
            print("Enter data by console 'c' or by txt 't'? (press 'e' to exit)")
            readMode = input().strip()
            if readMode.lower() == 'e': 
                exit = True
                break
            if readMode.lower() == 'c':
                text = input("Enter text:\n\n")
            else:
                if Bpath:
                    fileName = input("Enter file name: ").strip()
                    pathAux = path + "/" + fileName + ".txt"
                else:
                    while True:    
                        pathAux = input("Enter path: ")
                        if os.path.isfile(pathAux): break
                        else: print("File does not exist")        
                inp = open(pathAux, "r")
                text = inp.read()
                inp.close()
            break
        except:
            print("Error reading file. Try again")
        if exit: sys.exit()
    print("Text reading successful")
    return text
def giveText(text = ""):
    global path, Bpath, exit
    if exit: sys.exit()
    print("Get data by console 'c' or by txt 't'?")
    election = input().strip()
    if election.lower() == 'c':
        print(text)
    else:
        while True:
            if Bpath:
                pathAux = path 
            else:
                while True:
                    pathAux = input("Enter path: ")
                    if os.path.isdir(pathAux): break
                    else: print("Path does not exist, try again")
            while True:
                name = input("Enter file's name: ")
                if os.path.isfile(pathAux + "/" + name + ".txt"):
                    election = input("File does exist, do you want to conitue? (Y/N): ").strip().lower()
                    if election == "y":
                        pathAux = pathAux + "/" + name + ".txt"
                        break
                else: 
                    pathAux = pathAux + "/" + name + ".txt"
                    break
            try:
                output = open(pathAux, "w")
                output.write(text)
                output.close()
                break
            except:
                print("Error writing in file " + pathAux)
def textToKeys(text = "")->list:
    global exit
    if exit: sys.exit()
    text = text.split(" ")
    key = list()
    for i in text:
        if i.isnumeric():
            key.append(int(i))
    return key
def readKeys()-> list:
    global exit
    if exit: sys.exit()
    keys = list()
    while True:
        keys = getTextFromFile()
        keys = textToKeys(keys)
        if len(keys) == 0:
            if exit: break
            print("Error reading keys, try again")
        else: 
            print("Keys reading successful")
            break
    if exit: sys.exit()
    return keys
def getKeysAsText() -> str:
    auxKeys = readKeys()
    keys = ""
    for k in auxKeys:
        keys = keys + str(k) + "  "
    return keys
def giveKeys(keys = []):
    global path, Bpath, exit
    if exit: sys.exit()
    text = ""
    for i in keys:
        text = text + str(i) + " "
    giveText(text)
def randomPrime() -> int:
    return Entero.ranPrime()
def randomKeys() -> list:
    while True:
        choice = input("Random moddule? (Y/N)\n").strip().lower()
        if choice == "y":
            p = randomPrime()
            break
        else:
            p = input("Enter module: ").strip()
            if p.isnumeric() and int(p)>1:
                p = int(p)
                break
    while True:
        n = input("Enter number of keys: ").strip()
        if n.isnumeric() and int(n) > 0:
            n = int(n)
            break
        else: print("Value error, try again")
    keys = list()
    
    pFactors = list(factorint(p).keys())
    isPrime = False
    if len(pFactors) == 1:
        isPrime = True
    print("Wait, calculating keys...")
    for i in range(n):
        while True:
            again = False

            aux = random.choice(range(p))
            fac = factorint(aux).keys()
            if not isPrime:
                for i in pFactors:
                    if i in fac:
                        again = True
            if not again:
                keys.append(aux)
                break
    return keys



@main.command()
@click.option('--cesaro',is_flag =True,  help = 'Cesaro method')
@click.option('--vigenere',is_flag =True,  help = 'Vigenere method')
@click.option('--vernam',is_flag =True,  help = 'Vernam method')
def encrypt(cesaro, vigenere, vernam):
    """Encrypt mode"""
    getDefaultPath()
    if exit: sys.exit()
    if cesaro:
        print("Cesaro method\n")
        while True:
            try: 
                a = int(input("Enter a: "))
                b = int(input("Enter b: "))
                p = int(input("Enter module: "))
                break
            except:
                print("Invalid values. Try again")
        text = getTextFromFile()
        out = Encryptor(text, mod = p).cesaro(a = a, b = b)
        giveText(text=out)
    elif vigenere:
        print("Vigenere method\n")
        print("Values 'a' will be read\n")
        a = readKeys()
        print("\n\nValues 'b' will be read\n")
        b = readKeys()
        while True:
            p = input("Enter module: ").strip()
            if p.isnumeric() and int(p)>1:
                p = int(p)
                break
            else:
                print("Invalid number, try again")
        print("\n\nText to encrypt")
        text = getTextFromFile()

        out = Encryptor(text, mod = p).vigenere(a = a, b = b)
        giveText(text=out)
    elif vernam:
        print("Vigenere method\n")
        while True:
            p = input("Enter module: ").strip()
            if p.isnumeric() and int(p) > 1:
                p = int(p)
                break
            else:
                print("Invalid value, try again\n")
        print("\n\nText to encrypt")
        text = getTextFromFile()
        out = Encryptor(text, mod = p).Vernam()
        print("\n\nGetting encrypted text")
        giveText(out[0])
        print("\n\nGetting 'a' keys")
        giveKeys(out[1])
        print("\n\nGetting 'b' keys")
        giveKeys(out[2])

@main.command()
@click.option('--cesaro',is_flag =True,  help = 'Cesaro method')
@click.option('--vigenere',is_flag =True,  help = 'Vigenere method')
@click.option('--vernam',is_flag =True,  help = 'Vernam method')
def decrypt(cesaro, vigenere, vernam):
    """Decrypt mode"""
    getDefaultPath()
    if exit: sys.exit()
    if cesaro:
        print("Cesaro method\n")
        while True:
            try: 
                a = int(input("Enter a: "))
                b = int(input("Enter b: "))
                p = int(input("Enter module: "))
                break
            except:
                print("Invalid values. Try again")
        print("Text's keys will be read")
        keys = getKeysAsText()
        print("\nDecrypting...\n\n")
        text = Encryptor(to_decrypt=keys, mod=p).inv_cesaro(a=a, b=b)
        giveText(text=text)
    elif vigenere:
        print("Vigenere method\n")
        print("Values 'a' will be read\n")
        a = readKeys()
        print("\n\nValues 'b' will be read\n")
        b = readKeys()
        while True:
            p = input("Enter module: ").strip()
            if p.isnumeric() and int(p)>1:
                p = int(p)
                break
            else:
                print("Invalid number, try again")
        print("Text's keys will be read")
        print("\nDecrypting...\n\n")
        text = Encryptor(to_decrypt=keys, mod=p).vigenere(a=a, b=b)
        giveText(text=text)
        
    elif vernam:
        print("Vermam method\n")
        while True:
            p = input("Enter module: ").strip()
            if p.isnumeric() and int(p)>1:
                p = int(p)
                break
            else:
                print("Invalid number, try again")
        print("Values 'a' will be read")
        a = readKeys()
        print("\n\nValues 'b' will be read")
        b = readKeys()
        print("\n\nEncrypted text will be read")
        keys = getKeysAsText()
        text = Encryptor(to_decrypt=keys, mod=p).inv_Vernam(a=a, b=b)
        print("\nDecrypted text")
        giveText(text=text)

@main.command()
def ranK():
    "Random keys"
    getDefaultPath()
    giveKeys(randomKeys())

@main.command()
def ranP():
    "Random prime"
    print(randomPrime())
    


if __name__ == "__main__": 
    main()