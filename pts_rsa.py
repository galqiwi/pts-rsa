def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def rsa_keygen(p, q):
	n = p * q
	fi = (p - 1) * (q - 1)
	e = 65537
	
	d = modinv(e, fi)
	return {'public':(n, e), 'private':(n, d)}

p = 0xE306739D7FBD5F4DE81619FE0B3C7C049E1F60B593BB79BCECA6BF7C24275247
q = 0xE800E0652FB7F23D1112B29A03866898CA92341D89182A46BE633C2C21468615

keys = rsa_keygen(p, q)

f_public = open('rsa.pub', 'w')
f_private = open('rsa', 'w')

print(hex(keys['public'][0]), hex(keys['public'][1]), file=f_public)
print(hex(keys['private'][0]), hex(keys['private'][1]), file=f_private)

f_private.close()
f_public.close()