N = int(input())
a = list(map(int, input().split()))

t = [0] * N
for i in range(N - 1, -1, -1):
    t[i] = (sum(t[2 * (i + 1) - 1::i + 1]) % 2) ^ a[i]

print(sum(t))
print(*[i + 1 for i in range(N) if t[i] == 1])
