N = int(input())
L = list(map(int, input().split()))

L.sort()
print(sum(L[::2]))
