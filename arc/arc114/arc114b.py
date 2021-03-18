m = 998244353

N = int(input())
f = list(map(lambda x: int(x) - 1, input().split()))

c = 0
checked = set()
for i in range(N):
    if i in checked:
        continue
    t = {i}
    p = f[i]
    while p not in t:
        t.add(p)
        if p in checked:
            break
        p = f[p]
    if len(checked & t) == 0:
        c += 1
    checked |= t
print((2 ** c - 1) % m)
