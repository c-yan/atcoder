N = int(input())

result = 0
for _ in range(N):
    A, B = map(int, input().split())
    result += (A + B) * (B - A + 1) // 2
print(result)
