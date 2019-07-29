a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
x = int(raw_input())

result = 0
for i in range(a + 1):
  for j in range(b + 1):
    for k in range(c + 1):
      if i * 500 + j * 100 + k * 50 == x:
        result += 1

print result
