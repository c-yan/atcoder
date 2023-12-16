A, B, C = map(int, input().split())

if any(i % 2 == 0 for i in [A, B, C]):
    print(0)
else:
    t = [A, B, C]
    t.sort()
    print(t[0] * t[1])
