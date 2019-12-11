N = int(input())
A = list(map(int, input().split()))

result = 0
for bit in range(60):
    m = 1 << bit
    c = sum(a & m for a in A) >> bit
    result += (c * (N - c)) << bit
    result %= 1000000007
print(result)
