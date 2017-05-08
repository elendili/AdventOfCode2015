#!/usr/bin/python -u
import sys, argparse
import re, math

parser = argparse.ArgumentParser("")
parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
                    help='input data for parsing')
args = parser.parse_args(sys.argv[1:])

# test_input = """"coykr\x57luiy""".split('\n')
input = args.file.readlines()
# input = test_input
# find all wires
diff_total_1=0
diff_total_2=0
stripped_input = [line for line in (line.strip() for line in input) if line]
for index,line in enumerate(stripped_input):
    # if index>0:break
    evaluated_line = eval(line)
    represent=repr(line).replace("\"",r"\"")

    eval_len = len(evaluated_line)
    raw_len = len(line)
    repr_len = len(represent)
    diff_1 = raw_len - eval_len
    diff_total_1 += diff_1

    diff_2 =  repr_len - raw_len
    diff_total_2 += diff_2

    print index, "|", line, " c:",  raw_len, "    ", evaluated_line, "c:",  eval_len, " diff:", diff_1, "diff_total:", diff_total_1
    print index, "|", line, " c:",  raw_len, "    ", represent, "c:",  repr_len, " diff:", diff_2, "diff_total:", diff_total_2

print diff_total_1
print diff_total_2