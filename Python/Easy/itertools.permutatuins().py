import itertools

string, k = input().split()
k = int(k)
list = sorted(list(itertools.permutations(string, k)))

for i in list:
    print("".join(i))