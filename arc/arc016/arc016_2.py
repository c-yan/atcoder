N = int(input())

t = [False] * 9
result = 0
for _ in range(N):
    x = input()
    for i in range(9):
        if t[i]:
            if x[i] == 'o':
                continue
            result += 1
            t[i] = False
        if x[i] == 'x':
            result += 1
        elif x[i] == 'o':
            t[i] = True
result += t.count(True)
print(result)
