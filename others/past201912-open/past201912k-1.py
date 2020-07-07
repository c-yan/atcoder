N = int(input())

root = -1
children = [[] for _ in range(N + 1)]
left = [0] * (N + 1)
right = [0] * (N + 1)

for i in range(1, N + 1):
    p = int(input())
    if p == -1:
        root = i
    else:
        children[p].append(i)

i = 0
s = [root]
while s:
    n = s.pop()
    if n > 0:
        left[n] = i
        i += 1
        s.append(-n)
        for c in children[n]:
            s.append(c)
    else:
        right[-n] = i

Q = int(input())
result = []
for _ in range(Q):
    a, b = map(int, input().split())
    if left[b] < left[a] < right[b]:
        result.append('Yes')
    else:
        result.append('No')
print(*result, sep='\n')
