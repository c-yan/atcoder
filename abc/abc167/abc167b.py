A, B, C, K = map(int, input().split())

result = 0
t = min(A, K)
result += t
K -= t
t = min(B, K)
K -= t
t = min(C, K)
result -= t
print(result)
