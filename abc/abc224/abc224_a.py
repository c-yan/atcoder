S = input()

a = S.rfind('er')
b = S.rfind('ist')

if a > b:
    print('er')
else:
    print('ist')
