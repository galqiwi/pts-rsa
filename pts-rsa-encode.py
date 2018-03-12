#
#	RSA ENCODER BY MALINOVSKII VLADIMIR
#

from argparse import ArgumentParser
from os import path

parser = ArgumentParser()

parser.add_argument("-k", "--key", dest="keyfile", default = (path.dirname(path.abspath(__file__)) + "/rsa.pub"), help="path to key file")
parser.add_argument("-m", "--message", dest="msgfile", default = (path.dirname(path.abspath(__file__)) + "/msg"), help="path to message file")

args = parser.parse_args()

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

key = open(args.keyfile, 'r')

n, e = [int(i, 16) for i in key.read().split(' ')]

msg = input()

msg_encoded = pow(int.from_bytes(msg.encode(), byteorder='big'), e, n)

print(hex(msg_encoded), file=open(args.msgfile, 'w'))
