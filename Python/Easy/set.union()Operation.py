n, s1 = int(input()), set(input().split())
m, s2 = int(input()), set(input().split())

s3 = s1 | s2

print(len(s3))