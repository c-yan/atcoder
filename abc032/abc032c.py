# しゃくとり法
from sys import exit

N, K = map(int, input().split())
s = [int(input()) for _ in range(N)]

if any(i == 0 for i in s):
    print(N)
    exit()

if K == 0:
    print(0)
    exit()

result = 0
t = 1
left = 0
for right in range(N):
    t *= s[right]
    if t > K:
        if right - left > result:
            result = right - left
        for j in range(left, right + 1):
            t //= s[j]
            if t <= K:
                left = j + 1
                break
if N - left > result:
    result = N - left
print(result)
