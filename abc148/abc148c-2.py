A, B = map(int, input().split())

for i in range(B):
    if A * (i + 1) % B  == 0:
        print(A * (i + 1))
        break
