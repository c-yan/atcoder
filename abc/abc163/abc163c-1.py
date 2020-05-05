N = int(input())
A = list(map(int, input().split()))

d = {}

for i in range(N - 1):
    if A[i] in d:
        d[A[i]].append(i + 2)
    else:
        d[A[i]] = [i + 2]

for i in range(1, N + 1):
    if i in d:
        print(len(d[i]))
    else:
        print(0)
