N = int(input())
B = [int(input()) for _ in range(N - 1)]

m = [None] * (N + 1)
for i in range(N - 1):
    if m[B[i]] is None:
        m[B[i]] = [i + 2]
    else:
        m[B[i]].append(i + 2)

s = [0] * (N + 1)
for i in range(1, N + 1):
    if m[i] is None:
        s[i] = 1


def f(i):
    for j in m[i]:
        if s[j] == 0:
            s[j] = f(j)
    return min(s[j] for j in m[i]) + max(s[j] for j in m[i]) + 1


for i in range(1, N + 1):
    if s[i] == 0:
        s[i] = f(i)

print(s[1])
