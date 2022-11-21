import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrix_string = ""

j = 0
while j < m:
    for i in range(n):
        matrix_string += str(matrix[i][j])
    j += 1
        
print(re.sub(r"(?<=\w)(\W+)(?=\w)", " ", matrix_string))

#spent more time than i should have (about 1.25 hours) before i realized it was basically the same as the regex substitution problem.