N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

for x in [A, B, C]:
    x.sort()

i = -1
j = 0
result = 0
for b in B:
    while i < N - 1 and A[i + 1] < b:
        i += 1
    while j < N and C[j] <= b:
        j += 1
    result += (i + 1) * (N - j)
print(result)
