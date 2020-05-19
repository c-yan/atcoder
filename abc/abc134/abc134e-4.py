from bisect import bisect_right

N = int(input())
A = [int(input()) for _ in range(N)]

t = [-A[0]]
for a in A[1:]:
    if a <= -t[-1]:
        t.append(-a)
    else:
        t[bisect_right(t, -a)] = -a
print(len(t))
