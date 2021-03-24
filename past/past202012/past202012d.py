N = int(input())
S = [input() for _ in range(N)]

def f(s):
    lz = 0
    for c in s:
        if c != '0':
            break
        lz += 1
    return (int(s), -lz)


S.sort(key=f)
print(*S, sep='\n')
