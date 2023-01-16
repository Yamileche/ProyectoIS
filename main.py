#!/usr/bin/python3
import click
from Encrypt import *
from random import choice
from Entero import *

@click.group()
def main():
    """Encrypting program"""

def filterKeys(keysAux = "") ->list:
    """ Put on a list keys from text
    Args:
        keysAux (str, optional): Text of keys. Defaults to "".
    Returns:
        list: list of keys
    """
    keys = list()
    for letter in keysAux:
        if letter.isnumeric():
            keys.append(letter)
    return keys
def filterKeysInt(keysAux = "") ->list:
    """ Put on a list keys from text
    Args:
        keysAux (str, optional): Text of keys. Defaults to "".
    Returns:
        list: list of keys
    """
    keys = list()
    for letter in keysAux:
        if letter.isnumeric():
            keys.append(int(letter))
    return keys
def getKeysFromFile(path = "") -> list: 
    """ Get and separate the keys
    Returns:
        list(str): list of keys
    """
    inp = open(path, "r")
    keysAux = inp.read().replace("\n", " ").replace("\\", " ").split(" ")
    inp.close()

    return filterKeys(keysAux=keysAux)
def getKeysFromFileInt(path = "") -> list: 
    """ Get and separate the keys
    Returns:
        list(int): list of keys
    """
    inp = open(path, "r")
    keysAux = inp.read().split(" ").replace("\n", " ").replace("\\", " ")
    inp.close()

    return filterKeysInt(keysAux=keysAux)
def getTextFromTxtFile(path = "") -> str:
    """ Get text from certain txt file
    Args:
        path (str): txt's path Defaults to "".
    Returns:
        str: Text
    """
    if path == "":
        raise Exception("Path is empty") 
    try:
        inp = open(path, "r")
        try:
            text = inp.read()
        except:
            print("Error reading file at getTextFromTxtFile")
            inp.close()
    except:
        print("Error opening file at getTextFromTxtFile")

    return text
def writeTextToTxt(path = "", toWrite = "", nameFile = "output"):
    """ Write text in a Txt

    Args:
        path (str): Container file's path  . Defaults to "".
        toWrite (str): Text to write. Defaults to "".
        nameFile (str): Txt's name to create. Defaults to "output".
    """
    
    if nameFile.strip() == "": nameFile = "output"
    path = path + "/" +nameFile+".txt"
    output = open(path, "w")
    output.write(toWrite)
    output.close()


    

