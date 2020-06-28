from time import time
from random import random

limit_secs = 2
start_time = time()

D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(D)]

def calc_score():
    score = 0
    S = 0
    last = [-1] * 26
    for d in range(D):
        S += s[d][t[d]]
        last[t[d]] = d
        for i in range(26):
            S -= c[i] * (d - last[i])
        score += max(10 ** 6 + S, 0)
    return score

def solution():
    return [i % 26 for i in range(D)]

t = solution()
score = calc_score()
while time() - start_time + 0.14 < limit_secs:
    d = int(random() * D)
    q = int(random() * 26)
    old = t[d]
    t[d] = q
    new_score = calc_score()
    if new_score < score:
        t[d] = old
    else:
        score = new_score
print('\n'.join(str(e + 1) for e in t))
