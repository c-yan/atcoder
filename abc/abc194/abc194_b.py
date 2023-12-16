N = int(input())

a = []
b = []
for _ in range(N):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)

result = 10 ** 18
for i in range(N):
    for j in range(N):
        if i == j:
            result = min(result, a[i] + b[i])
        else:
            result = min(result, max(a[i], b[j]))
print(result)
