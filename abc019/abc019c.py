def f(x):
    while x % 2 == 0:
        x //= 2
    return x


N = int(input())
a = list(map(int, input().split()))

print(len({f(x) for x in set(a)}))
