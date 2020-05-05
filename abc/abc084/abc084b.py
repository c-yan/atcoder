A, B = map(int, input().split())
S = input()

for i in range(A):
    if S[i] not in '0123456789':
        print('No')
        exit()
if S[A] != '-':
    print('No')
    exit()
for i in range(A + 1, A + B + 1):
    if A[i] not in '0123456789':
        print('No')
        exit()
print('Yes')
