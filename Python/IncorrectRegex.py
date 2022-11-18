import re

for i in range(int(input())):
    test = input()
    try:
        re.compile(test)
        print(True)
    except re.error:
        print(False)