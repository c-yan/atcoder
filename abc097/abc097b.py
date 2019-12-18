from math import sqrt

X = int(input())

result = 1
for i in range(2, int(sqrt(X)) + 1):
    t = i * i
    while t <= X:
        if t > result:
            result = t
        t *= i
print(result)
