cube = lambda x: x**3

def fibonacci(n):
    results = []
    for i in range(n):
        if i == 0:
            results.append(0)
        elif i < 2:
            results.append(1)
        else:
            results.append((results[i-1])+(results[i-2]))
    return results

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))