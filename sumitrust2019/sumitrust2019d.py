N = int(input())
S = input()

t = [S[0]]
p = S[0]
r = 1
for i in range(1, N):
    if S[i] == p:
        r += 1
        if r < 4:
            t.append(S[i])
    else:
        r = 1
        t.append(S[i])
T = ''.join(t)

result = 0
for i in range(10):
    a = T.find(str(i))
    if a == -1:
        continue
    for j in range(10):
        b = T.find(str(j), a + 1)
        if b == -1:
            continue
        for k in range(10):
            if T.find(str(k), b + 1) != -1:
                result += 1
print(result)
