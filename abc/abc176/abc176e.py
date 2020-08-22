H, W, M = map(int, input().split())

hc = [0] * H
wc = [0] * W
d = {}
for _ in range(M):
    h, w = map(lambda x: int(x) - 1,input().split())
    hc[h] += 1
    wc[w] += 1
    d[(h, w)] = 1

maxh = max(hc)
maxw = max(wc)

result = maxh + maxw - 1
wi = [i for i in range(W) if wc[i] == maxw]
for h in [i for i in range(H) if hc[i] == maxh]:
    for w in wi:
        if (h, w) not in d:
            result = maxh + maxw
            break
print(result)
