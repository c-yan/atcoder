from operator import itemgetter

N = int(input())
A = list(map(int, input().split()))

x = [(A[i - 1], i) for i in range(1, N + 1)]
x.sort(key=itemgetter(0))
y = [t[1] for t in x]
print(*y)
