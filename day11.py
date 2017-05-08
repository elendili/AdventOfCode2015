#!/usr/bin/python -u
import sys, string
import re, math
import itertools
from itertools import izip, tee

alphabet = list(string.ascii_lowercase)


def letter_gen(letter):
    index = alphabet.index(letter)
    index = index if index + 1 < len(alphabet) else -1
    new_letter = alphabet[index + 1]
    return new_letter


def free_from_spec_symbol(word):
    indexes = [m.start() for m in re.finditer('i|o|l', word)]
    if len(indexes) > 0:
        index = indexes[0]
        word = word[:index] + letter_gen(word[index]) + 'a' * (len(word) - index-1)
    return word

def increase_sequence(word):
    if len(word) > 0:
        word = free_from_spec_symbol(word)
        letter = letter_gen(word[-1])
        if letter == 'a':
            string = increase_sequence(word[:-1])
        else:
            string = word[:-1]
        return string + letter
    return ''


def contains_three_straight(word):
    for index, letter in enumerate(word):
        if index <= len(word) - 3 \
                and word[index + 1] == letter_gen(letter) \
                and word[index + 2] == letter_gen(word[index + 1]) \
                and word[index:index + 3] not in ['zab', 'yza']:
            return True
    return False


def contains_2_pairs(word):
    return len([m.group(0) for m in re.finditer(r"(.)\1+", word) if len(m.group(0)) == 2]) >= 2


def doesnt_contain_specific_symbols(word):
    return not bool(re.findall('i|o|l', word))


def is_acceptable(word):
    return  doesnt_contain_specific_symbols(word) \
        and \
        contains_2_pairs(word) \
        and \
        contains_three_straight(word)


def search_new_password(word):
    new_pass = increase_sequence(word)
    while (not is_acceptable(new_pass)):
        # print new_pass
        new_pass = increase_sequence(new_pass)
    return new_pass


print search_new_password('cqjxjnds')
print search_new_password('cqjxxyzz')
