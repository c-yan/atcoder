from datetime import datetime

S = input()

d = datetime.strptime(S, '%Y/%m/%d')
if d <= datetime(2019, 4, 30):
    print('Heisei')
else:
    print('TBD')
