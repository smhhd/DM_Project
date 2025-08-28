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


def rsa_key_gen():
    p = q = 0

    while p == q:
        p = generate_large_prime()
        q = generate_large_prime()

    n = p*q
    phi = (p - 1) * (q - 1)

    e = find_public_key(phi)
    d = find_private_key(phi, e)

    return (n, e), (n, d)


def convert_message_to_ascii(message):
    to_ascii = []
    for c in message:
        to_ascii.append(ord(c))
    return to_ascii


def convert_ascii_to_message(ascii_list):
    message = ""
    for num in ascii_list:
        message += chr(num)
    return message


def encrypt(m, pub_key):
    n, e = pub_key
    return pow(m, e, n)


def decrypt(c, pv_key):
    n, d = pv_key
    return pow(c, d, n)


def main():
    public, private = rsa_key_gen()
    message = input("Please enter your message: ")
    ascii_message = convert_message_to_ascii(message)
    encrypted_msg_ascii = [encrypt(ch, public) for ch in ascii_message]
    print(f"The encrypted message is: {encrypted_msg_ascii}")
    decrypted_msg_ascii = [decrypt(ch, private) for ch in encrypted_msg_ascii]
    decrypted_msg = convert_ascii_to_message(decrypted_msg_ascii)
    print(f"The decrypted message is: {decrypted_msg}")


if __name__ == "__main__":
    main()
