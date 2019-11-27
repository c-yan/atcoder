a, b, x = map(int, input().split())

n = (a + x - 1) // x * x
print((b - n) // x + 1)
