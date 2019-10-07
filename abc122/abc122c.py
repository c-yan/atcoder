# 累積和
N, Q = map(int, input().split())
S = input()

cs = [0] * N
for i in range(1, N):
    if S[i - 1:i + 1] == 'AC':
        cs[i] = 1
for i in range(1, N):
    cs[i] += cs[i - 1]

for _ in range(Q):
    l, r = map(int, input().split())
    t = cs[r - 1]
    if l != 1:
        t -= cs[l - 2]
        if S[l - 2:l] == 'AC':
            t -= 1
    print(t)
