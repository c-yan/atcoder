from collections import deque

first, last = input().split()

if first == last:
    print(0)
    print(first)
    print(last)
    exit()

N = int(input())
s = [input() for _ in range(N)]
s.append(last)


def is_movable(a, b):
    d = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        d += 1
        if d > 1:
            break
    return d == 1


previous = {first: None}
q = deque([first])
while q:
    a = q.popleft()
    for b in s:
        if b in previous:
            continue
        if not is_movable(a, b):
            continue
        q.append(b)
        previous[b] = a

if last not in previous:
    print(-1)
    exit()

a = last
t = [last]
while previous[a] is not None:
    t.append(previous[a])
    a = previous[a]
result = t[::-1]
print(len(result) - 2)
print(*result, sep='\n')
