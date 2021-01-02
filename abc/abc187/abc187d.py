N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

s = sum(a for a, _ in AB)
t = [a * 2 + b  for a, b in AB]
t.sort(reverse=True)

c = 0
for i in range(N):
    c += t[i]
    if c > s:
        print(i + 1)
        break
