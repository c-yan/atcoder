N, K = map(int, input().split())
A = list(map(int, input().split()))

m = 1000000007

a = [e for e in A if e > 0]
b = [e for e in A if e < 0]
c = [e for e in A if e == 0]
# プラスルート
if len(a) >= K - (min(K, len(b)) // 2) * 2:
    a.sort(reverse=True)
    b.sort()
    result = 1
    i = 0
    j = 0
    k = 0
    while k < K:
        if k < K - 1 and i < len(a) - 1 and j < len(b) - 1:
            x = a[i] * a[i + 1]
            y = b[j] * b[j + 1]
            if y >= x:
                result *= y
                result %= m
                j += 2
                k += 2
            else:
                result *= a[i]
                result %= m
                i += 1
                k += 1
        elif k < K - 1 and j < len(b) - 1:
            y = b[j] * b[j + 1]
            result *= y
            result %= m
            j += 2
            k += 2
        elif i < len(a):
            result *= a[i]
            result %= m
            i += 1
            k += 1
        elif j < len(b):
            result *= b[j]
            result %= m
            j += 1
            k += 1
    print(result)
# 0 ルート
elif len(c) != 0:
    print(0)
# マイナスルート
else:
    a.sort()
    b.sort(reverse=True)
    result = 1
    i = 0
    j = 0
    k = 0
    while k < K:
        if i < len(a) and j < len(b):
            if a[i] <= -b[i]:
                result *= a[i]
                result %= m
                i += 1
                k += 1
            else:
                result *= b[j]
                result %= m
                j += 1
                k += 1
        elif i < len(a):
            result *= a[i]
            result %= m
            i += 1
            k += 1
        elif j < len(b):
            result *= b[j]
            result %= m
            j += 1
            k += 1
    print(result)
