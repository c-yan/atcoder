N = int(input())

Y = 0
for _ in range(N):
    t = input().split()
    x = float(t[0])
    u = t[1]
    if u == 'JPY':
        Y += x
    elif u == 'BTC':
        Y += x * 380000.0
print(Y)
