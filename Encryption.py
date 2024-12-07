import random

def encrypt(T, n): #ElGamal encryption function with parameters T (plaintext) and n (random integer).
    C1 = pow(r, n, p) #C1 = r^n mod p
    C2 = (T * pow(y, n, p)) % p #C2 = T * y^n mod p
    return C1, C2

#The variable's values:
p = 19        #Large Prime number
r = 2         #Primitive root
x = 5         #Private key
y = pow(r, x, p)  #Public key: y = r^x mod p

T = 7 #text/message to be encrypted

n = 3 #a random number

#the message and the random number
print("The given text: ", T)
print("The random number: ", n)

#Encrypt the message using ElGamal encryption
C1, C2 = encrypt(T, n)

#Display the ciphertext C1 and C2
print("The ciphertext is: ", "C1 = ", C1, "C2 = ", C2)
