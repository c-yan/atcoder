from sys import exit

N = int(input())

if N % 2 == 1:
    print(0)
    exit()

result = 0
t = 10
while t <= N:
    result += N // t
    t *= 5
print(result)
