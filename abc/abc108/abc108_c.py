N, K = map(int, input().split())

result = (N // K) ** 3
if K % 2 == 0:
    result += (N // (K // 2) - (N // K)) ** 3
print(result)
