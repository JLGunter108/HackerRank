#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    minArr = sorted(arr)
    minArr.pop()
    maxArr = sorted(arr)
    maxArr.pop(0)
    print(sum(minArr),sum(maxArr))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
