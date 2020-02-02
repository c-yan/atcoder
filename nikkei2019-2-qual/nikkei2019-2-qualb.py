N = int(input())
D = list(map(int, input().split()))

if D[0] != 0:
    print(0)
    exit()

c = {}
for i in D:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1

if c[0] != 1:
    print(0)
    exit()

result = 1
for i in range(1, max(D) + 1):
    if i not in c:
        print(0)
        exit()
    result = result * (c[i - 1] ** c[i]) % 998244353
print(result)
