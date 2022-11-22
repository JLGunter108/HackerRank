if __name__ == '__main__':
    string = input()
    s = list(string)
    
    t1 = False
    t2 = False
    t3 = False
    t4 = False
    t5 = False
    
    for i in range(len(s)):
        if s[i].isalnum():
            t1 = True
        if s[i].isalpha():
            t2 = True
        if s[i].isdigit():
            t3 = True
        if s[i].islower():
            t4 = True
        if s[i].isupper():
            t5 = True
    
    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)
