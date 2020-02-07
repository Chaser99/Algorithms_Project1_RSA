# rsa.py
import math
from random import random





class RSA:

    def __init__(self, minimum=1000):
        self.__minimum = minimum
        self.__maximum = (minimum * 10) - 1
        self.__p = self.__get_prime()
        self.__q = self.__get_prime()
        self.__n = self.__p * self.__q
        self.__f_of_n = (self.__p - 1) * (self.__q - 1)

        self.__e = self.__calculate_encrypt_key()
        self.__d = self.__calculate_decrypt_key()

    # Finds the encrypt key
    def __calculate_encrypt_key(self) -> int:
        e = int(self.__minimum + (random() * (self.__maximum - self.__minimum)))
        while math.gcd(e, self.__f_of_n) != 1:
            e = int(self.__minimum + (random() * (self.__maximum - self.__minimum)))
        return e

    def __calculate_decrypt_key(self) -> int:
        (x, y, d) = self.extended_gcd(self.__e, self.__f_of_n)
        if y < 0:
            y += self.__f_of_n
        return int(y)

    # Checks if a given number is prime
    def __is_prime(self, number: int) -> bool:
        if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 11 == 0:
            return False
        for i in range(3, 20, 2):
            k = int(random() * number)
            if math.gcd(number, k) != 1:
                return False
            if k ** (number - 1) % number != 1:
                return False
        return True

    # Finds a prime number within a range.
    def __get_prime(self) -> int:
        p = int(self.__minimum + (random() * (self.__maximum - self.__minimum)))
        while not self.__is_prime(p):
            p = int(self.__minimum + (random() * (self.__maximum - self.__minimum)))
        return p

    def extended_gcd(self, a=1, b=1):
        if a < b:
            a, b = b, a

        if b == 0:
            return (1, 0, a)
        (x, y, d) = self.extended_gcd(b, a % b)
        return y, x - a // b * y, d

    def encrypt_message(self, message):
        ciphertext = []
        for x in message:
            ciphertext.append(pow(ord(x), self.__e, self.__n))
        return ciphertext

    def decrypt_message(self, ciphertext):
        message = ""
        for x in ciphertext:
            message += chr(pow(x, self.__d, self.__n))
        return message

    def encrypt_signature(self, signature):
        ciphertext = []
        for x in signature:
            ciphertext.append(pow(ord(x), self.__d, self.__n))
        return ciphertext

    def decrypt_signature(self, ciphertext):
        message = ""
        for x in ciphertext:
            message += chr(pow(x, self.__e, self.__n))
        return message
