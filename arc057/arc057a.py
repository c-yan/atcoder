A, K = map(int, input().split())

n = 2 * 10 ** 12
if K == 0:
    print(n - A)
else:
    result = 0
    t = A
    while t < n:
        t += 1 + K * t
        result += 1
    print(result)
