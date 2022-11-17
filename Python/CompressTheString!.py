import itertools

S = input()
NS = ""
key_func = lambda x: x[0]
  
for key, group in itertools.groupby(S, key_func):
    NS += ("(" + str(list(group).count(key)) + ", " + str(key) + ") ")
    
print(NS)