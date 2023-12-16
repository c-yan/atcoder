def conv(x):
    return int(''.join(t[c] for c in x))

b = input().split()
N = int(input())
a = [input() for _ in range(N)]

t = {b[i]: str(i) for i in range(10)}
a.sort(key = lambda x: conv(x))
print(*a, sep='\n')
