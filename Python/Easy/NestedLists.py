if __name__ == '__main__':
    
    names = []
    scores = []
    second_min_students = []
    
    for i in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    
    second_min = sorted(list(set(scores)))[1]
    
    for i in range(len(names)):
        if scores[i] == second_min:
            second_min_students.append(names[i])

    for i in sorted(second_min_students):
        print(i)
