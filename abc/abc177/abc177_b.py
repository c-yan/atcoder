S = input()
T = input()

result = float('inf')
for i in range(len(S) - len(T) + 1):
    t = 0
    for j in range(len(T)):
        if S[i + j] != T[j]:
            t += 1
    result = min(result, t)
print(result)
