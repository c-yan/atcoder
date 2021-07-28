m = 1000000007

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

result = 1
for a in A:
    result *= sum(a)
    result %= m
print(result)
