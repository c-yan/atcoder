from math import atan, pi

a, b, x = map(int, input().split())

if x >= a * a * b / 2:
    print(atan((a*a*b-x)/(a*a*a/2))/(2 * pi)*360)
else:
    print(90 - atan(x/(a*b*b/2))/(2 * pi)*360)
