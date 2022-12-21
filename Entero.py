class Entero:
    __primesTXT = open("Files/primes.txt", "r")
    __primes = list(map(lambda x: int(x),__primesTXT.read().split(" ")[:-1]))
    __primesTXT.close()
    __primesIniLen = len(__primes)

    
    def __init__(self, k = int, fact = list) -> None:
        
        self.__k = k
        self.__fact = []
        self.__phi = 0

    @staticmethod
    def primesW():
        aux = open("Files/primes.txt", "a")
        au = ""
        if Entero.__primesIniLen < len(Entero.__primes):
            for i in Entero.__primes[Entero.__primesIniLen:]:
                au = au + str(i) + " "
            aux.write(au)
            Entero.__primesIniLen = len(Entero.__primes)
        aux.close()
        

    def factorizacion(self) -> list:
        
        """ Factoriza el número

        Returns:
            list: Lista con la factorización del número
        """
        if self.__fact != list(): return self.__fact
        auxk = abs(self.__k)
        if auxk == 0: 
            self.__fact.append(0)
            return self.__fact 
        
        isPrime = True

        primos  = Entero.__primes

        if not primos: 
            primos.append(2)
            primos.append(3)
            primos.append(5)
        for i in range(0, primos.__len__()):
            if auxk< primos[i]: break
            while auxk % primos[i] == 0:
                auxk = auxk//primos[i]
                self.__fact.append(primos[i])
                
        if auxk == 1: return self.__fact
        l = 1
        while 6*l + 5 <primos[primos.__len__()-1]: l +=1


        for i in range(l,auxk+1):
            Entero.primesW()
            S5 = 6*i+5
            S1 = 6*i+1
            if S5>auxk and S1>auxk:  break
            
            isPrime1 = True
            isPrime2 = True

            for j in range(primos.__len__()):
                if(isPrime1 and (S1)%primos[j]==0): 
                    isPrime1 = False

                if(isPrime2 and (S5)%primos[j]==0): 
                    isPrime2 = False
    
                if(not isPrime1 and not isPrime2): break
                
            if isPrime1: primos.append(S1)

            while isPrime1 and auxk % primos[primos.__len__()-1] == 0: 
                auxk = auxk//primos[primos.__len__()-1]
                self.__fact.append(primos[primos.__len__()-1])

            if isPrime2: primos.append(S5)

            while isPrime2 and auxk % primos[primos.__len__()-1] == 0:
                auxk = auxk//primos[primos.__len__()-1]
                self.__fact.append(primos[primos.__len__()-1])


            
        self.__fact.sort()
        return self.__fact

        
    def phi(self) -> int:
        """Obtiene la función phi valuada en el entero
        """
        if self.__fact == list(): self.factorizacion()
        if abs(self.__k) == 1: return 1
        
        if (self.__phi > 0): return self.__phi
        
        self.__phi = 1
        
        if(self.__fact.__len__() == 1):
            if self.__fact[0] == 0: return 1
            return self.__fact[0] - 1
        
        for i in range(self.__fact.__len__()):
            if(i<self.__fact.__len__()-1):
                if(self.__fact[i] == self.__fact[i+1]):
                    self.__phi *=self.__fact[i]
                else:
                    self.__phi *=(self.__fact[i] -1)
            else:
                self.__phi *=(self.__fact[i] -1)
        return self.__phi

    @staticmethod
    def mcd(a=1, b=1)-> tuple:
        aaux=a
        baux=b

        s0=t_1=0
        s_1=t0=1
        if a<0: a=-a
        if b<0: b=-b

        r=a%b

        while r!=0:
            q = a//b
            a=b
            b=r
            s=s0
            t=t0
            s0=s_1-q*s0
            t0=t_1-q*t0
            s_1=s
            t_1=t
            r=a%b

        
        return(b, -s0 if aaux <0 else s0, -t0 if baux <0 else t0)
    
    @staticmethod
    def toBinary(k = int,reversed = False) -> list:
        bin = list()
        aux = k

        if aux%2 == 0:
            bin.append(0)
        else:
            bin.append(1)
        
       
        while aux//2 != 0 :
            aux = aux//2
            if aux%2 == 0:
                bin.append(0)
            else:
                bin.append(1)
            
        if reversed: bin.reverse()
        return bin
    @staticmethod
    def esPrimo(p):
        for i in Entero._Entero__primes:
            if p < i: break
            if p%i == 0: False
        return True
    @staticmethod
    def ranPrime():
        from random import choice
        return choice(Entero.__primes)
