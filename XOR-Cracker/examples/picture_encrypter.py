import sys
sys.path.append('../')

from xor import XOR
filename = 'file.jpg'

instance = XOR(filename, dec_filename="target.jpg")
instance.encrypt(150)
