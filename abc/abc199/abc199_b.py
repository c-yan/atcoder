N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = max(A)
b = min(B)

if a > b:
    print(0)
else:
    print(b - a + 1)
