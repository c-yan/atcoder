# パスカルの三角形
N, K = map(int, input().split())

n = max(K, N - K + 1)
c = [[0] * (n + 1) for _ in range(n + 1)]
c[0][0] = 1
for i in range(1, n + 1):
    c[i][0] = 1
    for j in range(1, i + 1):
        c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % 1000000007

result = []
for i in range(1, K + 1):
    result.append(c[K - 1][i - 1] * c[N - K + 1][i] % 1000000007)
print('\n'.join(str(i) for i in result))
