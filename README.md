Challenges faced and solutions:
The challenges faced when implementing the encryption and decryption code was the modular exponentiation and when the modulo p is large, the exponentiation takes a very long time, to solve this, the built-in function pow() was used to make the process more efficient.
Another challenge faced was when generating a random number, the number was too weak making it easy for the attacker to guess therefore, the random module was added to help it be more secure

Findings:
The ElGamal encryption algorithm is secure based on its difficulty in solving discrete logarithms.
ElGamal is used to securely exchange keys however, its process is slower than symmetric algorithms like AES. 
ElGamal is useful for digital signatures and key exchange.
