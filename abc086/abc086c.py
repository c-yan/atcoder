import sys
n = int(raw_input())
data = [map(int, raw_input().split()) for i in range(n)]
t = 0
x = 0
y = 0
for d in data:
  duration = d[0] - t
  distance = abs(x - d[1]) + abs(y - d[2])
  if (distance > duration) or ((duration - distance) % 2 == 1):
    print 'No'
    sys.exit()
  t = d[0]
  x = d[1]
  y = d[2]
print 'Yes'
