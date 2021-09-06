from lib import functions as fun
import json

def keygen():

    p = fun.generate1024bitPrime()
    q = fun.generate1024bitPrime()
    n = p * q
    phiN  = (p-1) * (q-1)
    e = chooseE(phiN)
    d = chooseD(e, phiN)


    # Save Keys in 'keys.json'
    file = open('./resources/keys.json',)
    keys = json.load(file)
    keys["public"]["n"] = n
    keys["public"]["e"] = e
    keys["private"]["d"] = d
    file.write(keys)
    file.close
    print("\n...\nKeys successfully generated!\n...")


def chooseE(phi_n):
    # choose e {1,..,phi(n)-1}, such that gcd(e,phi(n)) = 1
    # generate an e until it is coprime with phi of n

    e = 0
    while fun.coPrimeTest(e, phi_n) == False: 
        e = fun.generate1024bitNumber()
    return e


def chooseD(e, phi_n):
    # choose d, such that d * e == 1 mod phi(n)
    d = fun.modularInverse(e, phi_n)
    return d

