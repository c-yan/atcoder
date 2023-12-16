N, L = map(int, input().split())

a = []
for _ in range(L):
    t = input()
    i = 0
    while True:
        j = t.find('-', i)
        if j == -1:
            break
        i = j + 1
        a.append(j // 2)
y = input()
result = y.find('o') // 2
for i in reversed(a):
    if result == i:
        result += 1
    elif result == i + 1:
        result -= 1
print(result + 1)
