L, *B = map(int, open(0).read().split())

A = [0] * L
for i in range(L - 1):
    A[i + 1] = A[i] ^ B[i]

if B[L - 1] != A[L - 1] ^ A[0]:
    print(-1)
    exit()

print(*A, sep='\n')
