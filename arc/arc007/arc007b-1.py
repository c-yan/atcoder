N, M = map(int, input().split())

t = list(range(N + 1))
t[0] = None
player = 0
for _ in range(M):
    disk = int(input())
    t[player] = t[disk]
    player = disk
t = {t[i]: i for i in range(N + 1) if i != player}
print(*(t[k] for k in sorted(t)), sep='\n')
