from collections import deque

S = input()

q = deque([])
is_reversed = False

for c in S:
    if c == 'R':
        is_reversed = not is_reversed
        continue

    if is_reversed:
        q.appendleft(c)
    else:
        q.append(c)

if is_reversed:
    q = reversed(q)

t = []
for c in q:
    if len(t) != 0 and t[-1] == c:
        t.pop()
    else:
        t.append(c)
print(''.join(t))
