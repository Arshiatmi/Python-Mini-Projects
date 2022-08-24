# -*- coding:utf-8 -*-

import os
import sys

play_code = False

try:
    file_name = sys.argv[1]
    try:
        play_code = sys.argv[2]
    except:
        pass
except:
    raise ValueError("Pass File Name As Arguemtnt To Application.")

f = open("words.txt", encoding='utf-8')
lines = f.readlines()
f.close()
words = {}
for i in lines:
    words[i.split(":")[0].strip()] = i.split(":")[1].strip()

f = open(file_name, "r", encoding='utf-8')
lines = f.readlines()
f.close()

ans = ""
for i in lines:
    string = i
    for j, z in words.items():
        string = string.replace(j, z)
    ans += string

f = open("output.py", "w", encoding='utf-8')
f.write(ans)
f.close()

if play_code == "run" or play_code == "play" or play_code == "--play":
    os.system("python output.py")
