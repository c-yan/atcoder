N = input()

if int(N) % sum(map(int, N)) == 0:
    print('Yes')
else:
    print('No')
