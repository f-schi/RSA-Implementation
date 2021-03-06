import random

def generate1024bitPrime():
    num = 0
    while rabinMillerTest() is False:
        num = generate1024bitNumber()
    return num

def rabinMillerTest():
    pass

def generate1024bitNumber():
    x = random.randrange(2 ** 1023, 2 ** 1024 - 1)
    return x



def coPrimeTest(a, b):
    #check if values a and b are coprime
    if euclideanAlgorithm(a, b) == 1:
        return True
    else:
        return False


def modularInverse(a,m):
    # returns the modular inverse of a^(-1) mod m
   gcd, s, t = extendedEuclideanAlgorithm(a,m)
   return t


def euclideanAlgorithm(a,b):
    # performs euclidean algorithm
    # returns greatest common denominator
    
    #init
    r = [a,b]
    i = 1

    #algorithm
    while r[i] != 0:
        i = i + 1
        r.append(r[i-2] % r[i-1])

    #output
    gcd = r[i-1]
    return gcd

def extendedEuclideanAlgorithm(a, b):
    # performs extended euclidean algorithm
    # returns greatest common denominator and bezout coefficients

    #init
    r = [a,b]
    s = [1,0]
    t = [0,1]
    q = [0]

    #algorithm
    i = 1
    while r[i] != 0:
        i = i + 1
        r.append(r[i-2] % r[i-1])
        q.append((r[i-2] - r[i]) / r[i-1])
        s.append(s[i-2] - q[i-1] * s[i-1])
        t.append(t[i-2] - q[i-1] * t[i-1])
    
    #output
    gcd = r[i-1]
    s = int(s[i-1])
    t = int(t[i-1])
    return(gcd, s, t)

