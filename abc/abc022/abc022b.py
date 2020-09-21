from sys import stdin

readline = stdin.readline

N = int(readline())
t = set()
result = 0
for _ in range(N):
    A = int(readline())
    if A in t:
        result += 1
    else:
        t.add(A)
print(result)
