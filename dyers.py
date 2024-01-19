"""
:file: dyers.py
:author: Shane Kosieradzki
:created: 5/25/2023
"""

from eclib.randutils import *
from eclib.primeutils import *
from eclib.modutils import *
from math import floor
from prime_list import *

def keygen(bit_length, rho, rho_):
    p = get_prime_list(bit_length)
    nu = rho_ - rho
    kappa = get_prime_list(nu)

    return kappa, p


def pgen(bit_length, rho_, p):
    eta = bit_length ** 2 // rho_ - bit_length
    q = get_prime_list(eta)
    modulus = p * q

    return modulus


def encode(x, delta):
    m = floor(x / delta + 0.5)

    return int(m)


def decode(m, delta):
    x = m * delta

    return x


def encrypt(m, kappa, p, modulus):
    q = modulus

    r = get_rand(1, q)
    s = get_rand(0, kappa)
    c = (m + s * kappa + r * p) % modulus

    return c


def decrypt(c, kappa, p):
    m = min_residue(min_residue(c, p), kappa)

    return m


def enc(x, kappa, p, modulus, delta):
    c = encrypt(encode(x, delta), kappa, p, modulus)

    return c


def dec(c, kappa, p, delta):
    x = decode(decrypt(c, kappa, p), delta)

    return x


def add(c1, c2, modulus):
    c3 = (c1 + c2) % modulus

    return c3


def mult(c1, c2, modulus):
    c3 = (c1 * c2) % modulus

    return c3


if __name__ == '__main__':
    # Security Parameters #
    bit_length = 350
    rho = 1
    rho_ = 32
    delta = 0.1

    # Primes #
    kappa, p = keygen(bit_length, rho, rho_)
    modulus = pgen(bit_length, rho_, p)
