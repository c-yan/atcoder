N, *p = map(int, open(0).read().split())

result = []
t = 0
s = set()
for x in p:
    s.add(x)
    while t in s:
        t += 1
    result.append(t)
print(*result, sep='\n')
