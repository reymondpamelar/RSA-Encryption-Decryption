#Reymond Pamelar
#RSA Encryption/Decryption

#Checks if given value is prime
def primeChk(x):
    if x > 1:
        for i in range(2, x):
            if(x % i) == 0:
                print(x, "is not prime, please reenter another number: ")
                x = int(input(" "))
                return primeChk(x)
            else:
                return x
    else:
        print(x, "is not prime, please reenter another number: ")
        x = int(input(" "))
        return primeChk(x)
        
#Finds GCD of two values
def gcd(a, b):
    if(b==0): 
        return a 
    else: 
        return gcd(b, a%b)
    
#Modular inverse formula
def modInv(e, phi):
    e = e % phi
    for i in range(1, phi):
        if (e * i) % phi == 1 :
            return i;
    return none;

#Finds an e that is relatively prime to phi between e and 1000    
def eFinder(phi):
    e=2
    for i in range(e, 1000):
        if gcd(i,phi) == 1 and modInv(i,phi) != None:
            e=i
    return e

#Generates public and private key
def keyGen():
    p = int(input("Enter the p prime value: "))
    p = primeChk(p)
    q = int(input("Enter the q prime value: "))
    q = primeChk(q)
    
    #RSA modulus(n)
    n = p * q
    
    #block size
    blockSize = 0
    if n < 2727:
        raise Exception("n is too small, please enter another p and q.")
    if n >= 2727 and n < 272727:
        blockSize = 2
    if n >= 272727:
        blockSize = 3
    
    
    #Euler's Totient
    phi = (p - 1) * (q - 1)
    
    #Chosen e
    e = eFinder(phi)
    
    #Chosen d
    d = modInv(e, phi)

    

    print("Public key = ", e, ", ", n)
    print("Private key = ", d)
    return e, n, d, blockSize
    
#Takes a string, converts it to ascii values, and changes the value to be between 1 and 27
def asciiEncode(s):
    base = [ord(c) for c in s]
    length = len(base)
    for i in range(length):
        if base[i] == 32:
            base[i] = base[i]-5
        else:
            base[i] = base[i]-96
    return base
    
#used for list of lists
def dHelper(s):
    for i in range(len(s)):
        if s[i] == 27:
            s[i] = s[i]+5
        else:
            s[i] = s[i]+96
    return s
    
#Decodes either a list of lists or a list of integers    
def asciiDecode(s, pT):
    
    #Takes list or list of list and corrects the values back into ascii 
    if isinstance(s[1], list):
        for i in range(len(s)):
            s[i] = dHelper(s[i])
    else:
        for i in range(len(s)):
            if s[i] == 27:
                s[i] = s[i]+5
            else:
                s[i] = s[i]+96
    
    #Add padding
    if isinstance(s[1], list):
        if pT > 0 and pT != len(s[1]):
            for i in range(pT):
                s[len(s)-1].append(pT+96)
        if pT == len(s[1]):
            newBlock = []
            for i in range(pT):
                newBlock.append(pT+96)
            s.append(newBlock)
        
    #Return ascii values for display
    res = ""
    if isinstance(s[1], list):
        for i in range(len(s)):
            for val in s[i]:
                res = res + chr(val)
    else:
        for val in s:
            res = res + chr(val)
    return res
    
#Splits list of int into blocks    
def blockLength(A, size):
    for i in range(0, len(A), size):  
        yield A[i:i + size]
    return A

#Returns the amount of times needed for the last block to be padded   
def padTimes(A, size):
    padT=0
    i = len(A)-1
    if len(A[i]) < size:
        padT = size - len(A[i])
    return padT

#helper method for encryption formula
def eFormula(A):
    for i in range(len(A)):
        A[i] = (A[i]**e) % n
    return A


def encryptmessage():
    
    asciiMessage = asciiEncode(m)
    
    #Split into blocks
    blocks = list(blockLength(asciiMessage, blockSize))
    
    #Tmp pad and get count of times padded
    pT = padTimes(blocks, blockSize)
    if pT == 0:
        pT = blockSize
    
    #Encrypt values
    for i in range(len(blocks)):
        blocks[i] = eFormula(blocks[i])
    
    #Convert blocks to display as ascii characters
    eMessage = asciiDecode(blocks,pT)
    
    print("Cipher Text: ", eMessage)
    
    return eMessage

def decryptmessage():
    dText = asciiEncode(cText)
    
    #Decrypt values
    for i in range(len(dText) - dText[len(dText)-1]):
        dText[i] = (dText[i]**d) % n
    
    #Append values that are not padding values
    dMessage2 = []
    for i in range(len(dText) - dText[len(dText)-1]):
        dMessage2.append(dText[i])
    
    #Convert blocks to display as ascii characters
    dMessage = asciiDecode(dMessage2, -1)

    print("Decrypted message: ", dMessage)
    
    

m = input("Enter the plaintext consisting of an assortment of characters a->z or space: ")

e, n, d, blockSize = keyGen()

cText = encryptmessage()
decryptmessage () 




