def main():
    from itertools import combinations

    N, M, P, Q, R = map(int, input().split())
    xyz = [tuple(map(int, input().split())) for _ in range(R)]

    result = 0
    for c in combinations(range(1, N + 1), P):
        s = set(c)
        t = [0] * (M + 1)
        for x, y, z in xyz:
            if x in s:
                t[y] += z
        t.sort(reverse=True)
        result = max(result, sum(t[:Q]))
    print(result)


main()
