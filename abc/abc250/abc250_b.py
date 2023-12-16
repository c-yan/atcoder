N, A, B = map(int, input().split())

l = ('.' * B + '#' * B) * N

for i in range(N):
    for _ in range(A):
        if i % 2 == 0:
            print(l[:N * B])
        else:
            print(l[B:(N + 1) * B])
