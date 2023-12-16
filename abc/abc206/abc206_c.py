from collections import Counter

N, *A = map(int, open(0).read().split())

t = 0
for c in Counter(A).values():
    t += c * (N - c)
print(t // 2)
