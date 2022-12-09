from collections import Counter

shoes = int(input())
stock = Counter(list(map(int, input().split())))
customers = int(input())
sale = 0 

for _ in range(customers):
    size, price = map(int, input().split())
    if size in stock and not stock[size] == 0:
        stock[size] -= 1
        sale += price
    
print(sale)