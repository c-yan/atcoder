N = int(input())
S = input()

MOD = 1000000007

d = {}
for c in S:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

result = 1
for x in d.values():
    result *= x + 1
    result %= MOD
result += MOD - 1
result %= MOD

print(result)
