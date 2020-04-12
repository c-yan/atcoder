def main():
    N = int(input())
    S = input()

    rcs = [0] * N
    gcs = [0] * N
    bcs = [0] * N

    for i in range(N):
        if S[i] == 'R':
            rcs[i] = 1
        elif S[i] == 'G':
            gcs[i] = 1
        elif S[i] == 'B':
            bcs[i] = 1

    for i in range(1, N):
        rcs[i] += rcs[i - 1]
        gcs[i] += gcs[i - 1]
        bcs[i] += bcs[i - 1]

    result = 0
    for i in range(N):
        if S[i] == 'R':
            for j in range(i + 1, N):
                if S[j] == 'R':
                    continue
                elif S[j] == 'G':
                    result += bcs[N - 1] - bcs[j]
                    t = 2 * j - i
                    if t < N and S[t] == 'B':
                        result -= 1
                elif S[j] == 'B':
                    result += gcs[N - 1] - gcs[j]
                    t = 2 * j - i
                    if t < N and S[t] == 'G':
                        result -= 1
        elif S[i] == 'G':
            for j in range(i + 1, N):
                if S[j] == 'G':
                    continue
                elif S[j] == 'R':
                    result += bcs[N - 1] - bcs[j]
                    t = 2 * j - i
                    if t < N and S[t] == 'B':
                        result -= 1
                elif S[j] == 'B':
                    result += rcs[N - 1] - rcs[j]
                    t = 2 * j - i
                    if t < N and S[t] == 'R':
                        result -= 1
        elif S[i] == 'B':
            for j in range(i + 1, N):
                if S[j] == 'B':
                    continue
                elif S[j] == 'R':
                    result += gcs[N - 1] - gcs[j]
                    t = 2 * j - i
                    if t < N and S[t] == 'G':
                        result -= 1
                elif S[j] == 'G':
                    result += rcs[N - 1] - rcs[j]
                    t = 2 * j - i
                    if t < N and S[t] == 'R':
                        result -= 1
    print(result)


main()
