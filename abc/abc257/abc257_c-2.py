from bisect import bisect_left

N = int(input())
S = input()
W = list(map(int, input().split()))

a = sorted(W[i] for i in range(N) if S[i] == '0')
b = sorted(W[i] for i in range(N) if S[i] == '1')
c = set()
for x in W:
    c.add(x - 1)
    c.add(x)
    c.add(x + 1)

result = 0
for x in c:
    result = max(result, bisect_left(a, x) + len(b) - bisect_left(b, x))
print(result)
