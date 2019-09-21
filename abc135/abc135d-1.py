def main():
  s = input()[::-1]
  multiplier = 1
  divisor = 10 ** 9 + 7
  list10 = list(range(10))
  list13 = list(range(13))
  p = [0] * 13
  np = [0] * 13
  rt = [i % 13 for i in range(121)]
  p[0] = 1
  for i in range(len(s)):
    if s[i] != '?':
      r = rt[int(s[i]) * multiplier]
      for j in list13:
        np[rt[j + r]] = p[j]
    else:
      r = 0
      for j in list10:
        for k in list13:
          np[rt[k + r]] += p[k]
        r = rt[r + multiplier]
    for j in list13:
      p[j] = np[j] % divisor
      np[j] = 0
    multiplier = rt[10 * multiplier]
  print(p[5])
main()
