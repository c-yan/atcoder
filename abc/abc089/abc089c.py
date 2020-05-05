N = int(input())
S = [input() for _ in range(N)]

s = [t[0] for t in S if t[0] in 'MARCH']
d = {}
for t in s:
    if t in d:
        d[t] += 1
    else:
        d[t] = 1

l = list(d.keys())
result = 0
for i in range(len(l) - 2):
    for j in range(i + 1, len(l) - 1):
        for k in range(j + 1, len(l)):
            result += d[l[i]] * d[l[j]] * d[l[k]]
print(result)
