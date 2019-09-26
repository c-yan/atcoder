N = int(input())
a = list(map(int, input().split()))
result = 0
start = 0
for i in range(N - 1):
    if a[i] >= a[i + 1]:
        t = i - start + 1
        result += (t + 1) * t // 2
        start = i + 1
t = (N - 1) - start + 1
result += (t + 1) * t // 2
print(result)
