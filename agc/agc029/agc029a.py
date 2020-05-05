S = input()

bc = 0
result = 0
for i in range(len(S)):
    if S[i] == 'B':
        bc += 1
    if S[i] == 'W':
        result += bc
print(result)
