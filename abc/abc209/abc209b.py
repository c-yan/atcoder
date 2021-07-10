N, X, *A = map(int, open(0).read().split())

if sum(A) - N // 2 <= X:
    print('Yes')
else:
    print('No')
