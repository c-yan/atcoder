A, B, C = map(int, input().split())

t = sorted([A, B, C])
print(t[0] + t[1] + t[2] * 10)
