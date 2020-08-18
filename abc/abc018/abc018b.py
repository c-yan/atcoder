S = input()
N = int(input())

t = list(S)
for _ in range(N):
    l, r = map(lambda e: int(e) - 1, input().split())
    for i in range((r - l + 1) // 2):
        t[l + i], t[r - i] = t[r - i], t[l + i]
print(''.join(t))
