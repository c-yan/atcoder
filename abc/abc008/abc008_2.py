N = int(input())

d = {}
for _ in range(N):
    S = input()
    d.setdefault(S, 0)
    d[S] += 1

v = max(d.values())
for k in d:
    if d[k] != v:
        continue
    print(k)
    break
