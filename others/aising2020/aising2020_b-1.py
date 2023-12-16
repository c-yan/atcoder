N = int(input())
a = list(map(int, input().split()))

result = 0
for i in range(N):
    if (i + 1) % 2 == 1 and a[i] % 2 == 1:
        result += 1
print(result)
