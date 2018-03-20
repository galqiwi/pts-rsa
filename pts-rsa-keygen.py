#
#   RSA KEYGEN BY MALINOVSKII VLADIMIR
#

from argparse import ArgumentParser
from os import path
import random

parser = ArgumentParser()

parser.add_argument("-k", "--key", dest="keyfile", default = (path.dirname(path.abspath(__file__)) + "/rsa"), help="path to key file")

args = parser.parse_args()

def egcd(a, b):
    if a == 0:
        return (0, 1)
    else:
        y, x = egcd(b % a, a)
        return (x - (b // a) * y, y)

def modinv(a, m):
    x, y = egcd(a, m)
    return x % m

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def rsa_keygen(p, q):
	n = p * q
	phi = (p - 1) * (q - 1)
	e = random.randint(p // 2, p)
	while (gcd(e, phi) != 1):
		e = e + 1

	#print(e)
	d = modinv(e, phi)
	return {'public':(n, e), 'private':(n, d)}

p, q = [int(i, 16) for i in random.sample(open('primes', 'r').read().split('\n'), 2)]

keys = rsa_keygen(p, q)

f_public = open(args.keyfile + '.pub', 'w')
f_private = open(args.keyfile, 'w')

print(hex(keys['public'][0]), hex(keys['public'][1]), file=f_public)
print(hex(keys['private'][0]), hex(keys['private'][1]), file=f_private)

f_private.close()
f_public.close()