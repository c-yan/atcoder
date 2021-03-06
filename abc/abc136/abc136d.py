S = input()

n = len(S)
result = [0] * n
start = 0
c = 'R'
for i in range(1, n):
    if S[i] != c:
        if c == 'R':
            result[i - 1] += (i - start) // 2 + (i - start) % 2
            result[i] += (i - start) // 2
            c = 'L'
        else:
            result[start] += (i - start) // 2 + (i - start) % 2
            result[start - 1] += (i - start) // 2
            c = 'R'
        start = i
result[start] += (n - start) // 2 + (n - start) % 2
result[start - 1] += (n - start) // 2
print(*result)
