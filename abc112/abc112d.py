from math import sqrt

N, M = map(int, input().split())

result = 1
for i in range(1, int(sqrt(M)) + 1):
    if M % i != 0:
        continue
    t = M // i
    if t >= N:
        result = max(result, i)
    if M // t >= N:
        result = max(result, t)
print(result)
