import sys
def main():
  _ord, _range = ord, range
  s = input()
  t = input()
  tset = set(t)
  slen = len(s)
  aord = _ord('a')
  if len(tset - set(s)) != 0:
      print(-1)
      sys.exit()
  s2t = [i - aord for i in (s + s).encode('ascii')]
  lut = [[-1 for _ in _range(slen)] for _ in _range(26)]
  for c in tset:
    b = _ord(c) - aord
    j = 0
    for i in _range(slen * 2 - 1, -1, -1):
      if s2t[i] == b:
        j = 0
      else:
        j += 1
      if i < slen:
        lut[b][i] = j
  p = 0
  for c in t:
    b = _ord(c) - aord
    p += lut[b][p % slen] + 1
  print(p)
main()
