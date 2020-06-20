N, M = map(int, input().split())

m = 1000000007

if abs(N - M) > 1:
    print(0)
    exit()

k = min(N, M)
t = 1
for i in range(2, k + 1):
    t = t * i % m
t = t * t % m

if N == M:
    print(2 * t % m)
else:
    print(t * (k + 1) % m)
