N = int(input())
H = list(map(int, input().split()))

t = 0
result = 0
for i in range(N - 1):
    if H[i + 1] <= H[i]:
        t += 1
    else:
        result = max(t, result)
        t = 0
result = max(t, result)
print(result)
