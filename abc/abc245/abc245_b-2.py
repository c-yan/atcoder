N = int(input())
A = list(map(int, input().split()))

print(min(set(range(2002)) - set(A)))
