from sys import stdin

readline = stdin.readline

T = int(readline())

result = []
for _ in range(T):
    N = int(readline())
    if N % 4 == 0:
        result.append('Even')
    elif N % 2 == 0:
        result.append('Same')
    elif N % 2 == 1:
        result.append('Odd')
print(*result, sep='\n')
