N = int(input())

sieve = [0] * 101
sieve[0] = -1
sieve[1] = -1
for i in range(2, 101):
    if sieve[i] != 0:
        continue
    sieve[i] = i
    for j in range(i * i, 101, i):
        if sieve[j] == 0:
            sieve[j] = i

d = {}
for i in range(2, N + 1):
    while i != 1:
        d.setdefault(sieve[i], 0)
        d[sieve[i]] += 1
        i //= sieve[i]

# 75 = 5 * 5 * 3
#    = 15 * 5
#    = 25 * 3
#    = 75
n74 = 0
n24 = 0
n14 = 0
n4 = 0
n2 = 0
for k in d:
    if d[k] >= 74:
        n74 += 1
    if d[k] >= 24:
        n24 += 1
    if d[k] >= 14:
        n14 += 1
    if d[k] >= 4:
        n4 += 1
    if d[k] >= 2:
        n2 += 1

result = 0
# x ^ 4 * y ^ 4 * z ^ 2 の約数の個数は75個
result += n4 * (n4 - 1) // 2 * (n2 - 2)
# x ^ 14 * y ^ 4 の約数の個数は75個
result += n14 * (n4 - 1)
# x ^ 24 * y ^ 2 の約数の個数は75個
result += n24 * (n2 - 1)
# x ^ 74 の約数の個数は75個
result += n74
print(result)
