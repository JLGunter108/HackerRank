import math
import os
import random
import re
import sys

def solve(s):
    s = s.split(" ")
    ns = []
    for i in s:
        ns.append(i.capitalize())
    return(" ".join(ns))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
