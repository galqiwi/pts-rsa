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

key = open('rsa', 'r')

n, d = [int(i, 16) for i in key.read().split(' ')]

msg_f = open('msg', 'r')

msg = int(msg_f.read(), 16)

msg_decoded = power(msg, d, n).to_bytes(n.bit_length(), byteorder = 'big').decode()

print(msg_decoded)