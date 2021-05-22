from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

x = {}
for i in range(N):
    b = B[i]
    x.setdefault(b, [])
    x[b].append(i)

y = {}
for i in range(N):
    c = C[i] - 1
    y.setdefault(c, 0)
    y[c] += 1

z = Counter(A)

result = 0
for a in z:
    if a not in x:
        continue
    c = 0
    for i in x[a]:
        if i not in y:
            continue
        c += y[i]
    result += c * z[a]
print(result)
