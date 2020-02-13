N = int(input())

t = {}
for i in range(1, N + 1):
    t[i] = int(input())

i = 1
result = 1
while True:
    if t[i] == -1:
        print(-1)
        exit()
    if t[i] == 2:
        print(result)
        exit()
    result += 1
    j = t[i]
    t[i] = -1
    i = j
