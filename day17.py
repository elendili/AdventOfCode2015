#!/usr/bin/python -u

import os, re, sys, argparse, json, itertools

parser = argparse.ArgumentParser("")
parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
                    help='input data for parsing')
args = parser.parse_args(sys.argv[1:])


input = args.file.readlines()
data=[]
for index,line in enumerate(input):
    data += [int(d) for d in re.findall('\w+',line)]

possible_combs = [list(itertools.combinations(data, i)) for i in range(1, len(data) + 1)]
accepptable_combs1=list()
accepptable_combs2=list()
mini_count=9999
for combs1 in possible_combs:
    for comb in combs1:
        if sum(comb)==150:
            accepptable_combs1.append(comb)
            mini_count= len(comb) if len(comb)< mini_count else mini_count
            if len(comb)==mini_count:
                accepptable_combs2.append(comb)

print accepptable_combs1
print len(accepptable_combs1)
print accepptable_combs2
print len(accepptable_combs2)