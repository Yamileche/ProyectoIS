#!/usr/bin/python3
import click
#from traitlets import default

from Encrypt import *

@click.group()
def main():
    """Encrypting program"""
    

@main.command()
@click.argument('pollito')
@click.option('--option', '-o', default='option', help="mete helps")
@click.option('--bandera', '-b', is_flag = True, default=True, help="mete helps")
def saluda_usuario(pollito, option, bandera):
    """Encrypting program"""
    print("Me gusta el ", pollito) 

@main.command()
@click.option('--cesaro', '-c',is_flag =True,  help = 'Cesaro method')
@click.option('--vigenere', '-vi',is_flag =True,  help = 'vigenere method')
@click.option('--vernam', '-ve',is_flag =True,  help = 'Cesaro method')
def encrypt(cesaro, vigenere, vernam):
    path = ""
    if cesaro:
        print("Cesaro method")
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        p = int(input("Enter prime:"))
        print("Enter text by console 'c' or by txt 't'?")
        ele = input().strip()
        if ele.lower() == 'c':
            text = input("Enter text:\n\n")
        else:
            path = input("Enter path: ")
            inp = open(path, "r")
            text = inp.read()
            inp.close()

        out = Encryptor(text, modCesaro = p).cesaro(a = a, b = b)

        
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

        

if __name__ == "__main__": 
    main()