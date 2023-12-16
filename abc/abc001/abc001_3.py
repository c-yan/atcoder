from decimal import Decimal
from bisect import bisect_left

Deg, Dis = map(int, input().split())

a = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
     'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
b = [Decimal(x) for x in ['0.2', '1.5', '3.3', '5.4', '7.9',
                          '10.7', '13.8', '17.1', '20.7', '24.4', '28.4', '32.6']]

W = bisect_left(b, Decimal(int((Decimal(Dis) / 60 + Decimal('0.05')) * 10)) / 10)
if W == 0:
    Dir = 'C'
else:
    Dir = a[(Deg * 10 + 1125) % 36000 * 16 // 36000]
print(Dir, W)
