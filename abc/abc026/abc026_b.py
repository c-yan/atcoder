from math import pi

N, *R = map(int, open(0).read().split())

R.sort(reverse=True)

t = 0
for r in R[::2]:
    t += r * r
for r in R[1::2]:
    t -= r * r
print(pi * t)
