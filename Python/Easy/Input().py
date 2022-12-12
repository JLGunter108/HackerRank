x, k = map(int, input().split())
P = input()

for _ in P:
    if _ == "x":
        _ = x

print("True" if eval(P) == k else "False")