from datetime import datetime, timedelta

Y, M, D = map(int, input().split('/'))

d = datetime(Y, M, D)
while True:
    if d.year % (d.month * d.day) == 0:
        print(d.strftime('%Y/%m/%d'))
        break
    d += timedelta(days = 1)
