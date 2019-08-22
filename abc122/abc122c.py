from sys import stdin
def main():
  readline = stdin.readline
  n, q = map(int, readline().split())
  s = input()
  c = [0] * (n + 1)
  for i in range(2, n + 1):
    if s[i - 1] == 'C' and s[i - 2] == 'A':
      c[i] = c[i - 1] + 1
    else:
      c[i] = c[i - 1]
  for _ in range(q):
    l, r = map(int, readline().split())
    t = c[r] - c[l - 1]
    if l >= 2 and s[l - 2: l] == 'AC':
      t -= 1
    print(t)
main()
