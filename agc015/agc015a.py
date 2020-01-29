N, A, B = map(int, input().split())

if A > B or (N == 1 and A != B):
    print(0)
else:
    lower = (N - 1) * A + B
    upper = (N - 1) * B + A
    print(upper - lower + 1)
