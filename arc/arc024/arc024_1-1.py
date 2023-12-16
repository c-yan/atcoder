L, R = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))

l.sort()
r.sort()
i, j = 0, 0
result = 0
while i < L and j < R:
    if l[i] == r[j]:
        result += 1
        i += 1
        j += 1
    elif l[i] < r[j]:
        i += 1
    elif l[i] > r[j]:
        j += 1
print(result)
