N, *S = open(0).read().split()

t = 1
f = 1
for s in S:
    if s == 'AND':
        f = t + f * 2
    elif s == 'OR':
        t = t * 2 + f
print(t)
