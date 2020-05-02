N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(Q)]

m = M - 1


def f(s):
    if len(s) == N:
        return [s]
    result = []
    if s == '':
        r = 0
    else:
        r = int(s[-1])
    for i in range(r, m + 1):
        result.extend(f(s + str(i)))
    return result


result = 0
V = f('')
for s in V:
    A = [int(c) + 1 for c in s]
    t = 0
    for a, b, c, d in abcd:
        if A[b - 1] - A[a - 1] == c:
            t += d
    result = max(result, t)
print(result)
