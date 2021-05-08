N, *A = map(int, open(0).read().split())


def backtrack(n):
    result = []
    while dp[n] is not None:
        pn = n
        result.append(dp[n] + 1)
        n -= A[dp[n]]
        n %= 200
        if n == pn:
            break
    return list(reversed(result))


def finish(B, C):
    print('Yes')
    print(len(B), *B)
    print(len(C), *C)
    exit()


dp = [None] * 200
for i in range(N):
    a = A[i] % 200

    if dp[0] is not None:
        B = backtrack(0) + [i + 1]
        C = [i + 1]
        finish(B, C)

    if dp[a] is not None:
        B = backtrack(a)
        C = [i + 1]
        finish(B, C)

    ndp = dp[:]
    ndp[a] = i
    for j in range(1, 200):
        if dp[j] is None:
            continue
        k = (j + a) % 200
        if dp[k] is not None:
            B = backtrack(k)
            C = backtrack(j) + [i + 1]
            finish(B, C)
        ndp[k] = i
    dp = ndp
print('No')
