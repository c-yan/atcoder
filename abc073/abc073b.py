N = int(input())

result = 0
for _ in range(N):
    l, r = map(int, input().split())
    result += r - l + 1
print(result)
