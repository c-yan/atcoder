# パスカルの三角形
N, K = map(int, input().split())

c = [[0] * 2001 for _ in range(2000 + 1)]
c[0][0] = 1
for i in range(1, 2000 + 1):
    ci = c[i]
    ci1 = c[i - 1]
    ci[0] = 1
    for j in range(1, i + 1):
        ci[j] = (ci1[j - 1] + ci1[j]) % 1000000007

for i in range(1, K + 1):
    print(c[K - 1][i - 1] * c[N - K + 1][i] % 1000000007)
