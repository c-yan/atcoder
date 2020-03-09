L = input()

result = 1
t = 1
for c in L[::-1]:
    if c == '1':
        result = result * 2 + t
        result %= 1000000007
    t *= 3
    t %= 1000000007
print(result)
