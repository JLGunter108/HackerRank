n = int(input())
words = []
score = 0

for i in input().split():
    words.append(str(i))
    
for word in words:
    count = 0
    
    for letter in word:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
            count += 1
    
    if count % 2 == 0:
        score += 2
    else: 
        score += 1
    
print(score)