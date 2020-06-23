N = int(input())
m = list(map(int, input().split()))

result = 0
for i in range(N):
    if m[i] < 80:
        result += 80 - m[i]
print(result)
