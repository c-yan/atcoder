def to_id(y, x):
    return y * 8 + x


def to_coordinate(x):
    return x // 8, x % 8


def remove_unusable(y, x, t):
    result = set(t)
    for n in range(8):
        k = to_id(n, x)
        if k in result:
            result.remove(k)
        k = to_id(y, n)
        if k in result:
            result.remove(k)
    for n in range(1, 8):
        if y - n >= 0 and x - n >= 0:
            k = to_id(y - n, x - n)
            if k in result:
                result.remove(k)
        if y - n >= 0 and x + n < 8:
            k = to_id(y - n, x + n)
            if k in result:
                result.remove(k)
        if y + n < 8 and x - n >= 0:
            k = to_id(y + n, x - n)
            if k in result:
                result.remove(k)
        if y + n < 8 and x + n < 8:
            k = to_id(y + n, x + n)
            if k in result:
                result.remove(k)
    return sorted(result)


def try_place(n, t):
    if n == 8 and len(t) != 0:
        return {t[0]}
    for k in t:
        y, x = to_coordinate(k)
        ret = try_place(n + 1, remove_unusable(y, x, t))
        if ret is None:
            continue
        ret.add(k)
        return ret
    else:
        return None


c = [input() for _ in range(8)]

result = set()
t = list(range(64))
for y in range(8):
    for x in range(8):
        if c[y][x] != 'Q':
            continue
        if to_id(y, x) not in t:
            print('No Answer')
            exit()
        t = remove_unusable(y, x, t)
        result.add(to_id(y, x))

ret = try_place(4, t)
if ret is None:
    print('No Answer')
    exit()

result = result | ret
for y in range(8):
    s = ''
    for x in range(8):
        if to_id(y, x) in result:
            s += 'Q'
        else:
            s += '.'
    print(s)
