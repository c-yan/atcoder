A, B, C, D, E, F = map(int, input().split())

w = set()
for i in range(F // (100 * A) + 1):
    for j in range((F - 100 * A * i) // (100 * B) + 1):
        w.add((A * i + B * j) * 100)
w.remove(0)

s = set()
t = E * F // 100
for i in range(t // C + 1):
    for j in range((t - C * i) // D + 1):
        s.add(C * i + D * j)

best_concentration = -1
best_a = -1
best_b = -1
for a in w:
    for b in sorted(s):
        if a + b > F:
            break
        if b > E * a // 100:
            break
        concentration = 100 * b / (a + b)
        if concentration > best_concentration:
            best_concentration = concentration
            best_a = a
            best_b = b
print(best_a + best_b, best_b)
