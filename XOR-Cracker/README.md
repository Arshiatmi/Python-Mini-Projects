# XOR Encrypt/Decrypter + Cracker In Python

**in this simple project you can encrypt and decrypt files with simple keys and you can crack them with cracker script.**

## Installation

```
git clone https://github.com/Arshiatmi/XOR-Cracker
cd XOR-Cracker
# Use Program And Have Some FUN !
```

## Usage

**Ways To Encrypt Or Decrypt Files:**

```
import xor

# Encrypt File
instance = XOR(filename, dec_filename="target.jpg")
instance.encrypt(key=150)

# Decrypt File
instance.decrypt(key=150)

# As You Might Know In XOR encryption Is Same As XOR Decryption. Then Both Functions Are The Same.

# You Can Remove The File After Encryption Or Decryption With This Command:
instance.remove()

```

**That How You Can Crack Encrypted Files:**

```
python cracker.py -f <file_name> -s <file_format> -l <language(Just For Text Files)>
```

# Built With

- [Python](https://www.python.org) - Scripting Language

## Authors

- **Arshia Tamimi** - [MegaExpert](https://github.com/Arshiatmi)
