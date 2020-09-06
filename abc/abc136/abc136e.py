def make_divisor_list(n):
    result = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.append(i)
            result.append(n // i)
    return result


def calc_min_ops(r, d):
    i, j = 0, len(r)
    while i < j and r[i] == 0:
        i += 1
    i -= 1
    a, b = 0, 0
    while j-i != 1:
        if a <= b:
            i += 1
            a += r[i]
        else:
            j -= 1
            b += d - r[j]
    return a


N, K, *A = map(int, open(0).read().split())

c = sum(A)
divisors = make_divisor_list(c)
divisors.sort(reverse=True)
r = [None] * N

for d in divisors:
    for i in range(N):
        r[i] = A[i] % d
    r.sort()
    if calc_min_ops(r, d) <= K:
        print(d)
        break
