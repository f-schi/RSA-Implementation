import json

def decrypt():
    # Decrypts a message

    print("\n...")

    # Load Public Key and Private Key from 'keys.json'
    file = open('./resources/keys.json',)
    keys = json.load(file)
    file.close()
    n = keys["public"]["n"]
    d = keys["private"]["d"]
    if n and d:
        print("Private Key successfully loaded!")
    else:
        print("Error: Private Key not found")


    # Load cipher from 'cipher.txt'
    with open('./resources/cipher.txt') as file:
        cipher = file.read()
    if cipher:
        print("Cipher successfully loaded!")
    else:
        print("Error: Cipher not found")


    # Perform RSA Decryption
    plaintext = ""
    ciphersplit = cipher.split()
    for character in ciphersplit:
        x = int(character) #transform unicode to letter
        plaintext += chr(pow(x, d, n))
    if plaintext:
        print("Message successfully generated!")
    else:
        print("Error: Message could not be generated")


    # Save encrypted text in cipher.txt
    with open('./resources/message.txt', 'w') as file:
        file.write(plaintext)
    if plaintext:
        print("Message successfully saved!")
    else:
        print("Error: Message could not be saved")
        
    print("...")

