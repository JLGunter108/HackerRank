import itertools

A = map(int, input().strip().split())
B = map(int, input().strip().split())
output = ""

for i in itertools.product(A,B):
    output += str(i) + " "
    
print(output)