from collections import deque

S = input()
Q = int(input())

t = deque(S)
reverse = False
for _ in range(Q):
    query = input()
    if query[0] == '1':
        reverse = not reverse
    elif query[0] == '2':
        _, F, C = query.split()
        if F == '1':
            if reverse:
                t.append(C)
            else:
                t.appendleft(C)
        elif F == '2':
            if reverse:
                t.appendleft(C)
            else:
                t.append(C)
result = ''.join(t)
if reverse:
    result = result[::-1]
print(result)
