if __name__ == '__main__':
    student_marks = {}
    for i in range(int(input())):
        name, *marks = input().split()
        scores = list(map(float, marks))
        student_marks[name] = scores
    student = input()
    
    print(format(sum(student_marks[student])/len(student_marks[student]), '.2f'))