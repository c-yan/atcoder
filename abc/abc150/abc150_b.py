N = int(input())
S = input()

result = 0
for i in range(N):
    if S[i:i+3] == 'ABC':
        result += 1
print(result)
