from math import sqrt

X = int(input())

result = int(sqrt(X * 2)) - 1  # n(n+1)/2 >= X  ->  (n+1)(n+1)/2 >= X
while result * (result + 1) // 2 < X:
    result += 1
print(result)
