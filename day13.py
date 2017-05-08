#!/usr/bin/python -u
import sys, argparse
import re, math
import itertools
from itertools import izip, tee

parser = argparse.ArgumentParser("")
parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
                    help='input data for parsing')
args = parser.parse_args(sys.argv[1:])

input = """"Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.""".split('\n')
input = args.file.readlines()

stripped_input = [line for line in (line.strip() for line in input) if line]
relations={}
peoples=set()
for index,line in enumerate(input):
    # if index>8:break
    line = str(line).replace('happiness units by sitting next to ','').replace('would','')\
        .replace('lose ','-').replace('gain ','')
    data = [z for z in re.findall('-?\w+',line) ]
    peoples.add(data[-1])
    relations[(data[0], data[-1])]=int(data[1])

permutations_list = list(itertools.permutations(peoples))

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

print "===="

def add_first_to_the_last(permutations_list):
    for i,permutation in enumerate(permutations_list):
        permutation = permutation + (permutation[0],)
        permutations_list[i]=permutation
    return permutations_list

def find_permutations_values(relations, permutations_list):
    known_permutations={}
    for permutation in permutations_list:
        permutation_happines=0
        for v, w in pairwise(list(permutation)):
            if relations.has_key((v, w)) and relations.has_key((w, v)):
                permutation_happines+=relations[(v, w)]
                permutation_happines+=relations[(w, v)]
        known_permutations[permutation]=permutation_happines
    return known_permutations

print "=== happiness measurement: "
# for route, distance in known_routes.iteritems():
#     print route, distance
permutations = find_permutations_values(relations, add_first_to_the_last(permutations_list))
print min(permutations.values())
print max(permutations.values())

print "=== happiness measurement with me: "
peoples.add('Me')
permutations_list = list(itertools.permutations(peoples))
permutations_with_me = find_permutations_values(relations, add_first_to_the_last(permutations_list))
print min(permutations_with_me.values())
print max(permutations_with_me.values())