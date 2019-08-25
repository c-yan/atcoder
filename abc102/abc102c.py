from sys import stdin
n, *a = map(int, stdin.read().split())
t = list(sorted(a[i] - (i + 1) for i in range(n)))
b = t[len(t) // 2]
print(sum(abs(a[i] - (b + i + 1)) for i in range(n)))
