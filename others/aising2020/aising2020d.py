def popcount(n):
    return bin(n).count("1")


def f(n):
    if n == 0:
        return 0
    return 1 + f(n % popcount(n))


N = int(input())
X = input()

c = X.count('1')
t1 = [0] * N
t1[0] = 1 % (c + 1)
for i in range(1, N):
    t1[i] = (t1[i - 1] << 1) % (c + 1)
x1 = 0
for i in range(N):
    if X[i] == '0':
        continue
    x1 += t1[N - 1 - i]

if c - 1 != 0:
    t2 = [0] * N
    t2[0] = 1 % (c - 1)
    for i in range(1, N):
        t2[i] = (t2[i - 1] << 1) % (c - 1)
    x2 = 0
    for i in range(N):
        if X[i] == '0':
            continue
        x2 += t2[N - 1 - i]

result = []
for i in range(N):
    if X[i] == '0':
        n = (x1 + t1[N - 1 - i]) % (c + 1)
    elif X[i] == '1':
        if c - 1 == 0:
            result.append(0)
            continue
        n = (x2 - t2[N - 1 - i]) % (c - 1)
    result.append(1 + f(n))
print(*result, sep='\n')
