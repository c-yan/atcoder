from collections import Counter


def is_ok(t):
    diff = 0
    pool = Counter(S)
    for i in range(len(t)):
        c = t[i]
        if S[i] != c:
            diff += 1
        pool[c] -= 1
        if pool[c] == 0:
            del pool[c]
    for i in range(len(t), N):
        c = S[i]
        if c in pool:
            pool[c] -= 1
            if pool[c] == 0:
                del pool[c]
        else:
            diff += 1
    return diff <= K


N, K = map(int, input().split())
S = input()

pool = Counter(S)
result = ''
for i in range(N):
    for c in sorted(pool):
        if not is_ok(result + c):
            continue
        result += c
        pool[c] -= 1
        if pool[c] == 0:
            del pool[c]
        break
print(result)
