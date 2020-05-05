N = int(input())
A = [int(input()) for _ in range(N)]

prev = A[0]
for i in range(1, N):
    if A[i] == prev:
        print('stay')
    elif A[i] < prev:
        print('down %d' % (prev - A[i]))
    elif A[i] > prev:
        print('up %d' % (A[i] - prev))
    prev = A[i]
