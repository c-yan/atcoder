from functools import cmp_to_key


def make_suffix_array(s):
    n = len(s)
    sa = list(range(n))
    rnk = [ord(c) for c in s]
    tmp = [0] * n
    k = 1
    while k < n:
        def cmp(x, y):
            if rnk[x] != rnk[y]:
                return rnk[x] - rnk[y]
            rx, ry = -1, -1
            if x + k < n:
                rx = rnk[x + k]
            if y + k < n:
                ry = rnk[y + k]
            return rx - ry
        sa.sort(key=cmp_to_key(cmp))
        tmp[sa[0]] = 0
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i - 1]]
            if cmp(sa[i - 1], sa[i]):
                tmp[sa[i]] += 1
        tmp, rnk = rnk, tmp
        k *= 2
    return sa


def make_lcp_array(s, sa):
    s = [ord(c) for c in s]
    n = len(s)
    rnk = [None] * n
    for i in range(n):
        rnk[sa[i]] = i
    lcp = [0] * (n - 1)
    h = 0
    for i in range(n):
        if h > 0:
            h -= 1
        if rnk[i] == 0:
            continue
        j = sa[rnk[i] - 1]
        while j + h < n and i + h < n:
            if s[j + h] != s[i + h]:
                break
            h += 1
        lcp[rnk[i] - 1] = h
    return lcp


S = input()
sa = make_suffix_array(S)

result = len(S) * (len(S) + 1) // 2
for x in make_lcp_array(S, sa):
    result -= x
print(result)
