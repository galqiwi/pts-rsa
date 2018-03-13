#
#	RSA DECODER BY MALINOVSKII VLADIMIR
#

from argparse import ArgumentParser
from os import path

parser = ArgumentParser()

parser.add_argument("-k", "--key", dest="keyfile", default = (path.dirname(path.abspath(__file__)) + "/rsa"), help="path to key file")
parser.add_argument("-m", "--message", dest="msgfile", default = (path.dirname(path.abspath(__file__)) + "/msg"), help="path to message file")

args = parser.parse_args()

from sys import getdefaultencoding

def mult(a, b, n):
	out = 0
	while (b != 0):
		if (b % 2 == 1):
			out = (out + a) % n
		a = (a << 1) % n
		b = b >> 1
	return out

def power(msg, key, n):
	# return (msg ** key) % n
	out = 1
	while (key != 0):
		if (key % 2 == 1):
			out = mult(out, msg, n)
		msg = mult(msg, msg, n)
		key = key >> 1
	return out

key = open(args.keyfile, 'r')

n, d = [int(i, 16) for i in key.read().split(' ')]

msg_f = open(args.msgfile, 'r')

msg = int(msg_f.read(), 16)

msg_decoded = power(msg, d, n).to_bytes(n.bit_length(), byteorder = 'big').decode()

print(msg_decoded)