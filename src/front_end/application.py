# application.py

from back_end.rsa import *

rsa = RSA()

message = "RSA IS SECURE. This is a message that is going to be encrypted."

ciphertext = rsa.encrypt(message)

decypheredtext = rsa.decrypt(ciphertext)

print(message)
print(ciphertext)
print(decypheredtext)
