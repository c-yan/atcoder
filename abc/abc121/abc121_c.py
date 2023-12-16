from sys import stdin


def main():
    from builtins import int, list, map, min
    readline = stdin.readline
    n, m = map(int, readline().split())
    data = [list(map(int, readline().split())) for _ in range(n)]
    data.sort(key=lambda x: x[0])
    purchased = 0
    amount = 0
    for a, b in data:
        t = min(m - purchased, b)
        amount += t * a
        purchased += t
        if purchased == m:
            break
    print(amount)


main()
