from fractions import gcd


def f(a, b, n):
    return b // n - (a - 1) // n


A, B, C, D = map(int, input().split())

acc = 0
acc += f(A, B, C)
acc += f(A, B, D)
acc -= f(A, B, C * D // gcd(C, D))
print(B - A + 1 - acc)
