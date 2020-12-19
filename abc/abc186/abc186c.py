N = int(input())

result = 0
for i in range(1, N + 1):
    if oct(i).count('7') + str(i).count('7') == 0:
        result += 1
print(result)
