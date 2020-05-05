S = input()

result = 0
p = S[0]
for i in range(1, len(S)):
    if p != S[i]:
        result += 1
        p = S[i]
print(result)
