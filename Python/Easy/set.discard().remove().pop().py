irrelevant = input()
s = set(map(int, input().split()))

for command in range(int(input())):
    cmd, *args = input().split()
    args = tuple(map(int, args))
    exec(f's.{cmd}{args}')

print(sum(s))
