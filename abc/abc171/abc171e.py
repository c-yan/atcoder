N = int(input())
a = list(map(int, input().split()))

t = 0
for e in a:
    t ^= e

print(*[e ^ t for e in a])
