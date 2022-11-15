q = int(input())

for i in range(q):
    o, n = input().split()
    if o == "odd":
        for i in range(int(n)*2):
            if i % 2 != 0:
                print(i)
    else:
        for i in range(int(n)*2):
            if i % 2 == 0:
                print(i)            