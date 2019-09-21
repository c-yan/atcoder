from sys import stdin
def main():
  from builtins import int, range
  readline = stdin.readline
  n, w = map(int, readline().split())
  maxv = 10 ** 3 * n + 1
  t = [-1] * maxv
  t[0] = w
  cmaxv = 0
  for _ in range(n):
    nw, nv = map(int, readline().split())
    for i in range(cmaxv, -1, -1):
      ti = t[i]
      if ti == -1:
        continue
      if t[i + nv] < ti - nw:
        t[i + nv] = ti - nw
        if cmaxv < i + nv:
          cmaxv = i + nv
  print(cmaxv)
main()
