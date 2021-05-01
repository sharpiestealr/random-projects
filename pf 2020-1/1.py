#text replacer for a tenis-polar type crypto

import os
import sys
import fileinput

with open('criptografado.txt', 'r') as file:
    lines = file.readlines()

for i in range(len(lines)):
    ch = 0
    while (ch != len(lines[i])):
        if lines[i][ch] == 's':
           lines[i][ch] == 'z'
        elif lines[i][ch] == 'z':
           lines[i][ch] == 's'
        elif lines[i][ch] == 'a':
           lines[i][ch] == 'e'
        elif lines[i][ch] == 'e':
           lines[i][ch] == 'a'
        elif lines[i][ch] == 'b':
           lines[i][ch] == 'r'
        elif lines[i][ch] == 'r':
           lines[i][ch] == 'b'
        ch +=1

for line in range(len(lines)):
    print(lines(line))