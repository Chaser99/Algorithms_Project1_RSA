# rsa.py
import math
from random import random


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


def get_random_in_range(minimum: int, maximum: int) -> int:
    return int(minimum + (random() * (maximum - minimum)))


def get_prime(minimum: int, maximum: int) -> int:
    p = get_random_in_range(minimum, maximum)
    while not is_prime(p):
        p = get_random_in_range(minimum, maximum)
    return p


class RSA:
    minimum = 100
    maximum = 999

    def __init__(self):
        self.p = get_prime(RSA.minimum, RSA.maximum)
        self.q = get_prime(RSA.minimum, RSA.maximum)
        self.n = self.p * self.q
        self.f_of_n = (self.p - 1) * (self.q - 1)

        self.e = self.__calculate_encrypt_key()
        self.d = self.__calculate_decrypt_key()
        if self.d < 0:
            self.d += self.f_of_n

    def __calculate_encrypt_key(self) -> int:
        e = get_random_in_range(RSA.minimum, self.f_of_n)
        while math.gcd(e, self.f_of_n) != 1:
            e = get_random_in_range(RSA.minimum, self.f_of_n)
        return e

    def __calculate_decrypt_key(self) -> int:
        for d in range(3, self.f_of_n, 2):
            if (self.e * d) % self.f_of_n == 1:
                return d
        return -1

    def encrypt(self, message):
        pass

    def decrypt(self, ciphertext):
        pass
