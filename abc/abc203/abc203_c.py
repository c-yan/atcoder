from sys import stdin

readline = stdin.readline

N, K = map(int, readline().split())
AB = [list(map(int, readline().split())) for _ in range(N)]

AB.sort()
p = 0
result = 0
while K != 0:
    result += K
    K = 0
    while p < N and AB[p][0] <= result:
        K += AB[p][1]
        p += 1
print(result)
