N = int(input())
S = input()

p = ''
result = 0
for i in range(N):
    if p != S[i]:
        result += 1
        p = S[i]
print(result)
