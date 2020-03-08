S = input()

result = 'No'
for i in range(1, 6):
    if S == 'hi' * i:
        result = 'Yes'
        break
print(result)
