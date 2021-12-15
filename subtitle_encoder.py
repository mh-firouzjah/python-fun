'''
convert all subtile (*.srt) files inside given directory
from encoding `windows 1256` to `utf-8`
'''

import os

for filename in os.listdir(input("Enter file(s) directory: ")):
    if filename.endswith('.srt'):
        with open(filename, mode='r', encoding='windows-1256') as target:
            text = target.read()
            with open(filename, mode='w', encoding='utf-8') as dest:
                dest.write(text)
