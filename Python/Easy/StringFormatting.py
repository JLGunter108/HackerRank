def print_formatted(n):
    w = len(format(n, 'b'))
    for i in range(1, n+1):
        num = str(i)
        o = str(format(i, 'o'))
        x = str(format(i, 'X'))
        b = str(format(i, "b"))
        print(num.rjust(w), o.rjust(w), x.rjust(w), b.rjust(w))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)