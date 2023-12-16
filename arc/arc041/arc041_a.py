x, y = map(int, input().split())
k = int(input())

result = 0
result += min(y, k)
k -= min(y, k)
result += x - k
print(result)
