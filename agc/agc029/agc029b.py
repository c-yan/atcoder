N = int(input())
A = list(map(int, input().split()))

d = {}
for a in A:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

result = 0
for a in sorted(d, reverse=True):
    if a not in d:
        continue
    t = (1 << a.bit_length()) - a
    if t not in d:
        continue
    if a != t:
        if d[a] < d[t]:
            i = d[a]
        else:
            i = d[t]
    else:
        if d[a] == 1:
            continue
        i = d[a] // 2
    result += i
    if d[a] == i:
        del d[a]
    else:
        d[a] -= i
    if d[t] == i:
        del d[t]
    else:
        d[t] -= i
print(result)
