def main():
    N, S = input().split()
    N = int(N)

    result = 0
    for i in range(N):
        a, b = 0, 0
        for c in S[i:]:
            if c == 'A':
                a += 1
            elif c == 'T':
                a -= 1
            elif c == 'C':
                b += 1
            elif c == 'G':
                b -= 1
            if a == 0 and b == 0:
                result += 1
    print(result)


main()
