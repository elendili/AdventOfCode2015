#!/usr/bin/python -u
import sys, argparse
import re
import math
import locale
import itertools
import copy
import random
import logging
from operator import mul
logging.basicConfig()
from random import shuffle

parser = argparse.ArgumentParser("")
parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
                    help='input data for parsing')
args = parser.parse_args(sys.argv[1:])

input = args.file.readlines()
input = [line for line in (line.strip() for line in input) if line]


base_packages=[]
for line in input:
    d = int(line.strip())
    base_packages.append(d)




n = 4
print len(base_packages), n
place_sum= sum(base_packages) / n
base_places=[[] for x in range(n)]
packages = copy.deepcopy(base_packages)


def find_combinations(packages,place_sum):
    possible_combinations=set()
    for perm in itertools.combinations(packages,5):
        if sum(perm)==place_sum:
            possible_combinations.add(tuple(sorted(perm,reverse=True)))
    return possible_combinations

possible_combinations = find_combinations(packages,place_sum)
print possible_combinations

total_min_qe=10000000000
for t in possible_combinations:
        min_qe_v=reduce(mul, t, 1)
        if min_qe_v<total_min_qe:
            total_min_qe=min_qe_v

print "stop:",total_min_qe


# for package in sorted(packages,reverse=True):
#     sorted(places, key=sum)[0].append(package)
#
# print places
# print  [sum(x) for x in places]
places = copy.deepcopy(base_places)
all_solutions=[]
minimum_len_solutions=[]
minimum_qe_solutions=[]
total_min_len=10
total_min_qe=  100000000000
#
# for i  in xrange(1000000000):
#     places = copy.deepcopy(base_places)
#     shuffle(packages)
#     for package in packages:
#         sorted(places, key=sum)[0].append(package)
#     sum_places=[sum(x) for x in places]
#     if all(x == sum_places[0] for x in sum_places ):
#         all_solutions.append(places)
#         min_len_v=min([len(x) for x in places])
#         if min_len_v < total_min_len:
#             minimum_len_solutions=[]
#             minimum_len_solutions.append(places)
#             minimum_qe_solutions=[]
#             minimum_qe_solutions.append(places)
#             total_min_len = min_len_v
#             print "min qe:",total_min_qe," min len:", total_min_len,
#         elif total_min_len==min_len_v:
#             minimum_len_solutions.append(places)
#             t=[reduce(mul, x, 1) for x in places if len(x)==min_len_v]
#             min_qe_v = min(t)
#             if min_qe_v<total_min_qe:
#                 total_min_qe=min_qe_v
#                 minimum_qe_solutions=[]
#                 minimum_qe_solutions.append(places)
#                 print "min qe:",total_min_qe," min len:", total_min_len,
#             elif min_qe_v==total_min_qe:
#                 minimum_qe_solutions.append(places)
#
#
# # first answer: 11266889531
# #                 236283339
# #                 80048183  5
#                   77387711