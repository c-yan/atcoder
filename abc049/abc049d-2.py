# 深さ優先探索版
from sys import stdin

def create_links(n, k):
  links = [[] for _ in range(n)]
  for i in range(k):
    p, q = map(int, stdin.readline().split())
    links[p - 1].append(q - 1)
    links[q - 1].append(p - 1)
  return links

def create_groups(n, links):
  groups = list(range(n))
  for i in range(n):
    if groups[i] != i:
      continue
    q = [i]
    while q:
      j = q.pop()
      for k in links[j]:
        if groups[k] != i:
          groups[k] = i
          q.append(k)
  return groups

n, k, l = map(int, input().split())
road_links = create_links(n, k)
rail_links = create_links(n, l)
road_groups = create_groups(n, road_links)
rail_groups = create_groups(n, rail_links)

d = {}
for i in range(n):
  t = (road_groups[i], rail_groups[i])
  if t in d:
    d[t] += 1
  else:
    d[t] = 1

print(*[d[(road_groups[i], rail_groups[i])] for i in range(n)])
