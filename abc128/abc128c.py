from functools import reduce

N, M = map(int, input().split())
s = [list(map(int, input().split()))[1:] for _ in range(M)]
p = list(map(int, input().split()))

t = [reduce(lambda x, y: x | (1 << (y - 1)), e, 0) for e in s]
result = 0
for i in range(2 ** N):
    for j in range(M):
        if (bin(i & t[j]).count('1') & 1) != p[j]:
            break
    else:
        result += 1
print(result)
