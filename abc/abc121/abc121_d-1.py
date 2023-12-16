def h(A, n):
    if A == -1:
        return 0
    return A // (2 * n) * n + max(A % (2 * n) - (n - 1), 0)


def g(A):
    result = 0
    for i in range(48):
        t = 1 << i
        if h(A, t) % 2 == 1:
            result += t
    return result


def f(A, B):
    return g(A - 1) ^ g(B)


A, B = map(int, input().split())

print(f(A, B))
