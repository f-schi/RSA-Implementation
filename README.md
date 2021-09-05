# RSA-Implementation

**Instruction:**
* run 'rsa.py' and follow the console guidance.

**Functionality:**
* keygen: generates a keypair and stores it in 'resources/keys.json'
* encrypt: generates a ciphertext from 'resources/message.txt' and stores it in 'resources/cipher.txt' using the public key in 'resources/keys.json'
* decrypt: generates a plaintext from 'resources/cipher.txt' and stores it in 'resources/message.txt' using the private key in 'resources/keys.json'

**Not yet implemented**
* square-and-multiply Exponentiation, as the python-native pow function already uses this technique for faster exponentiation
* fast decryption using the chinese remainder theorem
