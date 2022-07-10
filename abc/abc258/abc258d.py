from sys import stdin

readline = stdin.readline

result = 10 ** 20
t = 0
N, X = map(int, readline().split())
for i in range(min(X, N)):
    A, B = map(int, readline().split())
    result = min(result, t + A + B * (X - i))
    t += A + B
print(result)
