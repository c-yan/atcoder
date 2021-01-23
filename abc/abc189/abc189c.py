N, *A = map(int, open(0).read().split())

def f(x):
    result = 0
    i = 0
    j = 0
    while i < N:
        while j < N and x <= A[j]:
            j += 1
        result = max(result, x * (j - i))
        i = j + 1
        j = i
    return result

result = 0
for x in set(A):
    result = max(result, f(x))
print(result)
