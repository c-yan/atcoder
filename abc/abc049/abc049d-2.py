# DFS(深さ優先探索)
def create_links(N, K):
    links = [[] for _ in range(N)]
    for _ in range(K):
        p, q = map(int, input().split())
        links[p - 1].append(q - 1)
        links[q - 1].append(p - 1)
    return links


def create_groups(N, links):
    groups = list(range(N))
    for i in range(N):
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


N, K, L = map(int, input().split())

road_links = create_links(N, K)
rail_links = create_links(N, L)
road_groups = create_groups(N, road_links)
rail_groups = create_groups(N, rail_links)

d = {}
for i in range(N):
    t = (road_groups[i], rail_groups[i])
    if t in d:
        d[t] += 1
    else:
        d[t] = 1

print(*[d[(road_groups[i], rail_groups[i])] for i in range(N)])
