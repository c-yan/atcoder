A, B = map(int, input().split())

x_low = (A * 100 + 7) // 8
x_high = ((A + 1) * 100 + 7) // 8 - 1
y_low = (B * 100 + 9) // 10
y_high = ((B + 1) * 100 + 9) // 10 - 1

result = max(x_low, y_low)
if result > min(x_high, y_high):
    result = -1
print(result)
