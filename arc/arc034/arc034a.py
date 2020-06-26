N = int(input())

result = 0
for _ in range(N):
    a, b, c, d, e = map(int, input().split())
    result = max(result, ((a + b + c + d) * 900 + e * 110) / 900)
print(result)
