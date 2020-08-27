N, *a = map(int, open(0).read().split())

t = sum(a)
if t % N != 0:
    print(-1)
    exit()
t //= N

result = 0
c = 0
n = 0
for e in a:
    c += e
    n += 1
    if c % n == 0 and c // n == t:
        c = 0
        n = 0
    else:
        result += 1
print(result)
