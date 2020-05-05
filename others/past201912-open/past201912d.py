N = int(input())
A = [int(input()) for _ in range(N)]

t = set(A)
if len(t) == N:
    print('Correct')
    exit()

d = {}
for i in range(N):
    if A[i] in d:
        d[A[i]] += 1
    else:
        d[A[i]] = 1

for i in range(1, N + 1):
    if i not in d:
        x = i
    elif d[i] == 2:
        y = i

print(y, x)
