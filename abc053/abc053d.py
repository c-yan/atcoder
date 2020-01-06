N = int(input())
A = list(map(int, input().split()))

t = len(set(A))
if (len(A) - t) % 2 == 0:
    print(t)
else:
    print(t - 1)
