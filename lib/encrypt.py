import json

def encrypt():
    # Encrypts a message

    print("\n...")
    # Load Public Key from 'keys.json'
    f = open('./resources/keys.json',)
    keys = json.load(f)
    f.close()
    n = keys["public"]["n"]
    e = keys["public"]["e"]
    if n and e:
        print("Public Key successfully loaded!")
    else:
        print("Error: Public Key not found")


    # Load Message from 'message.txt'
    with open('./resources/message.txt') as f:
        plaintext = f.read()
    if plaintext:
        print("Message successfully loaded!")
    else:
        print("Error: Message not found")


    # Perform RSA Encryption
    cipher = ""
    for character in plaintext:
        x = ord(character) #tranform letter to unicode
        cipher += str(pow(x, e, n)) + " "
    if cipher:
        print("Cipher successfully generated!")
    else:
        print("Error: Error: Cipher could not be generated")

    # Save encrypted text in cipher.txt
    with open('./resources/cipher.txt', 'w') as f:
        f.write(cipher)
    if cipher:
        print("Cipher successfully saved!")
    else:
        print("Error: Cipher could not be save")
    print("...")