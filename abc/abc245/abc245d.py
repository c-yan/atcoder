N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

B = [None] * (M + 1)


def f(b, c):
    x = C[c]
    if A[c - b] == 0:
        return None
    for i in range(min(c, N) + 1):
        if A[i] == 0:
            continue
        if c - i == b:
            continue
        if B[c - i] is None:
            return None
        x -= A[i] * B[c - i]
    return x // A[c - b]


for i in range(M + 1):
    for j in range(M + 1):
        if B[j] is not None:
            continue
        for k in range(j, N + M + 1):
            x = f(j, k)
            if x is not None:
                B[j] = x
                break
        if B[j] is not None:
            break
print(*B)
