def f(s, n):
    result = 0
    b = 1
    for c in s[::-1]:
        result += int(c) * b
        b *= n
    return result


INF = 10 ** 19

X = input()
M = int(input())

d = int(max(X))

ok = d
ng = INF + 1
while ng - ok > 1:
    m = ok + (ng - ok) // 2
    if f(X, m) <= M:
        ok = m
    else:
        ng = m

if ok == INF:
    print(1)
else:
    print(ok - d)
