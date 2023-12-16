N, M = map(int, input().split())
H = list(map(int, input().split()))

t = [0] * N
for _ in range(M):
    A, B = map(int, input().split())
    t[A - 1] = max(t[A - 1], H[B - 1])
    t[B - 1] = max(t[B - 1], H[A - 1])

result = 0
for i in range(N):
    if H[i] > t[i]:
        result += 1
print(result)
