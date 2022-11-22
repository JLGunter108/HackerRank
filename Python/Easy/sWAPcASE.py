def swap_case(s):
    ns = ""
    for i in s:
        if i.islower():
            ns += i.upper()
        elif i.isupper():
            ns += i.lower()
        else:
            ns += i
    return ns

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)