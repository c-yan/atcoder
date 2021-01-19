from sys import stdin


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


def bit_query(bit, start, stop):
    return bit_sum(bit, stop - 1) - bit_sum(bit, start - 1)


readline = stdin.readline

N, Q = map(int, readline().split())
c = list(map(lambda x: int(x) - 1, readline().split()))

lr = [None] * Q
for i in range(Q):
    l, r = map(lambda x: int(x) - 1, readline().split())
    lr[i] = (r, l, i)
lr.sort(key=lambda x: x[0])
l = [lr[i][1] for i in range(Q)]
r = [lr[i][0] for i in range(Q)]
idx = [lr[i][2] for i in range(Q)]

result = [0] * Q
bit = [0] * N
mr = [-1] * N
j = 0
for i in range(N):
    if mr[c[i]] != -1:
        bit_add(bit, mr[c[i]], -1)
    bit_add(bit, i, 1)
    mr[c[i]] = i
    while j < Q:
        if r[j] != i:
            break
        result[idx[j]] = bit_query(bit, l[j], r[j] + 1)
        j += 1
print(*result, sep='\n')
