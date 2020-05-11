# フェルマーの小定理
N, M, K = map(int, input().split())

result = 0
n = 1
k = 1
for i in range(K + 1):
    # result += M * mcomb(N - 1, i) * pow(M - 1, N - 1 - i, 998244353)
    result += n * pow(k, 998244353 - 2, 998244353) * pow(M - 1, N - 1 - i, 998244353)
    result %= 998244353
    n *= N - 1 - i
    n %= 998244353
    k *= i + 1
    k %= 998244353
result *= M
result %= 998244353
print(result)
