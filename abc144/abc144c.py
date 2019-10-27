from math import sqrt
from sys import exit

N = int(input())

for i in range(int(sqrt(N)) + 1, -1, -1):
    if N % i == 0:
        print((i - 1) + (N // i - 1))
        exit()
