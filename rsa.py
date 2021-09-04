
from lib import encrypt
from lib import decrypt
  
def main():
    prompt = " "
    while prompt == " ":
        prompt = input("\nHello, welcome to the RSA Center! (enter 'quit' to exit) \n\
Enter 'keygen' to generate a key pair. \n\
Enter 'encrypt' to encrypt plaintext. \n\
Enter 'decrypt' to decrypt a cipher. \n\
")
        if prompt == 'keygen':
            #keygen()
            pass
        elif prompt == 'encrypt':
            encrypt.encrypt()
        elif prompt == 'decrypt':
            decrypt.decrypt()
        elif prompt == 'quit':
            exit()
        elif prompt == " ":
            pass
        else:
            print("\nError: Wrong Input")
            prompt = " "
main()

