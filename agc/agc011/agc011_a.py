N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()

c = 0
l = float('inf')
result = 0
for i in range(N):
    t = T[i]
    if t > l:
        result += 1
        l = float('inf')
        c = 0
    if c == 0:
        l = t + K
    c += 1
    if c == C:
        result += 1
        l = float('inf')
        c = 0
if c != 0:
    result += 1
print(result)
