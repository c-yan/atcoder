n = int(raw_input())
a = [int(e) for e in raw_input().split()]
i = 0
while True:
  if any(e % 2 == 1 for e in a):
    break
  i += 1
  a = [e / 2 for e in a]
print i
