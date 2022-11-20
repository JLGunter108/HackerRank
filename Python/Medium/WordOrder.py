n = int(input())
myDict = dict()
totals = []

for i in range(0, n):
    keyInput = input()
    if keyInput not in myDict:
        myDict.setdefault(keyInput, 1)
    else:
        myDict[keyInput] += 1

for key in myDict:
    totals.append(str(myDict[key]))    
        
print(len(myDict))
print(" ".join(totals))