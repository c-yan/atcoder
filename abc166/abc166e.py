N = int(input())
A = list(map(int, input().split()))

c1 = {}
c2 = {}

for i in range(N):
    c1.setdefault(i + A[i], 0)
    c1[i + A[i]] += 1
    c2.setdefault(i - A[i], 0)
    c2[i - A[i]] += 1

result = 0
for k in set(c1).intersection(c2):
    result += c1[k] * c2[k]
print(result)
