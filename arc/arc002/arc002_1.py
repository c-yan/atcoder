Y = int(input())

is_leap_year = False
if Y % 4 == 0:
    is_leap_year = True
if Y % 100 == 0:
    is_leap_year = False
if Y % 400 == 0:
    is_leap_year = True

if is_leap_year:
    print('YES')
else:
    print('NO')
