N = int(input())

o = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
t = [False] * 366
for i in range(0, 366, 7):
    t[i] = True
for i in range(6, 366, 7):
    t[i] = True
for _ in range(N):
    m, d = map(int, input().split('/'))
    x = o[m - 1] + d - 1
    while x < 366 and t[x]:
        x += 1
    if x < 366:
        t[x] = True

result = 0
l = 0
for x in t:
    if x:
        l += 1
    else:
        l = 0
    result = max(result, l)
print(result)
