# 累積和
from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

for x in [A, B, C]:
    x.sort()

t = [0] * (N + 1)  # 中部のパーツのサイズが Bi 以上のときの B と C の組み合わせの数
j = 0
for i in range(N):
    while j < N and C[j] <= B[i]:
        j += 1
    t[i] = N - j
for i in range(N - 1, -1, -1):
    t[i] += t[i + 1]

result = 0
i = 0
for a in A:
    while i < N and B[i] <= a:
        i += 1
    result += t[i]
print(result)
