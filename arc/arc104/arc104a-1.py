A, B = map(int, input().split())

for X in range(-200, 200):
    for Y in range(-200, 200):
        if X + Y == A and X - Y == B:
            print(X, Y)
            exit()
