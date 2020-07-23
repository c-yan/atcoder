m, n, N = map(int, input().split())

result = N
recycled = N
while recycled >= m:
    result += (recycled // m) * n
    recycled = (recycled % m) + (recycled // m) * n
print(result)
