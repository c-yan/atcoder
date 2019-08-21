from sys import stdin
def main():
  from builtins import range
  readline = stdin.readline
  h, w = map(int, readline().split())
  s = [readline().rstrip('\r\n') + '#' for _ in range(h)]
  s.append('#' * w)
  yoko = [[0] * w for _ in range(h)]
  for i in range(h):
    start = -1
    si = s[i]
    yokoi = yoko[i]
    for j in range(w + 1):
      if si[j] == '#':
        if start != -1:
          t = j - start
          for k in range(start, j):
            yokoi[k] = t
          start = -1
      else:
        if start == -1:
          start = j
  result = 0
  for i in range(w):
    start = -1
    for j in range(h + 1):
      if s[j][i] == '#':
        if start != -1:
          t = yoko_max + j - start - 1
          if t > result:
            result = t
          start = -1
      else:
        yji = yoko[j][i]
        if start == -1:
          start = j
          yoko_max = yji
        else:
          if yji > yoko_max:
            yoko_max = yji
  print(result)
main()
