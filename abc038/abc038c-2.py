# 累積和
N = int(input())
a = list(map(int, input().split()))

cs = [1] * N
for i in range(1, N):
    if a[i] > a[i - 1]:
        cs[i] += cs[i - 1]
print(sum(cs))
