L, R, d = map(int, input().split())

result = 0
for i in range(L, R + 1):
    if i % d == 0:
        result += 1
print(result)
