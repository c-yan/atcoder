# 二分探索, 累積和
from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

for x in [A, B, C]:
    x.sort()

t = [0] * (N + 1)  # 中部のパーツのサイズが Bi 以上のときの B と C の組み合わせの数
for i in range(N):
    t[i] = N - bisect_right(C, B[i])
for i in range(N - 1, -1, -1):
    t[i] += t[i + 1]

result = 0
for a in A:
    result += t[bisect_right(B, a)]
print(result)
