N = int(input())
K = int(input())

result = 0
for x in map(int, input().split()):
    result += min(x, K - x) * 2
print(result)
