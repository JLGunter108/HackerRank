import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

if n < 2:
    print("Weird")
for i in range(2,6):
    if i == n:
        if i % 2 != 0:
            print("Weird")
        else:
            print("Not Weird")
for i in range(6,21):
    if i == n:
        print("Weird")
for i in range(21,101):
    if i == n:
        if i % 2 != 0:
            print("Weird")
        else:
            print("Not Weird")