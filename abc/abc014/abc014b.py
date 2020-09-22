n, X, *a = map(int, open(0).read().split())

result = 0
for i in range(n):
    if X & 1 == 1:
        result += a[i]
    X >>= 1
print(result)
