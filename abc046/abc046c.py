N = int(input())

t, a = 1, 1
for _ in range(N):
    T, A = map(int, input().split())
    t = (t + (T - 1)) // T * T
    a = (a + (A - 1)) // A * A
    if a < t * A // T:
        a = t * A // T
    else:
        t = a * T // A
print(a + t)
