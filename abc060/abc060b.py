A, B, C = map(int, input().split())

a = 0
t = set()

while True:
    a += A
    a %= B
    if a in t:
        print('NO')
        break
    if a == C:
        print('YES')
        break
    t.add(a)
