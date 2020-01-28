N, M, P = map(int, input().split())

N %= M
result = 1
while P != 0:
    if P & 1 == 1:
        result *= N
        result %= M
    N *= N
    N %= M
    P >>= 1
print(result)
