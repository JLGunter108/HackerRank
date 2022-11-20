def stack(blocks):
    while len(blocks) > 2:
        if blocks[0] >= blocks[-1] and blocks[0] >= blocks[2]:
            blocks.pop(0)
        elif blocks[-1] >= blocks[0] and blocks[-1] >= blocks[-2]:
            blocks.pop()
        else:
            return "No"
    return("Yes")
            

for tests in range(int(input())):
    total, blocks = int(input()), list(map(int, input().split()))
    print(stack(blocks))
