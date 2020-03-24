def comb(n, k):
    if n - k < k:
        k = n - k
    if k == 0:
        return 1
    a = 1
    b = 1
    for i in range(k):
        a *= n - i
        b *= i + 1
    return a // b


N, P = map(int, input().split())
A = list(map(int, input().split()))

odds = sum(a % 2 for a in A)
evens = len(A) - odds

print(sum(comb(odds, i) for i in range(P, odds + 1, 2)) * (2 ** evens))
