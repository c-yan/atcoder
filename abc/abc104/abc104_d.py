from itertools import accumulate

m = 1000000007

S = input()

n = len(S)
a = [0] * n
c = [0] * n
w = [0] * n
for i in range(n):
    if S[i] == 'A':
        a[i] = 1
    elif S[i] == 'C':
        c[i] = 1
    elif S[i] == '?':
        w[i] = 1
a = list(accumulate(a))
c = list(accumulate(c))
w = list(accumulate(w))

result = 0
for j in range(1, n - 1):
    if S[j] not in 'B?':
        continue
    x = a[j - 1]
    y = w[j - 1]
    t = x * pow(3, y, m) + y * pow(3, y - 1, m)
    x = c[n - 1] - c[j]
    y = w[n - 1] - w[j]
    t *= x * pow(3, y, m) + y * pow(3, y - 1, m)
    result += t
    result %= m
print(result)
