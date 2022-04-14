N = int(input())
A = list(map(int, input().split()))

a = set(A)
for i in range(2002):
    if i in a:
        continue
    print(i)
    break
