s = input()
t = list(s.encode('us-ascii'))
t.sort()
if t[0] == t[1] and t[2] == t[3] and t[0] != t[2]:
  print('Yes')
else:
  print('No')
