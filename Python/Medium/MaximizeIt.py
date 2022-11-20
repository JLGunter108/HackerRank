from itertools import product
#https://docs.python.org/3/library/itertools.html#itertools.product

K,M = list(map(int, input().split()))

#Create list of lists of squares from input, slicing N from list
nums = [[int(number)**2 for number in input().split()[1:]] for group in range(K)]
#Iterate through cartesian product of nums and find max of sum of results mod M
maximum = max(sum(result)%M for result in product(*nums))

print(maximum)

#New Concepts: List Comprehension && Cartesian Products