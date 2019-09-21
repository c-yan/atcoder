n = int(input())
a = list(map(int, input().split()))
i = 0
while True:
    if any(e % 2 == 1 for e in a):
        break
    i += 1
    a = [e // 2 for e in a]
print(i)
