#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n = len(arr)
    pos = [i for i in arr if i > 0]
    neg = [i for i in arr if i < 0]
    zer = [i for i in arr if i == 0]
    print(len(pos)/n)
    print(len(neg)/n)
    print(len(zer)/n)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
