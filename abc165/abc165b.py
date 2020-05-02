X = int(input())

t = 100
result = 0
while t >= X:
    t += t // 100
    result += 1
print(result)
