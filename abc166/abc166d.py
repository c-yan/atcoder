X = int(input())

for A in range(1000):
    for B in range(-1000, 1000):
        if A ** 5 - B ** 5 == X:
            print(A, B)
            exit()
