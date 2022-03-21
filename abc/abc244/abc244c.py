N = int(input())

s = set(range(1, 2 * N + 2))
while True:
    print(s.pop())
    x = int(input())
    if x == 0:
        break
    s.remove(x)
