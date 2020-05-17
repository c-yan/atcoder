from collections import deque

N, M = map(int, input().split())
AB = [map(int, input().split()) for _ in range(M)]

links = [[] for _ in range(N + 1)]
for a, b in AB:
    links[a].append(b)
    links[b].append(a)

result = [-1] * (N + 1)
q = deque([1])
while q:
    i = q.popleft()
    for j in links[i]:
        if result[j] == -1:
            result[j] = i
            q.append(j)
print('Yes')
print('\n'.join(str(i) for i in result[2:]))
