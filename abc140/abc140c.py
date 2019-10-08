N = int(input())
B = list(map(int, input().split()))

result = B[0] + B[N - 2]
for i in range(1, N - 1):
    result += min(B[i - 1], B[i])
print(result)
