N, M, Q = map(int, input().split())

score = [N] * (M + 1)
answered = [[False] * (M + 1) for _ in range(N + 1)]
for _ in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        t = 0
        for i in range(1, M + 1):
            if answered[s[1]][i]:
                t += score[i]
        print(t)
    elif s[0] == 2:
        score[s[2]] -= 1
        answered[s[1]][s[2]] = True
