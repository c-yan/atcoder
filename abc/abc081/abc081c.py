N, K = map(int, input().split())
A = list(map(int, input().split()))

d = {}
for a in A:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
print(sum(sorted(d.values())[:-K]))
