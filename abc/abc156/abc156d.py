# フェルマーの小定理
def mcomb(n, k):
    a = 1
    b = 1
    for i in range(k):
        a *= n - i
        a %= m
        b *= i + 1
        b %= m
    return a * pow(b, m - 2, m) % m


n, a, b = map(int, input().split())

m = 1000000007

result = pow(2, n, m) - 1
result += m - mcomb(n, a)
result %= m
result += m - mcomb(n, b)
result %= m
print(result)
