#!/usr/bin/python -u
import sys, argparse
import re
import math
import locale
import itertools
import copy
import random
import logging
logging.basicConfig()
from random import shuffle

parser = argparse.ArgumentParser("")
parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
                    help='input data for parsing')
args = parser.parse_args(sys.argv[1:])

input = args.file.readlines()
input = [line for line in (line.strip() for line in input) if line]


instructions=[]
for line in input:
    d = [re.findall('-?\+?\w+', line)]
    instructions.extend(d)

print len(instructions)

# r={'a':0,'b':0}
r={'a':1,'b':0}
offset=0
while(True):
    try:
        d = instructions[offset]
    except IndexError:
        print "OOPS! Finished"
        break

    if d[0]== 'hlf':
        v = int(r[d[1]])
        r[d[1]]=int( v/2 )
        offset+=1

    elif d[0]=='tpl':
        v = int(r[d[1]])
        r[d[1]]=int( r[d[1]]*3 )
        offset+=1

    elif d[0]=='inc':
        v = int(r[d[1]])
        r[d[1]]=int( r[d[1]]+1 )
        offset+=1

    elif d[0]=='jmp':
        v = int(d[1])
        offset= offset + v

    elif d[0]=='jie':
        vr = int(r[d[1]])
        vi = int(d[-1])
        if vr%2==0: offset = offset + vi
        else: offset+=1

    elif d[0]=='jio':
        vr = int(r[d[1]])
        vi = int(d[-1])
        if vr==1: offset = offset + vi
        else: offset+=1

    else: raise ValueError

    print r, offset