from collections import deque

N, M = map(int, input().split())

links = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    links[A - 1].append(B - 1)

result = 0
for i in range(N):
    reachable = [0] * N
    reachable[i] = 1
    q = deque([i])
    while q:
        i = q.popleft()
        for j in links[i]:
            if reachable[j] == 1:
                continue
            reachable[j] = 1
            q.append(j)
    result += sum(reachable)
print(result)
