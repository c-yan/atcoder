from collections import deque

N = int(input())
b = list(map(int, input().split()))

result = deque([])
while b:
    for i in range(len(b) - 1, -1, -1):
        if b[i] == i + 1:
            result.appendleft(b.pop(i))
            break
    else:
        break

if not b:
    print('\n'.join(str(i) for i in result))
else:
    print(-1)
