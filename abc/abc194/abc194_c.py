from collections import Counter

N, *A = map(int, open(0).read().split())

c = Counter(A)
result = 0
for a in c:
    for b in c:
        result += (a - b) * (a - b) * c[a] * c[b]
print(result // 2)
