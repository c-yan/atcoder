N = int(input())
c = input()

d = list(c)

i = 0
j = N - 1
result = 0
while True:
    while i < N and d[i] != 'W':
        i += 1
    while j > 0 and d[j] != 'R':
        j -= 1
    if i == N or j == -1 or i >= j:
        break
    d[i] = 'R'
    d[j] = 'W'
    result += 1
print(result)
