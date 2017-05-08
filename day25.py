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

numbers=list(range(1,22))
n=int(len(numbers)/2)
table = [[0 for y in range(n)] for x in range(n)]
#
#    | 1   2   3   4   5   6   7
# ---+---+---+---+---+---+---+---+
#  1 |  1   3   6  10  15  21  28
#  2 |  2   5   9  14  20  27
#  3 |  4   8  13  19  26
#  4 |  7  12  18  25
#  5 | 11  17  24
#  6 | 16  23
#  7 | 22
# 3,2 = 9
# 3,4 = 18
# 6,1 = 21
# if y==1: x=6; sum([z for z in range(1,x+1)])
# if x==1: y=6; sum([z for z in range(1,y)])+1
# x==3;y==4; 8  sum([z for z in range(1,y)])+1

#    |    1         2         3         4         5         6
# ---+---------+---------+---------+---------+---------+---------+
#  1 | 20151125  18749137  17289845  30943339  10071777  33511524
#  2 | 31916031  21629792  16929656   7726640  15514188   4041754
#  3 | 16080970   8057251   1601130   7981243  11661866  16474243
#  4 | 24592653  32451966  21345942   9380097  10600672  31527494
#  5 |    77061  17552253  28094349   6899651   9250759  31663883
#  6 | 33071741   6796745  25397450  24659492   1534922  27995004


# print "start not example =========="
# code_generator = code_generator(first_value)
# grid = calculate_grid(9000000,code_generator)
# print "\n".join( [str(x) for x in grid] )
#
# x=3;y=3; print grid[y-1][x-1]
# x=3;y=1; print grid[y-1][x-1]
# x=1;y=3; print grid[y-1][x-1]
# x=3019;y=3010; print grid[y-1][x-1]
# x=3010;y=3019; print grid[y-1][x-1]
# print "end ============"

def coordinate_gen(base_coord):
    coord=base_coord
    while True:
        x,y = coord
        coord_before = coord
        if coord==None or not coord or coord==(0,0):
            coord=(1,1)
        elif coord==(1,1):
            coord=(2,1)
        elif y>1 and x==1:
            coord=(y+1,1)
        elif x>1:
            # coord=(x-1,y+1)
            coord=(x-1,y+1)
        else:
            raise ValueError
        yield coord


print "\n".join( [str(x) for x in table] )
print "================="

def code_generator(code):
    next_code = code
    while True:
        yield next_code
        next_code = next_code*multiplier % divider

first_value = 20151125
multiplier = 252533
divider = 33554393

code_gen = code_generator(first_value)

print "========="

def calculate_grid(n,generator):
    coord_gen=coordinate_gen((0, 0))
    table = [[0 for y in range(n)] for x in range(n)]
    i=0
    for code in generator:
        i+=1
        if i>n:break
        x,y=coord_gen.next()
        table[x-1][y-1]=code
    return table

print "start example =========="
numbers=iter(range(1,100))
grid = calculate_grid(30,numbers)
print "\n".join( [str(x) for x in grid] )
print "end ============"

print "start debug =========="
def get_code_for_coord(coord,generator):
     column,row=coord
     to_return=1
     ordinal_number = sum([z for z in range(1,row+column)])-row+1
     # table = [[0 for y in range(n)] for x in range(n)] #
     # coord_gen=coordinate_gen((0, 0)) #
     for i in range(ordinal_number):
         to_return = generator.next()
         # if i>=n:break
         # cx,cy=coord_gen.next() #
     #     table[cx-1][cy-1]=to_return #
     # print "\n".join( [str(x) for x in table] )  #
     return to_return

numbers=iter(range(1,100))
print get_code_for_coord((3,3),numbers) , "==", 13
numbers=iter(range(1,100))
print get_code_for_coord((2,5),numbers) , "==", 17
numbers=iter(range(1,100))
print get_code_for_coord((6,1),numbers) , "==", 21
numbers=iter(range(1,100))
print get_code_for_coord((1,6),numbers) , "==", 16
print "\n\ndebug with real =========="
code_gen = code_generator(first_value)
print get_code_for_coord((3,3),code_gen) , "==", 1601130
code_gen = code_generator(first_value)
print get_code_for_coord((2,5),code_gen) , "==", 17552253
code_gen = code_generator(first_value)
print get_code_for_coord((6,4),code_gen) , "==", 31527494
print "end debug =========="

print "start real =========="
code_gen = code_generator(first_value)
row=3010
column=3019
print get_code_for_coord((column,row),code_gen) , "==", "?"

# x=3019;y=3010; print grid[y-1][x-1]

# To continue, please consult the code grid in the manual.
# Enter the code at row 3010, column 3019.