N = int(input())
A = [int(input()) for _ in range(N)]

b = A[:]
b.sort(reverse=True)
for i in range(N):
    if A[i] != b[0]:
        print(b[0])
    else:
        print(b[1])
