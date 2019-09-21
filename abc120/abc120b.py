a, b, k = map(int, input().split())
c = 0
result = 0
for i in range(100, 0, -1):
    if a % i == 0 and b % i == 0:
        result = i
        c += 1
        if c == k:
            break
print(result)
