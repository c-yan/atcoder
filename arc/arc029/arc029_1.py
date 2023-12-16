N, *t = map(int, open(0).read().split())

t.sort(reverse=True)
a = 0
b = 0
for e in t:
    if a <= b:
        a += e
    else:
        b += e
print(max(a, b))
