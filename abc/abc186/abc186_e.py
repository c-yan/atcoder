from math import gcd

T = int(input())
for _ in range(T):
    N, S, K = map(int, input().split())
    d = gcd(gcd(K, -S), N)
    k = K // d
    n = N // d
    if gcd(k, n) != 1:
        print(-1)
    else:
        print(pow(k, -1, n) * (-S // d) % n)
