K = int(input())

a = 2
b = 1
for i in range(K - 1):
    a, b = a + b, a

print(a, b)
