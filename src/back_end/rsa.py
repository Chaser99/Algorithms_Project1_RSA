# rsa.py
import math
from random import random


# Checks if a given number is prime
def is_prime(number: int) -> bool:
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 11 == 0:
        return False
    for i in range(3, 20, 2):
        k = int(random() * number)
        if math.gcd(number, k) != 1:
            return False
        if k ** (number - 1) % number != 1:
            return False
    return True


# Returns a random integer within the minimum and maximum, inclusively.
def get_random_in_range(minimum: int, maximum: int) -> int:
    return int(minimum + (random() * (maximum - minimum)))


# Finds a prime number within a range.
def get_prime(minimum: int, maximum: int) -> int:
    p = get_random_in_range(minimum, maximum)
    while not is_prime(p):
        p = get_random_in_range(minimum, maximum)
    return p


class RSA:

    def __init__(self, minimum=1000):
        self.__minimum = minimum
        self.__maximum = (minimum * 10) - 1
        self.__p = get_prime(self.__minimum, self.__maximum)
        self.__q = get_prime(self.__minimum, self.__maximum)
        self.__n = self.__p * self.__q
        self.__f_of_n = (self.__p - 1) * (self.__q - 1)

        self.__e = self.__calculate_encrypt_key()
        self.__d = self.__calculate_decrypt_key()

    # Finds the encrypt key
    def __calculate_encrypt_key(self) -> int:
        e = get_random_in_range(self.__minimum, self.__f_of_n)
        while math.gcd(e, self.__f_of_n) != 1:
            e = get_random_in_range(self.__minimum, self.__f_of_n)
        return e

    def __calculate_decrypt_key(self) -> int:
        for d in range(3, self.__f_of_n, 2):
            if (self.__e * d) % self.__f_of_n == 1:
                if d < 0:
                    d += self.__f_of_n
                return d

        return -1

    def encrypt(self, message):
        ciphertext = []
        for x in message:
            ciphertext.append(pow(ord(x), self.__e, self.__n))
        return ciphertext

    def decrypt(self, ciphertext):
        message = ""
        for x in ciphertext:
            message += chr(pow(x, self.__d, self.__n))
        return message
