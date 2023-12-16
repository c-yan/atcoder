from collections import Counter
from sys import stdin

readline = stdin.readline

R, C, K = map(int, input().split())
N = int(input())
rc = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]

a = [0] * R
b = [0] * C
for r, c in rc:
    a[r] += 1
    b[c] += 1

ca = Counter(a)
cb = Counter(b)
result = 0
for i in range(K + 1):
    result += ca[i] * cb[K - i]
for r, c in rc:
    if a[r] + b[c] == K:
        result -= 1
    elif a[r] + b[c] == K + 1:
        result += 1
print(result)
