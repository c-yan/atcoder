N = int(input())
P = list(map(int, input().split()))

result = 0
m = P[0]
for i in range(N):
    if P[i] <= m:
        result += 1
        m = P[i]
print(result)
