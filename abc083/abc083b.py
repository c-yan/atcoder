n, a, b = [int(e) for e in raw_input().split()]
result = 0
for i in range(1, n + 1):
  if a <= sum(int(e) for e in str(i)) <= b:
    result += i
print result
