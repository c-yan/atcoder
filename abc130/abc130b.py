N, X = map(int, input().split())
L = list(map(int, input().split()))

d = 0
result = 1
for i in range(N):
    d += L[i]
    if d <= X:
        result += 1
    else:
        break
print(result)
