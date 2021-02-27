def f(cards):
    c = {}
    for i in range(1, 10):
        c[i] = 0
    for i in cards:
        c[i] += 1
    result = 0
    for k in c:
        result += k * pow(10, c[k])
    return result


K = int(input())
S = input()
T = input()

all = {}
for i in range(1, 10):
    all[i] = K

s = list(map(int, S[:4]))
t = list(map(int, T[:4]))

for i in s:
    all[i] -= 1
for i in t:
    all[i] -= 1

x = 9 * K - 8

result = 0
for i in range(1, 10):
    if all[i] == 0:
        continue
    a = all[i] / x
    all[i] -= 1
    k = f(s + [i])
    for j in range(1, 10):
        if all[j] == 0:
            continue
        b = all[j] / (x - 1)
        l = f(t + [j])
        if k > l:
            result += a * b
    all[i] += 1
print(result)
