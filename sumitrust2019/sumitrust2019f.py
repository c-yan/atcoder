from sys import exit

T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

if A1 > B1:
    A1, B1 = B1, A1
    A2, B2 = B2, A2

if A2 < B2:
    print(0)
    exit()

if A1 * T1 + A2 * T2 < B1 * T1 + B2 * T2:
    print(0)
    exit()

if A1 * T1 + A2 * T2 == B1 * T1 + B2 * T2:
    print('infinity')
    exit()

a = B1 * T1 - A1 * T1
b = (A1 * T1 + A2 * T2) - (B1 * T1 + B2 * T2)
t = a // b

if a % b == 0:
    print(t * 2)
else:
    print(t * 2 + 1)
