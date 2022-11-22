def count_substring(s, sS):
    k = 0
    i = 0
    
    while i < len(s): 
        if s[i:i+len(sS):] == sS:
            k += 1
        i+=1
    return k

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)