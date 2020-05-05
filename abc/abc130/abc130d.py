# しゃくとり法
N, K = map(int, input().split())
a = list(map(int, input().split()))

result = 0
i = 0
j = 0
v = 0
while True:
    v += a[j]
    if v < K:
        j += 1
    else:
        result += N - j
        v -= a[i]
        if j > i:
            v -= a[j]
        i += 1
        if j < i:
            j += 1
    if j == N:
        print(result)
        break
