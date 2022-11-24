import itertools

s, k = input().split()

ls = []
for i in range(int(k)):
    ls += itertools.combinations(sorted(s), i+1)

for item in ls:
    print("".join(item))