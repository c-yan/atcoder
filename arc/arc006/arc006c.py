from bisect import bisect_left

N, *w = map(int, open(0).read().split())

t = []
for x in w:
    i = bisect_left(t, x)
    if i == len(t):
        t.append(x)
    else:
        t[i] = x
    t.sort()
print(len(t))
