from lib import functions as fun
import json

def keygen():
    print("IN DEV")
    p = fun.generatePrime()
    q = fun.generatePrime()
    n = p * q
    phi_n  = (p-1) * (q-1)
    e = chooseE(phi_n)
    d = chooseD()


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
    e = 0
    while fun.coPrimeTest(e, phi_n) == False: # generate an e until it is coprime with phi of n
        e = fun.generate1024bitNumber()
    return e


def chooseD():
    # choose d, such that d * e == 1 mod phi(n)
    pass

