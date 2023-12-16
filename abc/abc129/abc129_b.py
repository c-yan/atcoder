N = int(input())
W = list(map(int, input().split()))

result = float('inf')
for T in range(N - 1):
    sd = abs(sum(W[0:T + 1]) - sum(W[T + 1:]))
    if sd < result:
        result = sd
print(result)
