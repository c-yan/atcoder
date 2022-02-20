N, *a = map(int, open(0).read().split())

q = []
c = 0
result = []
for x in a:
    if len(q) == 0 or q[-1][0] != x:
        q.append((x, 1))
        c += 1
    else:
        n = q[-1][1]
        if n == x - 1:
            q.pop()
            c -= n
        else:
            q[-1] = (x, n + 1)
            c += 1
    result.append(c)
print(*result, sep='\n')
