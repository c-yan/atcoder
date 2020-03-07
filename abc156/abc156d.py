# フェルマーの小定理
def mcomb(n, k):
    a = 1
    b = 1
    for i in range(k):
        a *= n - i
        a %= 1000000007
        b *= i + 1
        b %= 1000000007
    return a * pow(b, 1000000005, 1000000007) % 1000000007


n, a, b = map(int, input().split())

result = pow(2, n, 1000000007) - 1
result -= mcomb(n, a)
result + 1000000007
result %= 1000000007
result -= mcomb(n, b)
result + 1000000007
result %= 1000000007
print(result)
