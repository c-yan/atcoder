N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
    S[i] = ''.join(sorted(S[i]))

t = {}
for i in range(N):
    if S[i] in t:
        t[S[i]] += 1
    else:
        t[S[i]] = 1
print(sum(t[k] * (t[k] - 1) // 2 for k in t))
