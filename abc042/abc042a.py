A, B, C = map(int, input().split())
if list(sorted([A, B, C])) == [5, 5, 7]:
    print('YES')
else:
    print('NO')
