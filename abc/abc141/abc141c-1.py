N, K, Q = map(int, input().split())

score = [K - Q] * (N + 1)
for _ in range(Q):
    score[int(input())] += 1
for i in range(1, N + 1):
    if score[i] > 0:
        print('Yes')
    else:
        print('No')
