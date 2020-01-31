# application.py

from back_end.rsa import *

rsa = RSA()

print(rsa.p)  # large prime, p
print(rsa.q)  # large prime, q
print(rsa.e)  # e, part of public key
