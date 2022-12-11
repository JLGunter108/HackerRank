N = int(input())
A = set(map(int, input().split()))

for _ in range(int(input())):
    cmd, L = input().split()
    NS = set(map(int, input().split()))
    exec(f'A.{cmd}({NS})')
    
print(sum(A))