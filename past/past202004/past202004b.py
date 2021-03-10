S = input()

d ={}
for c in S:
    d.setdefault(c, 0)
    d[c] += 1
print(sorted(((d[k], k) for k in d), reverse=True)[0][1])
