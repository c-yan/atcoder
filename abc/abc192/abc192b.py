S = input()

for i in range(0, len(S), 2):
    if S[i] != S[i].lower():
        print('No')
        exit()

for i in range(1, len(S), 2):
    if S[i] != S[i].upper():
        print('No')
        exit()

print('Yes')
