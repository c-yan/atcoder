from math import radians, cos, sin

a, b, d = map(int, input().split())

theata = radians(d)
print(a * cos(theata) - b * sin(theata), a * sin(theata) + b * cos(theata))
