n = int(input())
a = [int(e) for e in input().split()]
p = a[0]
result = 0
for i in range(1, n):
    if p == a[i]:
        result += 1
        p = -1
    else:
        p = a[i]
print(result)