@main.command()
@click.option('--cesaro',is_flag =True,  help = 'Cesaro method')
@click.option('--vigenere',is_flag =True,  help = 'Vigenere method')
@click.option('--vernam',is_flag =True,  help = 'Vernam method')
def encrypt(cesaro, vigenere, vernam):
    """Encrypt mode"""
    path = ""
    if cesaro:
        print("Cesaro method")
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        p = int(input("Enter module: "))
        print("Enter text by console 'c' or by txt 't'?")
        ele = input().strip()
        if ele.lower() == 'c':
            text = input("Enter text:\n\n")
        else:
            path = input("Enter path: ")
            inp = open(path, "r")
            text = inp.read()
            inp.close()

        out = Encryptor(text, mod = p).cesaro(a = a, b = b)

        
        print("Obtain result by console 'c' or by txt?")
        election = input().strip()

        if election.lower() == 'c':
            print(out)
        else:
            path = input("Enter path: ")
            path +="/output.txt"
            output = open(path, "w")
            output.write(out)
            output.close()
    elif vigenere:
        print("Vigenere method")
        p = int(input("Enter module: "))
        print("\n\nEnter elements by console (c) or by txt (t)?")
        enter = input()
        enter.strip().lower()
        if enter.strip().lower() == "c":
            print("Enter 'a' values separated by spaces:")
            aString = input()
            a = list()
            for number in aString.split(" "):
                if number.isnumeric:
                    a.append(int(number))
            if len(a) == 0:
                print("Failure capturing 'a' values")
            print("Enter 'b' values separated by spaces:")
            bString = input()
            b = list()
            for number in bString.split(" "):
                if number.isnumeric:
                    b.append(int(number))
            if len(b) == 0:
                print("Failure capturing 'b' values")
        else:
            print("Enter path for 'a' values (must be separated by spaces)")
            path = input().strip()
            #Aquí debe ir un try catch por si no abre el archivo
            aKeys = open(path, "r")
            aString = aKeys.read().replace("\n", " ").replace("\\", " ")
            a = list()
            for number in aString.split(" "):
                if number.isnumeric():
                    a.append(int(number))
            if len(a) == 0:
                print("Failure capturing 'a' values")
            aKeys.close()

            print("\n\nEnter path for 'b' values (must be separated by spaces)")
            path = input().strip()
            #Aquí debe ir un try catch por si no abre el archivo
            bKeys = open(path, "r")
            bString = bKeys.read().replace("\n", "").replace("\\", "")
            b = list()
            for number in bString.split(" "):
                if number.isnumeric():
                    b.append(int(number))
            if len(b) == 0:
                print("Failure capturing 'b' values")
            bKeys.close()

        print("Enter text by console (c) or by txt (t)?")
        ele = input().strip()
        if ele.lower() == 'c':
            text = input("Enter text:\n\n")
        else:
            #Un Try catch por si no abre el archivo
            path = input("Enter path: ")
            inp = open(path, "r")
            text = inp.read()
            inp.close()

        out = Encryptor(text, mod = p).vigenere(a = a, b = b)

        print("Obtain result by console 'c' or by txt 't'?")
        election = input().strip()

        if election.lower() == 'c':
            print(out)
        else:
            default = input("In default path /home/Documents?\n(Y/n)").strip().lower()
            if default == "y" or default == "yes" or default == "si" or default == "s":
                path = "/home/Documents"
            else:
                path = input("Enter path: ").strip()
            path +="/output.txt"
            output = open(path, "w")
            output.write(out)
            output.close() 
    elif vernam:
        p = int(input("Enter module: "))

        print("Enter text by console (c) or by txt (t)?")
        ele = input().strip()
        if ele.lower() == 'c':
            text = input("Enter text:\n\n")
        else:
            #Un Try catch por si no abre el archivo
            path = input("Enter path: ")
            inp = open(path, "r")
            text = inp.read()
            inp.close()

        out = Encryptor(text, mod = p).Vernam()

        print("Obtain result by console 'c' or by txt 't'?")

        election = input().strip()

        if election.lower() == 'c':
            print(out[0])
        else:
            default = input("In default path /home/Documents?\n(Y/n)").strip().lower()
            if default == "y" or default == "yes" or default == "si" or default == "s":
                path = "/home/Documents"
            else:
                path = input("Enter path: ").strip()
            path +="/output.txt"
            output = open(path, "w")
            output.write(out[0])
            output.close() 
    
        print("Obtain keys by console 'c' or by txt 't'?")


        election = input().strip()
        aKeysString = ""
        for i in out[1]:
            aKeysString = aKeysString +  str(i) + " "
        bKeysString = ""
        for i in out[2]:
            bKeysString = bKeysString + str(i) + " "

        if election.lower() == 'c':
            print("\nakeys\n",aKeysString)
            print("\n\nbkeys\n", bKeysString)
        else:
            default = input("In default path /home/Documents?\n(Y/n)").strip().lower()
            if default == "y" or default == "yes" or default == "si" or default == "s":
                path = "/home/Documents"
            else:
                path = input("Enter path: ").strip()

            at = open(path+"/aKeys.txt", "w")
            bt = open(path+"/bKeys.txt", "w")   
            at.write(aKeysString)
            bt.write[bKeysString]
            at.close()
            bt.close()
