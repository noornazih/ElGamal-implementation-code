import random

def decrypt(C1, C2, x, p):
    Z = pow(C1, x, p) #Calculates Z = C1^x mod p 
    
    Z_inverse = pow(Z, -1, p) #The modular inverse of Z modulo p (Z^-1 mod p)
    
    T = (C2 * Z_inverse) % p #Decrypts the message using T = C2 * Z^-1 mod p
    return T

#The variable's values:
p = 19        #Prime number
r = 2         #Primitive root 
x = 5         #Private key
y = pow(r, x, p)  #Public key: y = r^x mod p

#encrypted ciphertext (C1, C2):
C1 = 8  #C1 = r^n mod p
C2 = 8  #C2 = T * y^n mod p (where T = 7 and y = 13, n = 3)

#ciphertext is decrypted by using the private key.
original_message = decrypt(C1, C2, x, p)

#the decrypted message
print("the decrypted message is: ", original_message)