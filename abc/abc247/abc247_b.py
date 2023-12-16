N = int(input())
st = [input().split() for _ in range(N)]

d = {}
for s, t in st:
    d.setdefault(s, 0)
    d.setdefault(t, 0)
    if s == t:
        d[s] += 1
    else:
        d[s] += 1
        d[t] += 1

for s, t in st:
    if d[s] != 1 and d[t] != 1:
        print('No')
        exit()
print('Yes')
