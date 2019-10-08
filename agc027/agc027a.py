N, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
result = 0
for v in a:
    x -= v
    if x < 0:
        break
    result += 1
if x != 0 and result == N:
    result -= 1
print(result)
