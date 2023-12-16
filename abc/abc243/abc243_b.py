N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

c = 0
for i in range(N):
    if A[i] == B[i]:
        c += 1
print(c)

c = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if A[i] == B[j]:
            c += 1
print(c)
