N = int(input())
A = list(map(int, input().split()))

print(*[t[1] for t in sorted(zip(A, range(1, N + 1)))])
