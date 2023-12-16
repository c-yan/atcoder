S = input()
T = int(input())

x = S.count('R') - S.count('L')
y = S.count('U') - S.count('D')
z = S.count('?')

if T == 1:
    print(abs(x) + abs(y) + z)
elif T == 2:
    if z <= abs(x) + abs(y):
        print(abs(x) + abs(y) - z)
    else:
        print((z - abs(x) + abs(y)) % 2)
