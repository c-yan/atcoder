from math import ceil, log

N, K = map(int, input().split())

m = ceil(log(K, 2))
if K <= N:
    result = sum(1 / 2 ** ceil(log(K / i, 2))
                 for i in range(1, K)) / N
    result += (N - (K - 1)) / N
else:
    result = sum(1 / 2 ** ceil(log(K / i, 2))
                 for i in range(1, N + 1)) / N
print('%.12f' % result)
