def minion_game(string):
    vowels = ["A", "E", "I", "O", "U"]
    cons, vows = 0, 0
    
    for i in range (len(string)):
        if string[i] in vowels:
            vows += len(string)-i
        else:
            cons += len(string)-i

    if cons > vows:
        print("Stuart", cons)
    elif vows > cons:
        print("Kevin", vows)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)