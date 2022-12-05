s = input()

sorting = [i for i in sorted(s) if i.islower()]+[i for i in sorted(s) if i.isupper()]+[i for i in sorted(s) if i.isnumeric() if int(i)%2 != 0]+[i for i in sorted(s) if i.isnumeric() if int(i)%2 == 0]

print("".join(sorting))

#https://peps.python.org/pep-0308/