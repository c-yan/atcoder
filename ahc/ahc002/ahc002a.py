def main():
    from time import time
    from heapq import heappush, heappop

    start = time()

    si, sj = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(50)]
    p = [list(map(int, input().split())) for _ in range(50)]

    def is_time_ok():
        return time() - start < 1.95

    best_scores = [[-1] * 50 for _ in range(50)]
    best_score = 0
    best_result = ''
    q = [(si, sj, 0, '', set([t[si][sj]]))]
    while q and is_time_ok():
        i, j, score, result, used = heappop(q)
        if -score > best_score:
            best_result = result
        for di, dj, s in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
            ni, nj = i + di, j + dj
            if ni < 0 or ni > 49 or nj < 0 or nj > 49:
                continue
            if t[ni][nj] in used:
                continue
            nscore = score - p[ni][nj]
            bs = best_scores[ni][nj]
            if -nscore < bs - 135:
                continue
            best_scores[ni][nj] = max(bs, -nscore)
            nresult = result + s
            nused = used | set([t[ni][nj]])
            heappush(q, (ni, nj, nscore, nresult, nused))
    print(best_result)


main()
