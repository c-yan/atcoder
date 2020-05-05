N, M = map(int, input().split())

for i in range(1, M + 1):
    if i % 2 == 1:
        j = (i - 1) // 2
        print(1 + j, M + 1 - j)
    else:
        j = (i - 2) // 2
        print(M + 2 + j, 2 * M + 1 - j)
