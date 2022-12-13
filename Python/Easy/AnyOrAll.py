N, arr = int(input()), list(map(int, input().split()))
#Prompt challenged 3 lines or less
print("True" if all((i > 0) for i in arr) and any((str(i) == str(i)[::-1]) for i in arr) else "False")