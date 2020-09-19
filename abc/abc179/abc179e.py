N, X, M = map(int, input().split())

existence = [0] * M
a = []
A = X
for i in range(N):
    if existence[A] != 0:
        break
    existence[A] = 1
    a.append(A)
    A = A * A % M

for i in range(len(a)):
    if a[i] == A:
        break
j = i

result = sum(a[:j])
a = a[j:]
N -= j
x = N // len(a)
y = N % len(a)
result += sum(a) * x + sum(a[:y])
print(result)
