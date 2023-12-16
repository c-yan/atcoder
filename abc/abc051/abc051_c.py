sx, sy, tx, ty = map(int, input().split())

dx = tx - sx
dy = ty - sy

result = ''
result += 'R' * dx + 'U' * dy  # 1st Forth
result += 'L' * dx + 'D' * dy  # 1st Back
result += 'D' + 'R' * (dx + 1) + 'U' * (dy + 1) + 'L'  # 2nd Forth
result += 'U' + 'L' * (dx + 1) + 'D' * (dy + 1) + 'R'  # 2nd Back
print(result)
