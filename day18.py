#!/usr/bin/python -u
import sys, argparse
import re

parser = argparse.ArgumentParser("")
parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
                    help='input data for parsing')
args = parser.parse_args(sys.argv[1:])

input = args.file.readlines()
# input = """.#.#.#\n...##.\n#....#\n..#...\n#.#..#\n####..""".split('\n')
# input = """##.#.#\n...##.\n#....#\n..#...\n#.#..#\n####.#""".split('\n')
input = [line for line in (line.strip() for line in input) if line]

x_size=len(input)
y_size=len(input)

# True = enabled light
original_grid = [[False for y in range(y_size)] for x in range(x_size)]



def print_frame(grid):
    for row in grid:
        line=''
        for light in row:
            if light:
                line+='#'
            else:
                line+='.'
        print line

print_frame(original_grid)

def next_value(light,count):
    if light:
        if count in [2,3]: return True
        else: return False
    else:
        if count==3: return True
        else: return False

def isAlwaysOn(x, y, edge):
    return (x,y) in [(0,0), (edge, 0), (0, edge), (edge, edge)]

def find_next_value(y,x,grid):
    count=0
    bound = len(grid)
    if isAlwaysOn(x,y, bound-1):
        return True
    else:
        for dy in range(y-1,y+2):
            for dx in range(x-1,x+2):
                if (dy!=y or dx!=x) and \
                   dx>-1 and dy>-1 and \
                   dx<bound and dy<bound:
                    if grid[dy][dx]:
                        count+=1
        return next_value(grid[y][x],count)


def generate_next_frame(grid):
    new_grid = [[False for y in range(y_size)] for x in range(x_size)]
    for y,row in enumerate(grid):
        for x,light in enumerate(row):
            new_grid[y][x]=find_next_value(y,x,grid)
    return new_grid


for y,line in enumerate(input):
    for x,symbol in enumerate(line):
        original_grid[y][x] = True if symbol is '#' else False
        if isAlwaysOn(x,y,x_size-1):
            original_grid[y][x]=True


steps_count=100
frame = original_grid
for i in range(1,steps_count+1):
    frame = generate_next_frame(frame)
    print i," ============"
    # print_frame(frame)
    print sum ( [  x.count(True) for x in frame  ] )
