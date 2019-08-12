from heapq import heappush, heappop
n, m = map(int, input().split())
jobs = {}
for _ in range(n):
  a, b = map(int, input().split())
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
