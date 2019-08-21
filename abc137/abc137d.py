from sys import stdin
def main():
  from builtins import int, map, range
  readline = stdin.readline
  from heapq import heappush, heappop
  n, m = map(int, readline().split())
  jobs = {}
  for _ in range(n):
    a, b = map(int, readline().split())
    if a > m:
      continue
    if a in jobs:
      jobs[a].append(b)
    else:
      jobs[a] = [b]
  result = 0
  candidates = []
  for a in range(1, m + 1):
    if a in jobs:
      for b in jobs[a]:
        heappush(candidates, -b)
    else:
      if len(candidates) == 0:
        continue
    result += -heappop(candidates)
  print(result)
main()
