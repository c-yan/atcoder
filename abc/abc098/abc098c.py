# 累積和
N = int(input())
S = input()

cws = [0] * N  # i番目がリーダーのとき、それより左にいる西を向いている人数
for i in range(1, N):
    if S[i - 1] == 'W':
        cws[i] = 1
    cws[i] += cws[i - 1]

ces = [0] * N  # i番目がリーダーのとき、それより右にいる東を向いている人数
for i in range(N - 2, -1, -1):
    if S[i + 1] == 'E':
        ces[i] = 1
    ces[i] += ces[i + 1]

print(min(cws[i] + ces[i] for i in range(N)))
