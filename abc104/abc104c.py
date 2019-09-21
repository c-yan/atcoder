INF = float('inf')
d, g = map(int, input().split())
data = []
calced = set()
for i in range(d):
    p, c = map(int, input().split())
    data.append([p, c, (i + 1) * 100, (i + 1) * 100 * p + c])


def f(data, total, targets):
    if total <= 0:
        return 0
    result = INF
    for i in range(len(targets)):
        p, _, score, subtotal = data[targets[i]]
        t = (total + score - 1) // score
        if t < p and t < result:
            result = t
        nt = tuple(targets[0:i] + targets[i + 1:])
        if nt not in calced:
            calced.add(nt)
            t = p + f(data, total - subtotal, nt)
            if t < result:
                result = t
    calced.add(targets)
    return result


print(f(data, g, tuple(range(len(data)))))
