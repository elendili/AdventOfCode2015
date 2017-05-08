#!/usr/bin/python -u
import sys, argparse
import re, math
import itertools
from itertools import izip, tee

parser = argparse.ArgumentParser("")
parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
                    help='input data for parsing')
args = parser.parse_args(sys.argv[1:])

# test_input = """"coykr\x57luiy""".split('\n')
input = args.file.readlines()
# input = test_input
stripped_input = [line for line in (line.strip() for line in input) if line]
distances={}
cities=set()
for index,line in enumerate(input):
    # if index>8:break
    data = [z for z in re.findall('\w+',line) if z != 'to']
    cities |= set(data[:2])
    distances[(data[0], data[1])]=distances[(data[1], data[0])]=int(data[-1])

    # print index, "\t", data, "\t", cities, "\t", distances

permuta_list = list(itertools.permutations(cities))

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

print "===="
known_routes={}
known_short_route_distance=9000000
for route in permuta_list:
    route_distance=0
    route_exist_and_minimal=True
    for v, w in pairwise(list(route)):
        if distances.has_key((v,w)):
            route_distance+=distances[(v,w)]
        else:
            route_exist_and_minimal=False
            break
        # if route_distance > known_short_route_distance:
        #     route_exist_and_minimal=False
        #     break
    # known_short_route_distance = route_distance if route_distance<known_short_route_distance else known_short_route_distance

    if route_exist_and_minimal:
        known_routes[route]=route_distance

print "=== Existing routes: "
# for route, distance in known_routes.iteritems():
#     print route, distance
print min(known_routes.values())
print max(known_routes.values())