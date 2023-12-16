N, K, *t = map(int, open(0).read().split())

a = t[0] + t[1]
for i in range(2, N):
    a += t[i]
    if a < K:
        print(i)
        break
    a -= t[i - 2]
else:
    print(-1)
