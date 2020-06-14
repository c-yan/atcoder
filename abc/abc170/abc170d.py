N = int(input())
A = list(map(int, input().split()))

d = {}
for a in A:
    d.setdefault(a, 0)
    d[a] += 1

A = sorted(set(A))
t = [True] * (10 ** 6 + 1)
for a in A:
    if d[a] > 1:
        t[a] = False
    for i in range(a + a, 10 ** 6 + 1, a):
        t[i] = False
print(sum(1 for a in A if t[a]))
