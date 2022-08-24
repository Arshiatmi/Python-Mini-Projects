import os

class XOR:
    def __init__(self, filename, dec_filename="ans.txt"):
        path = os.getcwd()
        filename = os.path.join(path, filename)
        dec_filename = os.path.join(path, dec_filename)
        self.filename = filename
        self.dec_filename = dec_filename

    def encrypt(self, key, write=True):
        if write:
            handler = open(self.filename, "rb")
            writer = open(self.dec_filename, "wb")
            ans = b""
            for line in handler:
                for char in line:
                    writer.write(bytes([char ^ key]))
                    ans += bytes([char ^ key])
            writer.close()
            handler.close()
        else:
            pass
        return ans

    def decrypt(self, key):
        return self.encrypt(key)
    
    def remove(self):
        os.remove(self.dec_filename)
