#!/usr/bin/python -u
import sys, argparse
import re, math

test_input = """x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
i AND h -> q
NOT x -> h
NOT y -> i
123 -> x
456 -> y
z -> u""".split('\n')
parser = argparse.ArgumentParser("")
parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
                    help='input data for parsing')
args = parser.parse_args(sys.argv[1:])


def convert(token, values):
    if (token.isdigit()):
        val = int(token)
        values[val] = val
        return val
    else:
        return token


def eval_tokens(tokens, values):
    value = -1
    if len(tokens) == 2:
        if tokens[0] in values:
            value = values[tokens[0]]
        else:
            return False
    elif "NOT" in tokens:
        if tokens[1] in values:
            _not = ~values[tokens[1]]
            value = 65536 + _not if _not < 0 else _not
        else:
            return False
    elif len(tokens) == 4:
        if ((tokens[0] in values) and (tokens[2] in values)):
            if "RSHIFT" in tokens:
                value = values[tokens[0]] >> values[tokens[2]]
            elif "LSHIFT" in tokens:
                value = values[tokens[0]] << values[tokens[2]]
            elif "OR" in tokens:
                value = values[tokens[0]] | values[tokens[2]]
            elif "AND" in tokens:
                value = values[tokens[0]] & values[tokens[2]]
        else:
            return False

    assert 0 <= value <= 65535
    ok = tokens[-1]
    values[ok] = value
    return True


wires = {}
values = {}
input = args.file.readlines()
# input = test_input
all_wires = set()
# find all wires
for line in input:
    all_wires = all_wires.union([wire for wire in re.findall(r"[a-z]+", line)])
print all_wires

result_dict = dict()
before_diff = 2
after_diff = 1
# define some tokens
while (after_diff > 0):
    before_diff = len(all_wires.difference(result_dict))
    for line in input:
        tokens = [convert(token, values) for token in re.findall(r"\w+", line)]
        eval_tokens(tokens, values)
    result_dict = dict((key, value) for key, value in values.iteritems() if type(key) == str)
    after_diff = len(all_wires.difference(result_dict))
    if after_diff == before_diff: raise Exception("Undefined wire!")
    print result_dict
print result_dict['a']
#     d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456
