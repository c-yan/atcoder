N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()

result = 10 ** 9
i = 0
for a in sorted(A):
    while i != M and B[i] < a:
        i += 1
    if i != 0:
        result = min(result, abs(a - B[i - 1]))
    if i != M:
        result = min(result, abs(a - B[i]))
print(result)
