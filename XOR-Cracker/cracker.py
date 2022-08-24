from signatures import signatures,languages
import re
import os
import colorama
from xor import XOR
from langdetect import detect
import argparse

import sys

if sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")

parser = argparse.ArgumentParser(description ='Crack a file That Encrypted With XOR And Find The Key.')
parser.add_argument('-f', '--file', help='File to be cracked.')
parser.add_argument('-l', '--language', help='Language of text file to be used ( if file format is text )')
parser.add_argument('-s', '--format', help='Format to be used')
args = parser.parse_args()

print(f"""
{colorama.Fore.LIGHTYELLOW_EX}################################################################################{colorama.Fore.LIGHTWHITE_EX}

Welcome To XOR Cracker By {colorama.Fore.LIGHTRED_EX}MegaExpert{colorama.Fore.LIGHTWHITE_EX}

Supported Formats Are :
{colorama.Fore.LIGHTBLUE_EX}{', '.join(signatures.keys())}{colorama.Fore.LIGHTWHITE_EX}
""")

if not args.format:
    target_format = input("""Enter Target File Format That You Want To Crack : """)
else:
    target_format = args.format

file_name = ""
text_language = ""
target_format = target_format.strip().lstrip('.').lower()
if target_format in signatures.keys():
    if not args.file:
        file_name = input("Enter Filename: ").strip()
    else:
        file_name = args.file
    if os.path.exists(file_name):
        if target_format == "txt":
            print(f"""
{colorama.Fore.LIGHTWHITE_EX}Supported Languages Are (ISO 639-1 codes):
    {colorama.Fore.LIGHTBLUE_EX}af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he,
    hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl,
    pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw{colorama.Fore.LIGHTWHITE_EX}
""")
            if not args.language:
                text_language = input("""Enter Target Language: """)
            else:
                text_language = args.language
            if text_language in languages:
                pass
            else:
                print("You Entered Invalid Format :(")
                exit(2)
    else:
        print("File Does Not Exists :/")
        exit(3)
else:
    print("You Selected Wrong Format :(")
    exit(1)

decrypted_file = f"ans.{target_format}"

instance = XOR(file_name, dec_filename=decrypted_file)

answer = -1

possibles = []
possible_texts = []

counter = 0
while counter < 256:
    print(
        f"{colorama.Fore.LIGHTBLUE_EX}[?] Trying Key : {colorama.Fore.LIGHTMAGENTA_EX}{counter}{colorama.Fore.LIGHTWHITE_EX}")
    answer = instance.decrypt(counter)
    hexdata = ""
    text_data = ""
    with open(decrypted_file, 'rb') as f:
        text_data = f.read()
        hexdata = text_data.hex().upper()
    for k in signatures[target_format]:
        if re.match(k, hexdata[:len(k)]):
            answer = counter
            print(
                f"{colorama.Fore.LIGHTGREEN_EX}[+] Key {colorama.Fore.LIGHTMAGENTA_EX}{counter}{colorama.Fore.LIGHTGREEN_EX} Seems Working !{colorama.Fore.LIGHTWHITE_EX}")
            counter = 256
            break
    if target_format == 'txt':
        try:
            ans = (text_data.decode())
        except:
            counter += 1
            continue
        lang = detect(ans)
        if lang == text_language:
            print(f"{colorama.Fore.LIGHTGREEN_EX}[+] Key {colorama.Fore.LIGHTMAGENTA_EX}{counter}{colorama.Fore.LIGHTGREEN_EX} Seems Working !{colorama.Fore.LIGHTWHITE_EX}")
            possibles.append(counter)
            possible_texts.append(ans[:100] + '...')
    counter += 1


if target_format == 'txt':
    print()
    if len(possibles) == 1:
        print(f"{colorama.Fore.LIGHTWHITE_EX}Answer Is : {colorama.Fore.LIGHTWHITE_EX}")
    else:
        print(f"{colorama.Fore.LIGHTWHITE_EX}Possible Answers Are : {colorama.Fore.LIGHTWHITE_EX}")
    print(f"\t{colorama.Fore.LIGHTGREEN_EX}{', '.join(map(str,possibles))}{colorama.Fore.LIGHTWHITE_EX}")
    for i,j in zip(possibles,possible_texts):
        print(f"""\n\t{colorama.Fore.LIGHTGREEN_EX}[{i}] -> {colorama.Fore.LIGHTWHITE_EX} {j}\n""")
    print()
    print(f"{colorama.Fore.LIGHTYELLOW_EX}################################################################################{colorama.Fore.LIGHTWHITE_EX}")
else:
    print()
    print(f"{colorama.Fore.LIGHTWHITE_EX}Answer Is : {colorama.Fore.LIGHTWHITE_EX}")
    print(f"\t{colorama.Fore.LIGHTGREEN_EX}{answer}{colorama.Fore.LIGHTWHITE_EX}")
    print()
    print(f"{colorama.Fore.LIGHTYELLOW_EX}################################################################################{colorama.Fore.LIGHTWHITE_EX}")
