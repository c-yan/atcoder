N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

result = T[:]
for _ in range(2):
    for i in range(N):
        j = (i + 1) % N
        x = result[i] + S[i]
        if result[j] > x:
            result[j] = x
print(*result, sep='\n')
