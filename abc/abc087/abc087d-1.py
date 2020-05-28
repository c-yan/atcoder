# 深さ優先探索
N, M = map(int, input().split())

links = [[] for _ in range(N + 1)]
for _ in range(M):
    L, R, D = map(int, input().split())
    links[L].append((R, D))
    links[R].append((L, -D))

t = [None] * (N + 1)
for i in range(1, N + 1):
    if t[i] is not None:
        continue
    t[i] = 0
    s = [i]
    while s:
        j = s.pop()
        for k, l in links[j]:
            if t[k] is None:
                t[k] = t[j] + l
                s.append(k)
            else:
                if t[k] != t[j] + l:
                    print('No')
                    exit()
print('Yes')
