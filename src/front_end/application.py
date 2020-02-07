# application.py

from back_end.rsa import *

rsa = RSA()

#front end

rsa = RSA()

def main():
    print("Do you want to ")
    print("1. Encrypt or decrypt a message or ")
    print("2. Decipher or sign a document digitally?")
    print("Enter 1 or 2: ")
    encrypt_or_sign = int(input())
    print("Are you sending or recieving message?")
    print("1. Sending")
    print("2. Recieveing")
    print("Enter 1 or 2: ")
    send_or_recieve = int(input())

    if encrypt_or_sign == 1 and send_or_recieve == 1:
        encrypt_sender()
    elif encrypt_or_sign == 1 and send_or_recieve == 2:
        encrypt_reciever()
    elif encrypt_or_sign == 2 and send_or_recieve == 1:
        sign_sender()
    elif encrypt_or_sign == 2 and send_or_recieve == 2:
        sign_reciever()
    

    
def encrypt_sender():
    #encrypts message
    print("Input the message you want to send:")
    message = input()

    encryptedMessage = rsa.encrypt_message(message)
    
    print("Encrypted message is: ")
    print(message)


def encrypt_reciever():
    #decrypts message
    print("Enter the encrypted messsage:")
    encrypted_mes = input()

    decryptedMessage = rsa.decrypt_message(encrypted_mes)
    
    print("The deciphered message is: ")
    print(decryptedMessage)
    
def sign_sender():
    #sign digital document
    print("Enter file name to be signed:")
    filename = input ("Filename: ");
    with open (filename, "a") as f:
        f.write (input ());
    
    
    


def sign_reciever():
    #decipher digital signature
    print("Enter file name to be read:")
   
    

