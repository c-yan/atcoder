N = int(input())
A = list(map(int, input().split()))

m = 1000000007

A.sort()
if N % 2 == 0:
    B = list(range(1, N, 2)) * 2
else:
    B = [0] + list(range(2, N, 2)) * 2
B.sort()

if A != B:
    print(0)
else:
    result = 1
    for i in range(N // 2):
        result *= 2
        result %= m
    print(result)
