S = input()

N = len(S) + 1
t = [0] * N
for i in range(N - 1):
    if S[i] == '<':
        t[i + 1] = t[i] + 1
for i in range(N - 2, -1, -1):
    if S[i] == '>':
        t[i] = max(t[i], t[i + 1] + 1)
print(sum(t))
