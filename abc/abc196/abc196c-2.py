N = int(input())

result = 0
for i in range(1, 1000000):
    if int(str(i) * 2) > N:
        break
    result += 1
print(result)
