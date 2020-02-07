# application.py

from back_end.rsa import *

rsa = RSA()

message = "RSA IS SECURE. This is a message that is going to be encrypted."

ciphertext = rsa.encrypt_message(message)

decypheredtext = rsa.decrypt_message(ciphertext)

print(message)
print(ciphertext)
print(decypheredtext)


signature = "My Name"
encrypted_sig = rsa.encrypt_signature(signature)
decrypted_sig = rsa.decrypt_signature(encrypted_sig)

print(signature)
print(encrypted_sig)
print(decrypted_sig)