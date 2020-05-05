from collections import deque

N, D, A = map(int, input().split())
XH = [list(map(int, input().split())) for _ in range(N)]

XH.sort()
q = deque()
damage = 0
result = 0
for x, h in XH:
    while q:
        if x <= q[0][0]:
            break
        damage -= q.popleft()[1]
    h -= damage
    if h <= 0:
        continue
    c = (h + A - 1) // A
    result += c
    damage += c * A
    q.append((x + 2 * D, c * A))
print(result)
