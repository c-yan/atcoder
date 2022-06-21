N, *A = map(int, open(0).read().split())

result = N
t = 0
for a in reversed(A):
    t += A
    if t >= 4:
        break
    result -= 1
print(result)
