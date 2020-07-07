N, A, B = map(int, input().split())

if N <= 5:
    print(B * N)
else:
    print(A * (N - 5) + B * 5)
