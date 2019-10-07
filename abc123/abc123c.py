N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

t = min(A, B, C, D, E)
print(4 + (N + (t - 1)) // t)
