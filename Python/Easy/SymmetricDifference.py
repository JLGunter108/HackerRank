l1 =  int(input())
m = set(map(int, input().split()))
l2 = int(input())
n = set(map(int, input().split()))

a = m.difference(n)
b = n.difference(m)

a.update(b)

for i in sorted(a):
    print(i)
