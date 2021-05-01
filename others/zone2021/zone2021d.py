from collections import deque

S = input()

T = deque([])
is_reversed = False

for c in S:
    if c == 'R':
        is_reversed = not is_reversed
        continue

    if is_reversed:
        if len(T) != 0 and T[0] == c:
            T.popleft()
        else:
            T.appendleft(c)
    else:
        if len(T) != 0 and T[-1] == c:
            T.pop()
        else:
            T.append(c)

if is_reversed:
    T = reversed(T)
print(''.join(T))
