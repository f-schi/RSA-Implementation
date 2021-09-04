import json

def decrypt():
    # Decrypts a message

    print("\n...")
    # Load Public Key and Private Key from 'publickey.json' and 'privatekey.json'
    f = open('./resources/publickey.json',)
    pubkey = json.load(f)
    f.close()
    n = pubkey["n"]
    f = open('./resources/privatekey.json',)
    privkey = json.load(f)
    f.close()
    n = pubkey["n"]
    d = privkey["d"]

    if n and d:
        print("Private Key successfully loaded!")
    else:
        print("Error: Private Key not found")


    # Load cipher from 'cipher.txt'
    with open('./resources/cipher.txt') as f:
        cipher = f.read()
    if cipher:
        print("Cipher successfully loaded!")
    else:
        print("Error: Cipher not found")


    # Perform RSA Decryption
    plaintext = ""
    ciphersplit = cipher.split()
    for character in ciphersplit:
        plaintext += chr(pow(int(character), d, n))
    if plaintext:
        print("Message successfully generated!")
    else:
        print("Error: Message could not be generated")


    # Save encrypted text in cipher.txt
    with open('./resources/message.txt', 'w') as f:
        f.write(plaintext)
    if plaintext:
        print("Message successfully saved!")
    else:
        print("Error: Message could not be saved")
    print("...")
    print("\nCipher:")
    print(cipher)
    print("\nPlaintext:")
    print(plaintext)
