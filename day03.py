#!/usr/bin/python -u
import sys, argparse

parser = argparse.ArgumentParser("")
parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
                    help='input data for parsing')
args = parser.parse_args(sys.argv[1:])
x=y=0
move={'^':(x,y+1),'v':(x,y-1), '>':(x+1,y), '<':(x-1,y)}
robosanta_xy=santa_xy=only_santa_xy=start=(0,0)
only_santa_houses={start:None}
robo_and_santa_houses={start:None}

for index,symbol in enumerate(args.file.read()):
    movement=move[symbol]
    only_santa_xy=tuple(map(sum, zip( movement,only_santa_xy)))
    only_santa_houses[only_santa_xy]=None
    if index % 2==0:
            santa_xy=tuple(map(sum, zip( movement,santa_xy)))
            robo_and_santa_houses[santa_xy]=None
    else:
            robosanta_xy=tuple(map(sum, zip( movement,robosanta_xy)))
            robo_and_santa_houses[robosanta_xy]=None
print len(only_santa_houses)
print len(robo_and_santa_houses)


