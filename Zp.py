from Entero import *

class Zp:
    def __init__(self, n = int, p = int) -> None:
        self.__n__ = n%p
        self.__p__ = p

    def getN(self) -> int:
        return self.__n__
    def getMod(self) -> int:
        return self.__p__
    def __str__(self) -> str:
        return str(self.__n__)

    def sum(self,b):
        if type(b) == Zp:
            return Zp(self.getN() + b.getN(),self.getMod())
    def rest(self,b):
        if type(b) == Zp:
            return Zp(self.getN() - b.getN(),self.getMod())
    def mult(self,b):
        if type(b) == Zp:
            return Zp(self.getN() * b.getN(),self.getMod())
    
    def pow(self,power = int, po = []):
        
        if po == list():
            po = Entero.toBinary(power)
        
        A = Zp(1, self.getMod())
        b = Zp(self.getN(), self.getMod())

        for i in po:
            if i == 1:
               A =  A.mult(b)
            b = b.mult(b)
        return A

    def inv(self, po = 1):
        if po == 1:
            po = Entero(self.getMod()).phi()-1
        return self.pow(po)