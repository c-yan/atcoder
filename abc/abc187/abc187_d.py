from sys import stdin

readline = stdin.readline

N = int(readline())
AB = [tuple(map(int, readline().split())) for _ in range(N)]

s = sum(a for a, _ in AB)
t = [a * 2 + b for a, b in AB]
t.sort(reverse=True)

c = 0
for i in range(N):
    c += t[i]
    if c > s:
        print(i + 1)
        break
