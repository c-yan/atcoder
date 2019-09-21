def main():
    import sys
    _int = int
    n = _int(input())
    a = [_int(e) for e in input().split()]
    b = [_int(e) for e in input().split()]
    result = 0
    q = [i for i in range(n) if b[i] != a[i]]
    while len(q) != 0:
        nq = []
        c = 0
        for i in q:
            if i == 0 or i == n - 1:
                j = b[(n + i - 1) % n] + b[(n + i + 1) % n]
            else:
                j = b[i - 1] + b[i + 1]
            if j > b[i] - a[i]:
                nq.append(i)
                continue
            c += 1
            k = (b[i] - a[i]) // j
            result += k
            b[i] -= j * k
            if a[i] != b[i]:
                nq.append(i)
        if c == 0 and len(nq) != 0:
            print(-1)
            sys.exit()
        q = nq
    print(result)


main()
