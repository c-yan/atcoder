from sys import stdin

readline = stdin.readline

N = int(readline())
a = []
s = set()
for i in range(N):
    S, T = readline().split()
    T = int(T)
    if S in s:
        continue
    s.add(S)
    a.append((T, -i, S))
a.sort(reverse=True)
print(-a[0][1] + 1)
