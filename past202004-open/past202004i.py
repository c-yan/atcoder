N = int(input())
A = list(map(int, input().split()))

result = [1] * (2 ** N)
t = [(i, A[i]) for i in range(2 ** N)]
while len(t) != 1:
    nt = []
    for i in range(0, len(t), 2):
        ai, aj = t[i]
        bi, bj = t[i + 1]
        if aj > bj:
            result[ai] += 1
            nt.append(t[i])
        else:
            result[bi] += 1
            nt.append(t[i + 1])
    t = nt
result[t[0][0]] -= 1

for i in result:
    print(i)
