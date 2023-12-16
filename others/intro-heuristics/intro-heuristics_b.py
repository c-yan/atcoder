D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]
t = [int(input()) - 1 for _ in range(D)]

S = 0
last = [-1] * 26
score = 0
for d in range(D):
    S += s[d][t[d]]
    last[t[d]] = d
    for i in range(26):
        S -= c[i] * (d - last[i])
    score += max(10 ** 6 + S, 0)
    print(S)
