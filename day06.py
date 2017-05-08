#!/usr/bin/python -u
import sys, argparse
import re

parser = argparse.ArgumentParser("")
parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
                    help='input data for parsing')
args = parser.parse_args(sys.argv[1:])

x_size=1000
y_size=1000

def part_one():
    grid = [[False for y in range(y_size)] for x in range(x_size)]
    for line in args.file.readlines():
        x0, y0, x1, y1 = [int(s) for s in re.findall(r"\d+", line)]
        assert x0<=x1
        assert y0<=y1
        if line.startswith("turn on "):
            for x in range(x0,x1+1):
                for y in range(y0,y1+1):
                    grid[x][y]=True;
        if line.startswith("turn off "):
            for x in range(x0,x1+1):
                for y in range(y0,y1+1):
                    grid[x][y]=False;
        if line.startswith("toggle "):
            for x in range(x0,x1+1):
                for y in range(y0,y1+1):
                    grid[x][y]=not grid[x][y];

    count_lights=0
    for x in range(0,x_size):
        for y in range(0,y_size):
            count_lights+=grid[x][y]
    return count_lights

def part_two():
    grid = [[0 for y in range(y_size)] for x in range(x_size)]
    for line in args.file.readlines():
        x0, y0, x1, y1 = [int(s) for s in re.findall(r"\d+", line)]
        assert x0<=x1
        assert y0<=y1
        if line.startswith("turn on "):
            for x in range(x0,x1+1):
                for y in range(y0,y1+1):
                    grid[x][y]+=1
        if line.startswith("turn off "):
            for x in range(x0,x1+1):
                for y in range(y0,y1+1):
                    value = grid[x][y]
                    grid[x][y] = 0 if value==0 else value-1
                    assert grid[x][y] >= 0
        if line.startswith("toggle "):
            for x in range(x0,x1+1):
                for y in range(y0,y1+1):
                    grid[x][y]+=2

    total_brightness=0
    for x in range(0,x_size):
        for y in range(0,y_size):
            total_brightness+=grid[x][y]
    return total_brightness

# print part_one()
print part_two()