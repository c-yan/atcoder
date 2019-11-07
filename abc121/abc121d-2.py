def g(A, n):
    if A == -1:
        return 0
    return A // (2 * n) * n + max(A % (2 * n) - (n - 1), 0)


def f(A, B):
    result = 0
    for i in range(48):
        t = 1 << i
        if (g(B, t) - g(A - 1, t)) % 2 == 1:
            result += t
    return result


A, B = map(int, input().split())

print(f(A, B))
