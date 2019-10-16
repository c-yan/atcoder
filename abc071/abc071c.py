N = int(input())
A = list(map(int, input().split()))

d = {}
for a in A:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

l = [k for k in d if d[k] >= 2]
l.sort(reverse=True)

if len(l) == 0:
    print(0)
elif d[l[0]] >= 4:
    print(l[0] * l[0])
elif len(l) == 1:
    print(0)
else:
    print(l[0] * l[1])