@main.command()
@click.option('--cesaro',is_flag =True,  help = 'Cesaro method')
@click.option('--vigenere',is_flag =True,  help = 'Vigenere method')
@click.option('--vernam',is_flag =True,  help = 'Vernam method')
def decrypt(cesaro, vigenere, vernam):
    """Decrypt mode"""
    path = ""
    if cesaro:
        print("Cesaro method")
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        p = int(input("Enter module: "))
 

        print("Enter keys by console 'c' or by txt 't'?")
        ele = input().strip()
        keys = []
        keysAux = ""

        if ele.lower() == 'c':
            keysAux  =input("Enter keys:\n\n")
            keys = filterKeys(keysAux)
        else:
            path = input("Enter key's path: ")
            keys = getKeysFromFile(path)

        if not keys: raise Exception("Error de lectura Cesaro keys en main.py en decrypt")

        print("\nDecrypting\n")

        out = Encryptor(to_decrypt=keys, mod = p).inv_cesaro(a = a, b = b)

        
        print("Obtain result by console 'c' or by txt?")
        writingChoice = input().strip()
 
        if writingChoice.lower() == 'c':
            print(out)
        else:
            path = input("Enter path: ")
            nameFile = input("Enter txt's name (default output): ")
            writeTextToTxt(path, out, nameFile)

    elif vigenere:

        print("Vigenere method")
        p = int(input("Enter module: "))

        print("\n\nEnter elements by console (c) or by txt (t)?")
        readingChoice = input()

        if readingChoice.strip().lower() == "c":

            print("Enter 'a' values separated by spaces:")
            aString = input()
            a = filterKeysInt(aString.split(" "))
            if len(a) == 0: raise Exception("Reading failure Vigenere a-keys at main.py at decrypt")

            print("Enter 'b' values separated by spaces:")
            bString = input()
            b = filterKeysInt(bString.split(" "))
            if len(b) == 0: raise Exception("Reading failure Vigenere b-keys at main.py at decrypt")

        else:

            print("Enter path for 'a' values (it must be separated by spaces)")
            path = input().strip()
            a = getKeysFromFileInt(path)
            if len(a) == 0: raise Exception("Reading failure Vigenere a-keys at main.py at decrypt")
            
            print("\n\nEnter path for 'b' values (it must be separated by spaces)")
            path = input().strip()
            b = getKeysFromFileInt(path)
            if len(b) == 0: raise Exception("Reading failure Vigenere a-keys at main.py at decrypt")

        print("Enter keys by console (c) or by txt (t)?")
        readingChoice = input()
        keys = []
        keysAux = ""

        if readingChoice.lower() == 'c':
            keysAux = input("Enter text:\n\n")
            keys = filterKeys(keysAux)
        else:
            path = input("Enter path: ")
            keys = getKeysFromFile(path)

        if not keys: raise Exception("Reading failure Vigenere keys at main.py at decrypt") 

        out = Encryptor(to_decrypt=keys, mod = p).vigenere(a = a, b = b)

        print("Obtain result by console 'c' or by txt 't'?")
        writingChoice = input().strip()
 
        if writingChoice.lower() == 'c':
            print(out)
        else:
            path = input("Enter path: ")
            nameFile = input("Enter txt's name (default 'output'): ")
            writeTextToTxt(path, out, nameFile)
    elif vernam:
        p = int(input("Enter module: "))

        print("Enter keys by console (c) or by txt (t)?")
        ele = input().strip()
        keys = []
        keysAux = ""
        a = []
        aAux = ""
        b = []
        bAux = ""
        if ele.lower() == 'c':
            keysAux = input("Enter text:\n\n")
            aAux = input("Enter a values:\n\n")
            bAux = input("Enter b values:\n\n")
        else:
            path = input("Enter key's path: ")
            inp = open(path, "r")
            keysAux = inp.read().split(" ")
            inp.close()

            path = input("Enter a's path: ")
            inp = open(path, "r")
            aAux = inp.read().split(" ")
            inp.close()

            path = input("Enter b's path: ")
            inp = open(path, "r")
            bAux = inp.read().split(" ")
            inp.close()

        for letter in keysAux:
            if letter.isnumeric():
                keys.append(letter)

        for letter in aAux:
            if letter.isnumeric():
                a.append(int(letter))
        for letter in bAux:
            if letter.isnumeric():
                b.append(int(letter))

    

        out = Encryptor(to_decrypt=keys, mod = p).inv_vernam(a = a, b = b)

        print("Obtain result by console 'c' or by txt 't'?")

        election = input().strip()

        if election.lower() == 'c':
            print(out)
        else:
            default = input("In default path /home/Documents?\n(Y/n)").strip().lower()
            if default == "y" or default == "yes" or default == "si" or default == "s":
                path = "/home/Documents"
            else:
                path = input("Enter path: ").strip()
            path +="/output.txt"
            output = open(path, "w")
            output.write(out)
            output.close() 

@main.command()
@click.option('--prime', is_flag = False, help = "Returns a random prime")
@click.option('--keys', default=0, help='Returns a random prime number and a certain number of keys smaller than the prime number')
def random (prime, keys):
    if prime:
        print(Entero.ranPrime())
        if keys:
            for i in range(keys):
                print(random.choice(range(2, keys)))
    else:
        if keys:
            prime = input("Prime: ").strip()
            while not prime.isnumeric():
                print("Try again\n") 
                prime = input("Prime: ").strip()
            key = ""
            for i in range(keys):
                auxkey = choice(range(2, int(prime)))
                while Entero.mcd(auxkey, int(prime))[0] != 1:
                    auxkey = choice(range(2, int(prime)))
                key = key + str(auxkey) + " "

        print("\n\nObtain result by console 'c' or by txt 't'?")
        election = input().strip()
        if election == "c":
            print(key)
        else:

            default = input("In default path /home/Documents?\n(Y/n)").strip().lower()
            if default == "y" or default == "yes" or default == "si" or default == "s":
                path = "/home/Documents"
            else:
                path = input("Enter path: ").strip()

            at = open(path+"/aKeys.txt", "w")   
            at.write(key)
            at.close()
    
                

if __name__ == "__main__": 
    main()
