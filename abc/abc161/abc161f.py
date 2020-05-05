N = int(input())

if N == 2:
    # K = 2
    print(1)
    exit()

result = 2  # K = N - 1, N
for K in range(2, int(N ** 0.5 + 1)):
    t = N
    while t >= K and t % K == 0:
        t //= K
    if t % K == 1:
        result += 1

    if (N-1) % K == 0 and (N-1) // K > K:
        result += 1
print(result)
