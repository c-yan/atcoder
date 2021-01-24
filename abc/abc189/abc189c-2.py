from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

N, *A = map(int, open(0).read().split())


def f(a):
    n = len(a)
    m = min(a)
    result = m * n
    i = 0
    for j in range(n):
        if a[j] != m:
            continue
        if i < j:
            result = max(result, f(a[i:j]))
        i = j + 1
    if i < n:
        result = max(result, f(a[i:n]))
    return result


print(f(A))
