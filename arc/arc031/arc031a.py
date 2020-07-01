Name = input()

for i in range(len(Name) // 2):
    if Name[i] != Name[len(Name) - 1 - i]:
        print('NO')
        break
else:
    print('YES')
