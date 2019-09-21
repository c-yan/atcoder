from sys import exit
s = input()[::-1]
while True:
  if s == '':
    print('YES')
    exit()
  for w in ['maerd', 'remaerd', 'esare', 'resare']:
    if s.startswith(w):
      s = s[len(w):]
      break
  else:
    print('NO')
    exit()
