N = int(input())

for A in range(1, 38):
    for B in range(1, 26):
        if 3 ** A + 5 ** B == N:
            print(A, B)
            exit()
print(-1)
