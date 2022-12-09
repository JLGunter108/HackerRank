import re

regex_postal_code = re.compile(r"^(([456])(\d{3}))((-?)(\d{4})){3}$")
regex_consecutive_numbers = re.compile(r"((\d)(-?\2){3})")


for _ in range(int(input())):
    string = input()
    if regex_postal_code.match(string) and not regex_consecutive_numbers.search(string):
        print("Valid")
    else:
        print("Invalid")