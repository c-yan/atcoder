from operator import itemgetter

N = int(input())
A = list(map(int, input().split()))

print(*[t[0] + 1 for t in sorted(enumerate(A), key=itemgetter(1))])
