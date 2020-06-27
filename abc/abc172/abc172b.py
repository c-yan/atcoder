S = input()
T = input()

result = 0
for i in range(len(S)):
    if S[i] == T[i]:
        continue
    result += 1
print(result)
