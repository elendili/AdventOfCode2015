#!/usr/bin/python -u
import os, re, sys, argparse

parser = argparse.ArgumentParser("")
parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin, help='input data for parsing')
args = parser.parse_args(sys.argv[1:])

floor_num = 0
char_num=0
for char in args.file.read():
    char_num+=1
    if char == "(":
        floor_num += 1
    elif char == ")":
        floor_num -= 1
    if floor_num == -1:
        print "Santa enter the basement on char: ", char_num

print floor_num
# Answer: 280