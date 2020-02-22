N, K = map(int, input().split())

result = 0
while N != 0:
    result += 1
    N //= K
print(result)
