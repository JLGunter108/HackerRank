def merge_the_tools(string, k):
    temp = ""
    for i in range(0, len(string)):
        if (i+1) % k == 0:
            temp += string[i]
            print("".join(set(temp)))
            temp = ""
        else:
            temp += string[i]

        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)