# RSA-Encryption-Decryption
Encrypts and Decrypts a message using RSA.

Inputs: Message, p, q
Outputs: Ciphertext, decrypted text

RSA steps:
1)  Given p and q,
    n = p * q
    phi = (p-1) * (q-1)
    
2)  Choose e,
    e must be greater than 1 and less than phi,
    e and phi must have their greatest common denominator of 1
    
3)  Calculate d,
    d is the modular inverse of e and phi
    
3)  The public key is e and n while the private key is d

4)  Encryption,
    Takes the message, e, and n, and encrypts with the formula, c = (p ^ e)mod n
    
5)  Decryption,
    Takes encrypted message and d and decrypts with the formula, t = (c ^ d)mod n
    


