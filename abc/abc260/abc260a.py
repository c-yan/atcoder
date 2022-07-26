S = input()

d = {}
for c in S:
    d.setdefault(c, 0)
    d[c] += 1

for c in d:
    if d[c] == 1:
        print(c)
        exit()
else:
    print(-1)
