from sys import stdin

readline = stdin.readline

N, M = map(int, readline().split())

links = [set() for _ in range(N)]
for _ in range(M):
    U, V = map(int, readline().split())
    links[U - 1].add(V - 1)

result = 0
for a in range(N - 2):
    for b in range(a + 1, N - 1):
        for c in range(b + 1, N):
            if b not in links[a]:
                continue
            if c not in links[b]:
                continue
            if c not in links[a]:
                continue
            result += 1
print(result)
