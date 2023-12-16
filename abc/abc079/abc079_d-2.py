# ワーシャルフロイド
from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall

H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
c = floyd_warshall(csgraph_from_dense(c))

result = 0
for _ in range(H):
    for i in map(int, input().split()):
        if i == -1:
            continue
        result += c[i][1]
print(int(result))
