d = {}
N = int(input())
for _ in range(N):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
M = int(input())
for _ in range(M):
    t = input()
    if t in d:
        d[t] -= 1
    else:
        d[t] = -1
print(max(0, *d.values()))
