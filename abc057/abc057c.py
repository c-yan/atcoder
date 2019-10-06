from math import sqrt


def F(A, B):
    return max(len(str(A)), len(str(B)))


N = int(input())

for i in range(int(sqrt(N)), 0, -1):
    if N % i == 0:
        print(F(i, N // i))
        break
