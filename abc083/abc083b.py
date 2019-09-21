n, a, b = map(int, input().split())
result = 0
for i in range(1, n + 1):
    if a <= sum(map(int, str(i))) <= b:
        result += i
print(result)
