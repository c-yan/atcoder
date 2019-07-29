import sys
s = raw_input()
ts = ['']
while True:
  nts= []
  for t in ts:
    for w in ['dreamer', 'eraser', 'dream', 'erase']:
      if s == t + w:
        print 'YES'
        sys.exit()
      if s.startswith(t + w):
        nts.append(t + w)
  if len(nts) == 0:
    print 'NO'
    sys.exit()
  ts = nts
