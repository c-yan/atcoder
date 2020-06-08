N = int(input())
a = [input() for _ in range(N)]

t = ''
for i in range(N // 2):
    u = list(set(a[i]) & set(a[N - 1 - i]))
    if len(u) == 0:
        print(-1)
        exit()
    t += u[0]

if N % 2 == 0:
    print(t + t[::-1])
else:
    print(t + a[N // 2][0] + t[::-1])
