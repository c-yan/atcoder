L = input()

m = 1000000007

result = 1
t = 1
for c in L[::-1]:
    if c == '1':
        result = result * 2 + t
        result %= m
    t *= 3
    t %= m
print(result)
