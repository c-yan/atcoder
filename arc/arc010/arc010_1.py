N, M, A, B = map(int, input().split())

t = N
for i in range(M):
    if t <= A:
        t += B
    c = int(input())
    t -= c
    if t < 0:
        print(i + 1)
        break
else:
    print('complete')
