N = input()

if sum(int(c) for c in N) % 9 == 0:
    print('Yes')
else:
    print('No')
