def next_diverse_word(s):
    alphabets = set(chr(ord('a') + i) for i in range(26))
    if s == 'zyxwvutsrqponmlkjihgfedcba':
        return -1
    r = alphabets - set(s)
    if len(r) != 0:
        return s + sorted(r)[0]
    s = list(s)
    r = [s[-1]]
    s = s[:-1]
    while True:
        k = s[-1]
        r.append(s[-1])
        s = s[:-1]
        t = [c for c in r if c > k]
        if len(t) != 0:
            s.append(sorted(t)[0])
            return ''.join(s)


S = input()
print(next_diverse_word(S))
