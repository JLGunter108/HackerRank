#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    s = s.split(":")
    if s[2].endswith("PM") and int(s[0])<12:
        s[0] = str(int(s[0]) + 12)
    if s[0] == "24":
        s[0] = "00"
    if s[0] == "12" and s[2].endswith("AM"):
        s[0] = "00"
    s[2] = s[2][:2]
    s = ":".join(map(str, s))
    return(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
