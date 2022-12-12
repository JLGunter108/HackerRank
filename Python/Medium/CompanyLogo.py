#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()

letters = dict()

for i in s:
    if i not in letters:
        letters[i] = 1
    else:
        letters[i] += 1

count = 0

for i in sorted(letters.values(), reverse=True):
    for key, value in sorted(letters.items()):
        if value == i:
            if count == 3:
                break
            else:
                print(key, value)
                letters.pop(key)
                count+=1