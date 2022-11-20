inputs = list(map(int, input().split()))
array = list(map(int, input().split()))
likes = set(map(int, input().split()))
dislikes = set(map(int, input().split()))
happiness = 0

for i in array:
    if i in likes:
        happiness += 1
    elif i in dislikes:
        happiness -= 1
    
print(happiness)