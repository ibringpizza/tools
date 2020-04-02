import base64
from itertools import cycle
import sys

def encrypt(data, key):
    xored = ''.join(chr(ord(a) ^ ord(b)) for (a,b) in zip(data, cycle(key)))
    xored = base64.encodebytes(bytes(xored, 'utf-8')).strip()
    return xored.decode('utf-8')

def decrypt(data, key):
    xored = base64.decodebytes(bytes(data, 'utf-8')).decode('utf-8')
    xored = ''.join(chr(ord(a) ^ ord(b)) for (a,b) in zip(xored, cycle(key)))
    return xored

if len(sys.argv) != 5:
    print('python encrypt.py encrypt/decrypt key input_file output_file')
    sys.exit()

if sys.argv[1] == 'encrypt' or 'e':
    read = open(sys.argv[3], 'r').read()
    encrypted = encrypt(read, sys.argv[2])
    open(sys.argv[4], 'w').write(encrypted)

if sys.argv[1] == 'decrypt' or 'd':
    read = open(sys.argv[3], 'r').read()
    decrypted = decrypt(read, sys.argv[2])
    open(sys.argv[4], 'w').write(decrypted)
