# imos 法
N, K, Q = map(int, input().split())

score = [0] * N
score[0] = K
for _ in range(Q):
    A = int(input())
    if A == 1:
        score[1] -= 1
    elif A == N:
        score[0] -= 1
        score[N - 1] += 1
    else:
        score[0] -= 1
        score[A - 1] += 1
        score[A] -= 1

for i in range(1, N):
    score[i] += score[i - 1]

for v in score:
    if v > 0:
        print('Yes')
    else:
        print('No')
