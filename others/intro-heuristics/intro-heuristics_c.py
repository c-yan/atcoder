def calc_satisfaction():
    S = 0
    last = [-1] * 26
    for d in range(D):
        S += s[d][t[d]]
        last[t[d]] = d
        for i in range(26):
            S -= c[i] * (d - last[i])
    return S


D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]
t = [int(input()) - 1 for _ in range(D)]
M = int(input())
for _ in range(M):
    d, q = [int(s) - 1 for s in input().split()]
    old = t[d]
    t[d] = q
    print(calc_satisfaction())
