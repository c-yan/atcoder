s = input()

for i in range(len(s) // 2):
    if s[i] != '*' and s[len(s) - 1 - i] != '*' and s[i] != s[len(s) - 1 - i]:
        break
else:
    print('YES')
    exit()
print('NO')
