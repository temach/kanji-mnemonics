#!/usr/bin/env python3
import argparse
import re
from pprint import pprint

parser = argparse.ArgumentParser(description='Return words from dict that are ordered by frequency')
parser.add_argument('dictionary', metavar='D', type=str, help='Dict file e.g. /usr/share/dict/words or english-dict-small.txt')
parser.add_argument('frequency', metavar='F', type=str, help='File with words by frequency e.g. google-10000-english-by-frequency.txt')
parser.add_argument('regex', metavar='R', type=str, help='Regex to execute on dictonary file')
args = parser.parse_args()
print(args)

tmp = []
with open(args.dictionary) as f:
    tmp = f.readlines()
content = []
for x in tmp:
    x = x.strip()
    if len(x) > 2 and x[-2:] == "'s":
        continue
    content.append(x)
# print(len(content))

pattern = re.compile(args.regex)
# print(pattern)
matched = [line for line in content if pattern.match(line)]
# print(len(matched))

fcontent = []
with open(args.frequency) as f:
    fcontent = f.readlines()
fcontent = [x.strip() for x in fcontent] 

matched_freq = []
for l in matched:
    try:
        freq = fcontent.index(l)
    except:
        freq = 20000
    matched_freq.append( (freq, l) )

fin = sorted(matched_freq, key=lambda x: x[0], reverse=False)
pprint(fin)
