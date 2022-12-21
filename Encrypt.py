import random
from Zp import*

class Encryptor:
    def __init__(self, to_encrypt = "", to_decrypt = "", mod = 19999999) -> None:
        self.__to_encrypt = to_encrypt
        self.__to_decrypt = to_decrypt
        self.__mod = mod
        self.__encrypted = ""
        self.__decrypted = ""
       
    def cesaro(self, a = 1, b = 1) -> str:
        if self.__encrypted !="":
            return self.__encrypted
        mod = self.__mod
        a = Zp(a,mod)
        b = Zp(b,mod)

        for letter in self.__to_encrypt:
            self.__encrypted += str(a.mult(Zp(ord(letter),mod)).sum(b).getN())+ "  "
        return self.__encrypted

    def inv_cesaro(self, a=1, b=1) -> str:
        if self.__decrypted!="":
            return self.__decrypted
        if type(self.__to_decrypt) == str:
            self.__to_decrypt = self.__to_decrypt.split("  ")
        
        mod = self.__mod
        b = Zp(b,mod)
        a1 = Zp(a,mod).inv()
        
        for letter in self.__to_decrypt:
            if letter.isnumeric():
                self.__decrypted+= chr(a1.mult(Zp(int(letter),mod).rest(b)).getN())
        return self.__decrypted
    
    def vigenere(self, a = [1], b = [1]) -> str:
        if self.__encrypted!="":
            return self.__encrypted
		# checar que los elemnetos de a no tengan divisores en común con modCesaro
        mod = self.__mod

        for i in range(len(a)):
            a[i] = Zp(a[i],mod)
        for i in range(len(b)):
            b[i] = Zp(b[i],mod)
        
        modA = len(a)
        modB = len(b)
        iA = 0
        iB = 0
        
        for letter in self.__to_encrypt:
            self.__encrypted += str(a[iA].mult(Zp(ord(letter),mod)).sum(b[iB]).getN())+ "  "
            iA = (iA + 1)%modA
            iB = (iB + 1)%modB
			
        return self.__encrypted

    def inv_vigenere(self, a=[1], b=[1]) -> str:
        if self.__decrypted!="":
            return self.__decrypted
        mod = self.__mod
        self.__to_decrypt = self.__to_decrypt.split("  ")

        for i in range(len(a)):
            a[i] = Zp(a[i],mod)
        for i in range(len(b)):
            b[i] = Zp(b[i],mod)
        s = list(map(lambda x: x.inv(), a))

        modA = len(a)
        modB = len(b)
        iA = 0
        iB = 0
       
        for letter in self.__to_decrypt:

            if letter.isnumeric():
                self.__decrypted+= chr(s[iA].mult(Zp(int(letter),mod).rest(b[iB])).getN())

            iA = (iA + 1)%modA
            iB = (iB + 1)%modB
        return self.__decrypted
    
    def Vernam(self) -> tuple:
        if self.__encrypted !="":
            return self.__encrypted

        mod = self.__mod
        aaux = 0
        baux = 0
        a = list()
        b = list()
        po = Entero(mod).phi()-1
        isPrime = False
        if po == mod -2:
            isPrime = True
        i=0
        for letter in self.__to_encrypt:
            
            b.append(random.choice(range(mod)))
            aaux = random.choice(range(mod))

            if not isPrime:
                aux = Zp(aaux,mod)
                while aux.inv(po).mult(aux).getN() != 1:
                    aaux = random.choice(range(mod))
                    aux = Zp(aaux,mod)
            
            a.append(aaux)
                 
            self.__encrypted +=str(Zp(a[i],mod).mult(Zp(ord(letter), mod)).sum(Zp(b[i],mod)).getN())+ "  "
            
            i+=1
        return self.__encrypted, a, b

    def inv_Vernam(self, a, b) -> tuple:
        if self.__decrypted!="":
            return self.__decrypted
        mod = self.__mod


        self.__to_decrypt = self.__to_decrypt.split("  ")

        i = 0
        phi = Entero(mod).phi() - 1
        
        for letter in self.__to_decrypt:
            if letter.isnumeric():
                
                s = Zp(a[i],mod).inv(phi)  
                
                self.__decrypted+= chr(s.mult(Zp(int(letter),mod).rest(Zp(b[i],mod))).getN())
                i+=1
        return self.__decrypted