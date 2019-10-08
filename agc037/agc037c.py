def main():
    from sys import exit

    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = 0
    q = [i for i in range(N) if B[i] != A[i]]
    while len(q) != 0:
        nq = []
        c = 0
        for i in q:
            if i == 0 or i == N - 1:
                j = B[(N + i - 1) % N] + B[(N + i + 1) % N]
            else:
                j = B[i - 1] + B[i + 1]
            if j > B[i] - A[i]:
                nq.append(i)
                continue
            c += 1
            k = (B[i] - A[i]) // j
            result += k
            B[i] -= j * k
            if A[i] != B[i]:
                nq.append(i)
        if c == 0 and len(nq) != 0:
            print(-1)
            exit()
        q = nq
    print(result)


main()
