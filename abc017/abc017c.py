# imos 法
N, M = map(int, input().split())

score = [0] * M  # 宝石iを取らないときの得点
for i in range(N):
    l, r, s = map(int, input().split())
    score[0] += s
    score[l - 1] -= s
    if r < M:
        score[r] += s
for i in range(1, M):
    score[i] += score[i - 1]
print(max(score))
