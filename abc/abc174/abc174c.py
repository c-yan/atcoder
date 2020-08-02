K = int(input())

t = 7
for i in range(K):
    if t % K == 0:
        print(i + 1)
        break
    t = (t * 10 + 7) % K
else:
    print(-1)
