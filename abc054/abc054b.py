N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

for i in range(N - M + 1):
    for j in range(N - M + 1):
        ok = True
        for k in range(M):
            for l in range(M):
                if A[i + k][j + l] != B[k][l]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            print('Yes')
            exit()
print('No')
