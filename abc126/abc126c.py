import math
n, k = [int(e) for e in input().split()]
m = math.ceil(math.log(k, 2))
if k <= n:
    result = sum(1 / 2 ** math.ceil(math.log(k / i, 2))
                 for i in range(1, k)) / n
    result += (n - (k - 1)) / n
else:
    result = sum(1 / 2 ** math.ceil(math.log(k / i, 2))
                 for i in range(1, n + 1)) / n
print('%.12f' % result)
