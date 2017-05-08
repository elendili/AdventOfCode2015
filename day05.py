#!/usr/bin/python -u
import sys, argparse
import re

parser = argparse.ArgumentParser("")
parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
                    help='input data for parsing')
args = parser.parse_args(sys.argv[1:])


def contains_3_vowels(word):
    count = len(re.findall(r'a|e|i|o|u', word))
    return count >= 3


def one_letter_twice(word):
    count = len(re.findall(r'(\w)\1+', word))
    return count > 0


def not_contains_specific_strings(word):
    count = len(re.findall(r'ab|cd|pq|xy', word))
    return count == 0


def contains_pair_of_two_letters(word):
    count = len(re.findall(r'(\w{2}).*\1', word))
    return count > 0


def contains_letter_repeats_with_one_letter_between(word):
    count = len(re.findall(r'(\w).\1', word))
    return count > 0


nice_count_1 = 0
nice_count_2 = 0

for line in args.file.readlines():
    if contains_3_vowels(line) and one_letter_twice(line) and not_contains_specific_strings(line):
        nice_count_1 += 1
    if contains_pair_of_two_letters(line) and contains_letter_repeats_with_one_letter_between(line):
        nice_count_2 += 1

print nice_count_1
print nice_count_2
