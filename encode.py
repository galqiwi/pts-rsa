from sys import getdefaultencoding

def power(msg, key, n):
	# return (msg ** key) % n
	out = 1
	while (key != 0):
		if (key % 2 == 1):
			out = (out * msg) % n
		msg = (msg * msg) % n
		key = key >> 1
	return out

key = open('rsa.pub', 'r')

n, e = [int(i, 16) for i in key.read().split(' ')]

msg = input()

print(int.from_bytes(str.encode(msg), byteorder='big'))

msg_encoded = pow(int.from_bytes(msg.encode(), byteorder='big'), e, n)

print(hex(msg_encoded), file=open('msg', 'w'))
