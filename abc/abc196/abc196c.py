N = input()

if len(N) % 2 == 1:
    N = '9' * (len(N) - 1)
if len(N) == 0:
    print(0)
    exit()

a = N[:len(N) // 2]
b = int(N)
result = 0
for i in range(1, int(a) + 1):
    if int(str(i) * 2) > b:
        break
    result += 1
print(result)
