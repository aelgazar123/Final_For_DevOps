import sympy
import random


def gen_key():
    plist = list(sympy.primerange(200, 500))
    q = plist[random.randint(0, len(plist))]
    p = plist[random.randint(0, len(plist))]
    while p == q:
        p = plist[random.randint(0, len(plist))]
    return p * q


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;

    else:
        return gcd(b, a % b)


def modInverse(a, m):
    a = a % m;
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1


def power(x, e, m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E / 2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y


def key_gen(n):
    key = random.randint(1000, phi(n))
    while gcd(phi(n), key) != 1:
        key = random.randint(1000, phi(n))
    return key


def phi(n):
    totient = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            totient += 1
    return totient


def coprime(a, b):
    return gcd(a, b) == 1


def main():
    msg = 'mathematics is the music of reason'
    print("Original Message:", msg)


def key_gen(n):
    key = random.randint(1000, phi(n))
    while gcd(phi(n), key) != 1:
        key = random.randint(1000, phi(n))
    return key


def encryption(msg, n, e):
    listing = list(msg)
    print(listing)
    asciiList = [ord(c) for c in listing]
    print(asciiList)
    cipher = []
    for i in asciiList:
        cipher.append(power(i, n, e))
    print(cipher)


def findD(key, n):
    return modInverse(key, phi(n))


def decryption(msg, d, n):
    cipher = []
    for i in msg:
        cipher.append(power(i, d, n))
    print(cipher)
    convert = []
    for p in cipher:
        convert.append(chr(p))
    print(convert)


def power(x, e, m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E / 2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y