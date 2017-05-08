#!/usr/bin/python -u
import sys, argparse
import re, math
import itertools
from itertools import izip, tee

input = "1113222113"
# input = "1"

def convert(input):
    data = re.findall("("+"|".join([str(x)+"+" for x in range(10)])+")" , input)
    toReturn = ""
    for seq in data:
        toReturn+= str(len(seq)) + seq[0]
    return toReturn

for index in range(50):
    converted = convert(input)
    print index, ":", len(converted)
    # print index, ":", len(converted), input, "->", converted
    input = converted