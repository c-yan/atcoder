N = int(input())

a = N
while a % 2 == 0:
    a //= 2
a *= 2

result = 0
for i in range(1, int(a ** 0.5) + 1):
    if a % i != 0:
        continue
    result += 1
    if i * i != a:
        result += 1
print(result)
