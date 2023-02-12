n, nL = int(input()), set(map(int, input().split()))
m, mL = int(input()), set(map(int, input().split()))

print(len(nL.difference(mL)))