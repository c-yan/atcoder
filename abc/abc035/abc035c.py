# imos 法
N, Q = map(int, input().split())
cs = [0] * N
for _ in range(Q):
    l, r = map(int, input().split())
    cs[l - 1] += 1
    if r != N:
        cs[r] -= 1
for i in range(1, N):
    cs[i] += cs[i - 1]
print(''.join(str(i % 2) for i in cs))
