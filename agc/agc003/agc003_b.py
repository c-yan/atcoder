N = int(input())

result = 0
remainder = 0
for _ in range(N):
    A = int(input())
    result += (A + remainder) // 2
    if A == 0:
        remainder = 0
    else:
        remainder = (A + remainder) % 2
print(result)
