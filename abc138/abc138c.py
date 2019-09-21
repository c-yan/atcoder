n = int(input())
v = [int(e) for e in input().split()]
v.sort()
result = v[0]
for i in range(1, n):
    result = (result + v[i]) / 2
print(result)
