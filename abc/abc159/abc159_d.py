N = int(input())
A = list(map(int, input().split()))

d = {}
for a in A:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

s = 0
for k in d:
    s += d[k] * (d[k] - 1) // 2

for i in range(N):
    t = d[A[i]]
    print(s - t * (t - 1) // 2 + (t - 1) * (t - 2) // 2)
