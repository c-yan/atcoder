# 1. 3つとも違う数字
#  => 小さいふたつを + 1
# 2. 2つ同じ数字
#  => 1つだけの数字が小さい
#     小さい数字を + 2
#  => 1つだけの数字が大きい
#     小さいふたつを + 1
a, b, c = map(int, input().split())
result = 0
while True:
  if a == b and b == c:
    break
  elif a != b and b != c and a != c:
    if a < b:
      if b < c:
        a += 1
        b += 1
      else:
        a += 1
        c += 1
    else:
      if a < c:
        a += 1
        b += 1
      else:
        b += 1
        c += 1
  else:
    if a == b:
      if a > c:
        c += 2
      else:
        a += 1
        b += 1
    elif b == c:
      if a > b:
        b += 1
        c += 1
      else:
        a += 2
    else:
      # a == c
      if a > b:
        b += 2
      else:
        a += 1
        c += 1
  result += 1
print(result)
