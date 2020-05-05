N = int(input())

t = 1
result = 0
for a in map(int, input().split()):
    if a == t:
        t += 1
    else:
        result += 1

if result == N:
    print(-1)
else:
    print(result)
