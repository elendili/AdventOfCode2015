#!/usr/bin/python -u

import os, re, sys, argparse, json

parser = argparse.ArgumentParser("")
parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
                    help='input data for parsing')
args = parser.parse_args(sys.argv[1:])

# input = '{"a":1,"b":{"bb":"red", "bc":11 },"c":[5,7,"red"]}'
input = args.file.readlines()[0]

def find_number(obj):
    sum = 0
    if type(obj) == int:
        return obj
    elif type(obj) == str or type(obj) == unicode:
        return 0
    elif type(obj) == dict:
        if 'red' in obj.values():
            return 0
        else:
            for value in obj.values():
                sum += find_number(value)
    elif type(obj) == list:
        for element in obj:
            sum += find_number(element)
    else:
        raise TypeError
    return sum


line = input
data = [int(d) for d in re.findall(r'-?\d+', line)]
print reduce(lambda x, y: x + y, data,0)

print '=== second part ===='
jdata = json.loads(line)
print find_number(jdata)
# print json.dumps(jdata, sort_keys=True, indent=4, separators=(',', ': '))
