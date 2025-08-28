import random
import math

def is_prime(n, k=40):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for j in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_large_prime(bits=8, k=40):
    while True:
        num = random.getrandbits(bits)
        num = random.randint(2**(bits-1), 2**bits - 1)
        if num % 2 == 0:
            num += 1

        if is_prime(num):
            return num

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_public_key(phi):
    for num in range(3, phi):
        if gcd(num, phi) == 1:
            return num
        
def find_private_key(phi, e):
    p = phi+1
    while True:
        if (e * p) % phi == 1:
            return p
        p += 1

p = q = 0

while p == q:
    p = generate_large_prime()
    q = generate_large_prime()

n = p*q
phi = (p - 1) * (q - 1)

e = find_public_key(phi)
d = find_private_key(phi, e)

print(p)
print(q)
print(n)
print(phi)
print(e)
print(d)