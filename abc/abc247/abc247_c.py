N = int(input())

S = [None] * N
S[0] = [1]
for i in range(N - 1):
    S[i + 1] = S[i] + [i + 2] + S[i]
print(*S[N - 1])
