from itertools import accumulate


def main():
    N, S = input().split()
    N = int(N)

    a = [0] * (N + 1)
    g = [0] * (N + 1)
    c = [0] * (N + 1)
    t = [0] * (N + 1)

    for i in range(N):
        x = S[i]
        if x == 'A':
            a[i + 1] = 1
        elif x == 'G':
            g[i + 1] = 1
        elif x == 'C':
            c[i + 1] = 1
        elif x == 'T':
            t[i + 1] = 1

    a = list(accumulate(a))
    g = list(accumulate(g))
    c = list(accumulate(c))
    t = list(accumulate(t))

    result = 0
    for i in range(N):
        for j in range(i + 2, N + 1, 2):
            k = a[j] - a[i]
            l = g[j] - g[i]
            m = c[j] - c[i]
            n = t[j] - t[i]
            if k == n and l == m:
                result += 1
    print(result)


main()
