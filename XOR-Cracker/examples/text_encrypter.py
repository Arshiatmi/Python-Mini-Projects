import sys
sys.path.append('../')

from xor import XOR
filename = 'file.txt'

a = XOR(filename, dec_filename="target.txt")
a.encrypt(150)
