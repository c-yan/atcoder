N, A, B = map(int, input().split())

N %= A + B
if N == 0 or N > A:
    print('Bug')
else:
    print('Ant')
