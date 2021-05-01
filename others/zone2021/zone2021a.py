S = input()

result = 0
i = 0
while i != -1:
    i = S.find('ZONe', i)
    if i == -1:
        continue
    result += 1
    i += 1
print(result)
