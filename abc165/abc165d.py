from math import floor

A, B, N = map(int, input().split())


def f(x):
    return floor(A * x / B) - A * floor(x / B)


result = 0
for x in range(min(A + 1, N + 1)):
    result = max(result, f(x))

if B > A:
    for i in range(10 ** 20):
        x = (i * B + A - 1) // A
        if x > N:
            break
        result = max(result, f(x))

print(result)
