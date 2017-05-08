#!/usr/bin/python -u
import sys, argparse
import hashlib

# m = hashlib.md5()
# m.update("abcdef609043")
# print m.hexdigest()
# m = hashlib.md5()
# m.update("pqrstuv1048970")
# print m.hexdigest()

for i in range(0, 10000000):
    m = hashlib.md5()
    m.update("bgvyzdsv"+str(i))
    hd = m.hexdigest()
    # print hd, ':::', '0'*5
    if hd[0:6]=='0'*6:
        print hd, ':::', i
        break
