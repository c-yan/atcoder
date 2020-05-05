S = input()

for i in range(3):
    if S[i] not in '0123456789':
        print('error')
        exit()
print(int(S) * 2)
