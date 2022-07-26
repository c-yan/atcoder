N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []

a = list(range(1, N + 1))

a.sort(key=lambda x: (A[x - 1], -x), reverse=True)
result.extend(a[:X])
a = a[X:]

a.sort(key=lambda x: (B[x - 1], -x), reverse=True)
result.extend(a[:Y])
a = a[Y:]

a.sort(key=lambda x: (A[x - 1] + B[x - 1], -x), reverse=True)
result.extend(a[:Z])

print(*sorted(result), sep='\n')
