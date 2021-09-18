X = input()
N = int(input())
S = [input() for _ in range(N)]

t = {}
for i in range(26):
    t[X[i]] = chr(i + ord('a'))

print(*sorted(S, key=lambda s: ''.join(t[c] for c in s)), sep='\n')
