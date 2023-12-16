A, B, C, D = map(int, input().split())

s = sum([A, B, C, D])
for x in [A, B, C, D, A + B, A + C, A + D, B + C, B + D, C + D]:
    if x == s - x:
        print('Yes')
        break
else:
    print('No')
