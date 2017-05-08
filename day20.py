#!/usr/bin/python -u
import sys, argparse
import re
import math
import locale
from random import shuffle


# y = 1*10 +2*10 +3*10 +4*10 +5*10 = 150
# S5 = (10 + (5-1)*10  /  2 ) * 5 = 125
# S5 = (10 + 5*10  /  2 ) * 5 = 30*5=150
# S4 = ((10 + 4*10) / 2 )* 4 = 100
# S4 = ((10 + 4*10) / 2 )* 4 = 100
# ((10 + x*10) / 2 )* x = 100
# ((10 + x*10))* x = 100*2
# (x*10 + x**2*10 = 100*2
# x*10 + x**2*10 - 2*100 = 0
# x**2*10 + x*10 - 2*100 = 0
# D = b**2 - 4ac
# D = 10**2 - 4 * 10 * (- 2 * 100)
# D = 100 - 40 * (- 2 * 100)
# D = 100 + 80 * 100 = 8100
# D = d**2 - 4 * 10 * (- 2 * 100)

locale.setlocale(locale.LC_ALL, 'en_US')

def num(num):
    return locale.format("%d", num, grouping=True)

def factors(n):
    return sorted(set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0))))



input = 29000000
# input = 50000
print input
from_one_elf=11


for house in range(1,input):
    all_factors_list = factors(house)
    factors_list_filtered = [d for d in all_factors_list if (house/d<=50)]
    gfh = sum(factors_list_filtered)*from_one_elf
    if (house%len(all_factors_list)>1000 ):
        print num(house), '; all factors:', len(all_factors_list), 'filtered factors:', len(factors_list_filtered),'; gifts:', num(gfh)
    if gfh>=input:
        print "house",num(house),"will gets", num(gfh)
        break