from sys import setrecursionlimit, stdin


def bit_add(bit, i, x):
    i += 1
    n = len(bit)
    while i <= n:
        bit[i - 1] += x
        i += i & -i


def bit_sum(bit, i):
    result = 0
    i += 1
    while i > 0:
        result += bit[i - 1]
        i -= i & -i
    return result


def query(bit, start, stop):
    if start == 0:
        return bit_sum(bit, stop - 1)
    else:
        return bit_sum(bit, stop - 1) - bit_sum(bit, start - 1)


readline = stdin.readline
setrecursionlimit(10 ** 6)

N, Q = map(int, readline().split())
a = list(map(int, readline().split()))

bit = [0] * N
for i in range(N):
    bit_add(bit, i, a[i])

result = []
for _ in range(Q):
    Query = readline()
    if Query[0] == '0':
        _, p, x = map(int, Query.split())
        bit_add(bit, p, x)
    elif Query[0] == '1':
        _, l, r = map(int, Query.split())
        result.append(query(bit, l, r))

print(*result, sep='\n')
