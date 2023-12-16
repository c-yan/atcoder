A, B, W = map(int, input().split())

w = W * 1000
min_x = (w + B - 1) // B
max_x = w // A
if w < min_x * A or w > max_x * B:
    print('UNSATISFIABLE')
    exit()
print(min_x, max_x)
