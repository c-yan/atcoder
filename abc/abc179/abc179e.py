N, X, M = map(int, input().split())

existence = [False] * M
a = []
A = X
for i in range(N):
    if existence[A]:
        break
    existence[A] = True
    a.append(A)
    A = A * A % M

for i in range(len(a)):
    if a[i] == A:
        break
loop_start = i

result = sum(a[:loop_start])
a = a[loop_start:]
N -= loop_start
loops = N // len(a)
remainder = N % len(a)
result += sum(a) * loops + sum(a[:remainder])
print(result)
