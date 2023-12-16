N, L = map(int, input().split())
x = set(map(int, input().split()))
T1, T2, T3 = map(int, input().split())

t = [float('inf')] * (L + 4)
t[0] = 0
for i in range(L):
    a = t[i]
    if i in x:
        a += T3
    if t[i + 1] > a + T1:
        t[i + 1] = a + T1
    if t[i + 2] > a + T1 + T2:
        t[i + 2] = a + T1 + T2
    if t[i + 4] > a + T1 + T2 * 3:
        t[i + 4] = a + T1 + T2 * 3

result = t[L]
a = t[L - 1]
if L - 1 in x:
    a += T3
result = min(result, a + T1 // 2 + T2 // 2)

a = t[L - 2]
if L - 2 in x:
    a += T3
result = min(result, a + T1 // 2 + 3 * T2 // 2)

a = t[L - 3]
if L - 3 in x:
    a += T3
result = min(result, a + T1 // 2 + 5 * T2 // 2)

print(result)
