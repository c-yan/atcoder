def g(A):
    t = ((A + 1) // 2) % 2  # 任意の偶数 n について n ^ (n + 1) == 1
    if A % 2 == 0:
        return A ^ t
    return t


def f(A, B):
    return g(A - 1) ^ g(B)


A, B = map(int, input().split())

print(f(A, B))
