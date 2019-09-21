n, k = map(int, input().split())
result = (n // k) ** 3
if k % 2 == 0:
    result += (n // (k // 2) - (n // k)) ** 3
print(result)
