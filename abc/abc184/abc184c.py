r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

if abs(r1 - r2) + abs(c1 - c2) == 0:
    print(0)
    exit()

# Move
if abs(r1 - r2) + abs(c1 - c2) <= 3:
    print(1)
    exit()

r3 = r2
t = abs(r1 - r2)
if abs(c1 + t - c2) < abs(c1 - t - c2):
    c3 = c1 + t
else:
    c3 = c1 - t

# Bishop warp
if c3 == c2:
    print(1)
    exit()

# Move + Move
if abs(r1 - r2) + abs(c1 - c2) <= 6:
    print(2)
    exit()

# Bishop warp + Move
if abs(r3 - r2) + abs(c3 - c2) <= 3:
    print(2)
    exit()

# Bishop warp + Bishop warp
if (r1 + c1) % 2 == (r2 + c2) % 2:
    print(2)
    exit()

# Bishop warp + Bishop warp + Move
print(3)
