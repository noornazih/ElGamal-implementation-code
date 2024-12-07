def is_prime(n):
    #This function defined checks to see if the number n is a prime.
    if n < 2: #any number less than 2 is not a prime.
        return False
    for i in range(2, int(n**0.5) + 1):  #Checks if there are any divisors between 2 up to the square root of n.
        if n % i == 0: #if n is divisible by i
            return False #if remainder is 0
    return True

#Variable p (large prime) is equals to 19.
p = 19  
assert is_prime(p), f"{p} is not a prime number"

#The primitive root and private key are difined.
r = 2   #Primitive root modulo p
x = 5   #Private key

#Compute the public key y = r^x mod p
y = pow(r, x, p)  #y = r^x mod p

#Generate the private and public keys
print("The private key is: ", "x = ", x)
print("The public key is: ","r = ","(",r,")", "p =","(",p,")","y =","(",y,")")
