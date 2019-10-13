from sys import exit

divisor = 1000000007

N, M = map(int, input().split())

if abs(N - M) > 1:
    print(0)
    exit()

k = min(N, M)
t = 1
for i in range(2, k + 1):
    t = t * i % divisor
t = t * t % divisor

if N == M:
    print(2 * t % divisor)
else:
    print(t * (k + 1) % divisor)
