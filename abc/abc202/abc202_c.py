from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

x = Counter(A)
y = Counter(B[c - 1] for c in C)

result = 0
for a in x:
    if a not in y:
        continue
    result += x[a] * y[a]
print(result)
