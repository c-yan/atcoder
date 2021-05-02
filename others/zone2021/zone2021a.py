S = input()

result = 0
i = 0
while True:
    i = S.find('ZONe', i) + 1
    if i == 0:
        break
    result += 1
print(result)
