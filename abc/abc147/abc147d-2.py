import numpy as np

N = int(input())
A = np.fromiter(map(int, input().split()), np.int64)

m = 1000000007

result = 0
for bit in range(60):
    c = int((A & 1).sum())
    A >>= 1
    result = (result + c * (N - c) * (1 << bit)) % m
print(result)
