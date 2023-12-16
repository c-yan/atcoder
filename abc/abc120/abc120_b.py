A, B, K = map(int, input().split())

result = 0
for i in range(100, 0, -1):
    if A % i == 0 and B % i == 0:
        result = i
        K -= 1
        if K == 0:
            break
print(result)
