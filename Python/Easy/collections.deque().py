from collections import deque

d = deque()

for i in range(int(input())):
    cmd, *args = input().split()
    args = tuple(args)
    exec(f'd.{cmd}{args}')
    
print(' '.join(d))