A, B, C = map(int, input().split())
K = int(input())
result = sum([A, B, C])
t = max(A, B, C)
result += (t << K) - t
print(result)
