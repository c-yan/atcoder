N = int(input())
a = list(map(int, input().split()))

result = -float('inf')
for i in range(N):
    index = -1
    best = -float('inf')
    for j in range(N):
        if i == j:
            continue
        t = sum(a[min(i, j): max(i, j) + 1][1::2])
        if best < t:
            best = t
            index = j
    result = max(result, sum(a[min(i, index): max(i, index) + 1][::2]))
print(result)
