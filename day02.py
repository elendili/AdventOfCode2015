#!/usr/bin/python -u

import os, re, sys, argparse

parser = argparse.ArgumentParser("")
parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
                    help='input data for parsing')
args = parser.parse_args(sys.argv[1:])

total_ribbon = 0
total_paper = 0
char_num=0
for line in args.file.readlines():
    l,w,h = [int(s) for s in line.split('x')]
    base_paper=2*l*w + 2*w*h + 2*h*l
    slack_paper=min(l*w, w*h, h*l)
    wrap_ribbon = min(2*l+2*w, 2*w+2*h, 2*h+2*l)
    bow_ribbon=l*w*h
    paper_for_box=base_paper+slack_paper
    ribbon_for_box=wrap_ribbon+bow_ribbon
    print l, '*', w, '*', h, '-> paper: ', slack_paper,'+', base_paper, '=', paper_for_box,\
        "-> ribbon: ", wrap_ribbon, '+', bow_ribbon, '=', ribbon_for_box
    total_paper+=paper_for_box
    total_ribbon+=ribbon_for_box

print "total paper square =",  total_paper
print "total ribbon length=", total_ribbon