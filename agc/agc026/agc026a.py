N = int(input())
a = list(map(int, input().split()))

p = a[0]
result = 0
for i in range(1, N):
    if p == a[i]:
        result += 1
        p = -1
    else:
        p = a[i]
print(result)
