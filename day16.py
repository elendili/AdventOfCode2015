#!/usr/bin/python -u

import os, re, sys, argparse, json

parser = argparse.ArgumentParser("")
parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
                    help='input data for parsing')
args = parser.parse_args(sys.argv[1:])

properties_raw= """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""
data = re.findall('\w+',properties_raw)
i = iter(data)
properties_dict=dict(zip(i, i))

input = args.file.readlines()
aunts=[]
for index,line in enumerate(input):
    data = re.findall('\w+',line)
    i = iter(data)
    aunt_dict = dict(zip(i, i))
    aunts.append(aunt_dict)

def isDifferent(dict1,dict2):
    return bool ( [k for k in set(dict1.keys()) & set(dict2.keys()) if dict1[k]!=dict2[k]] )

def isSuitable(dict1,properties):
    common_keys =  set(dict1.keys()) & set(properties.keys())
    toReturn = True
    for k in common_keys:
        if k in ['cats','trees']:
            toReturn &= dict1[k] > properties[k]
        elif k in ['pomeranians','goldfish']:
            toReturn &= dict1[k] < properties[k]
        else:
            toReturn &= dict1[k] == properties[k]
    return toReturn

isDifferent(aunts[0],properties_dict)

filtered_aunts_1 = filter(lambda d: not isDifferent(d,properties_dict),aunts)
filtered_aunts_2 = filter(lambda d: isSuitable(d,properties_dict),aunts)

print len(filtered_aunts_1)
print filtered_aunts_1

print len(filtered_aunts_2)
print filtered_aunts_2
