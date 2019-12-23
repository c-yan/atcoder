N = int(input())
a = [int(s) - 1 for s in input().split()]

result = 0
for i in range(N):
    if a[i] != (i - result):
        result += 1

if result == N:
    print(-1)
else:
    print(result)
