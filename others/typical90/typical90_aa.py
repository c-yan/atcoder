from sys import stdin

readline = stdin.readline

N = int(readline())
S = [readline()[:-1] for _ in range(N)]

t = set()
result = []
for i in range(N):
    if S[i] in t:
        continue
    result.append(i + 1)
    t.add(S[i])
print(*result, sep='\n')
