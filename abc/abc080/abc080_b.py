N = int(input())

if N % sum(map(int, str(N))) == 0:
    print('Yes')
else:
    print('No')
