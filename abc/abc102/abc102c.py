N = int(input())
A = list(map(int, input().split()))

t = list(sorted(A[i] - (i + 1) for i in range(N)))
b = t[len(t) // 2]
print(sum(abs(A[i] - (b + i + 1)) for i in range(N)))
