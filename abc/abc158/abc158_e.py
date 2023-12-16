N, P = map(int, input().split())
S = input()

S = S[::-1]
result = 0
if P == 2 or P == 5:
    for i in range(N):
        if int(S[i]) % P == 0:
            result += N - i
else:
    t = [0] * P
    m = 1
    n = 0
    for i in range(len(S)):
        t[n] += 1
        n += int(S[i]) * m
        n %= P
        result += t[n]
        m *= 10
        m %= P
print(result)
