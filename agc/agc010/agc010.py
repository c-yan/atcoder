N = int(input())
A = list(map(int, input().split()))

if sum(1 for i in A if i % 2 == 1) % 2 == 1:
    print('NO')
else:
    print('YES')
