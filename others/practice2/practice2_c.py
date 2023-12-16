from sys import stdin


def floor_sum(n, m, a, b):
    result = 0
    if a >= m:
        result += (n - 1) * n * (a // m) // 2
        a %= m
    if b >= m:
        result += n * (b // m)
        b %= m

    yMax = (a * n + b) // m
    xMax = yMax * m - b
    if yMax == 0:
        return result
    result += (n - (xMax + a - 1) // a) * yMax
    result += floor_sum(yMax, a, m, (a - xMax % a) % a)
    return result


readline = stdin.readline

T = int(readline())

result = []
for _ in range(T):
    N, M, A, B = map(int, readline().split())
    result.append(floor_sum(N, M, A, B))
print(*result, sep='\n')
