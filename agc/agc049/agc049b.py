N = int(input())
S = list(input())
T = list(input())

result = 0
j = 0
for i in range(N):
    if S[i] == T[i]:
        continue

    try:
        j = S.index('1', max(j, i + 1))
    except:
        print(-1)
        exit()

    if j != i + 1:
        S[i + 1], S[j] = S[j], S[i + 1]
        result += j - (i + 1)

    if S[i] == '0':
        S[i] = '1'
    elif S[i] == '1':
        S[i] = '0'
    S[i + 1] = '0'
    result += 1
print(result)
