# rsa.py
import math
from random import random


def is_prime(number):
    if number % 2 == 0:
        return False
    for i in range(2, 10):
        k = int(random() * number)
        if math.gcd(number, k) != 1:
            return False
        if k ** (number - 1) % number != 1:
            return False
    return True

def get_random_in_range(minimum, maximum):
    return int(minimum + (random() * (maximum - minimum)))

def get_prime(minimum, maximum):
    p = get_random_in_range(minimum, maximum)
    while not is_prime(p):
        p = get_random_in_range(minimum, maximum)
    return p


class RSA:
    minimum = 10000
    maximum = 99999

    def __init__(self):
        self.p = get_prime(RSA.minimum, RSA.maximum)
        self.q = get_prime(RSA.minimum, RSA.maximum)
        self.n = self.p * self.q
        self.f_of_n = (self.p - 1) * (self.q - 1)

        self.e = get_random_in_range(1000, self.f_of_n)
        while math.gcd(self.e, self.f_of_n) != 1:
            self.e = get_random_in_range(1000, self.f_of_n)
