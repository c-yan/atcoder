s = input()
h = int(s[:2])
l = int(s[2:])
def mmok(i):
  return 1 <= i <= 12
if mmok(h):
  if mmok(l):
    print('AMBIGUOUS')
  else:
    print('MMYY')
else:
  if mmok(l):
    print('YYMM')
  else:
    print('NA')
