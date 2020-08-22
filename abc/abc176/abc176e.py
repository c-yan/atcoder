H, W, M = map(int, input().split())

hc = [0] * H
wc = [0] * W
d = {}
for _ in range(M):
    h, w = map(lambda x: int(x) - 1,input().split())
    hc[h] += 1
    wc[w] += 1
    d.setdefault(h, {})
    d[h][w] = 1

result = 0
hm = max(hc)
wm = max(wc)
hi = [i for i in range(H) if hc[i] == hm]
wi = [i for i in range(W) if wc[i] == wm]

for h in hi:
    for w in wi:
        if h in d and w in d[h]:
            result = max(result, hm + wm - 1)
        else:
            result = max(result, hm + wm)
            break
print(result)
